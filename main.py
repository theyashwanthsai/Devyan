import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from decouple import config

from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks

from crewai_tools import SerperDevTool, FileReadTool

search_tool = SerperDevTool()
file_read_tool = FileReadTool()

# Tools
architect_tools = [file_read_tool]
programmer_tools = [file_read_tool]
tester_tools = [file_read_tool]
reviewer_tools = [file_read_tool]

os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")


class CustomCrew:
    def __init__(self, user_input):
        self.user_input = user_input
    def run(self):
        agents = CustomAgents()
        tasks = CustomTasks()

        # Agents
        architect_agent = agents.architect_agent(architect_tools)
        programmer_agent = agents.programmer_agent(programmer_tools)
        tester_agent = agents.tester_agent(tester_tools)
        reviewer_agent = agents.reviewer_agent(reviewer_tools)

        # Tasks
        architecture_task = tasks.architecture_task(architect_agent, architect_tools, self.user_input)
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



if __name__ == "__main__":
    print("## Welcome to Devain##")
    print("-------------------------------")
    user_input = input("What problem do you want us to solve?")
    crew = CustomCrew(user_input)
    result = crew.run()
    
    print("\n\n########################")
    print("## Here is you crew run result:")
    print("########################\n")
    print(result)
