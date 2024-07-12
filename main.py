import warnings
warnings.filterwarnings("ignore")

import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from decouple import config
from milvus_client import MilvusClient

from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks
from crewai_tools import FileReadTool
from tools.file_write import FileWriteTool
from tools.directory_write import DirWriteTool
from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()
file_read_tool = FileReadTool()
file_write_tool = FileWriteTool.file_write_tool
dir_write_tool = DirWriteTool.dir_write_tool

# Tools
architect_tools = [search_tool, file_read_tool, file_write_tool, dir_write_tool]
programmer_tools = [file_read_tool, file_write_tool, dir_write_tool]
tester_tools = [file_read_tool, file_write_tool, dir_write_tool]
reviewer_tools = [file_read_tool, file_write_tool, dir_write_tool]

os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")

class CustomCrew:
    def __init__(self, user_input):
        self.user_input = user_input
        self.milvus_client = MilvusClient()

    def run(self):
        agents = CustomAgents()
        tasks = CustomTasks()

        # Query Milvus for relevant code snippets
        query_embedding = self.get_query_embedding(self.user_input)
        code_snippets = self.milvus_client.search(query_embedding)

        # Agents
        architect_agent = agents.architect_agent(architect_tools)
        programmer_agent = agents.programmer_agent(programmer_tools)
        tester_agent = agents.tester_agent(tester_tools)
        reviewer_agent = agents.reviewer_agent(reviewer_tools)

        # Tasks
        architecture_task = tasks.architecture_task(architect_agent, architect_tools, self.user_input, code_snippets)
        implementation_task = tasks.implementation_task(programmer_agent, programmer_tools, [architecture_task])
        testing_task = tasks.testing_task(tester_agent, tester_tools, [implementation_task])
        reviewing_task = tasks.reviewing_task(reviewer_agent, reviewer_tools, [architecture_task, implementation_task, testing_task])

        crew = Crew(
            agents=[architect_agent, programmer_agent, tester_agent, reviewer_agent],
            tasks=[architecture_task, implementation_task, testing_task, reviewing_task],
            verbose=True,
        )

        result = crew.kickoff()
        return result

    def get_query_embedding(self, query):
        # Convert the query to an embedding using a pre-trained model
        from langchain.embeddings import OpenAIEmbeddings
        embeddings = OpenAIEmbeddings()
        query_embedding = embeddings.embed_query(query)
        return query_embedding

if __name__ == "__main__":
    print("\n####### Welcome to Devyan #######")
    print("---------------------------------")
    user_input = input("What problem do you want me to solve?\n")
    crew = CustomCrew(user_input)
    result = crew.run()

    print("\n\n########################")
    print("## Here is your crew run result:")
    print("########################\n")
    print(result)