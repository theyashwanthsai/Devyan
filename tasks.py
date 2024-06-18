from crewai import Task
from textwrap import dedent


class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def architecture_task(self, agent, tools, user_input):
        return Task(
            description=dedent(
                f"""
            Provide a high-level solution architecture for the given problem: {user_input}. 
            Your final answer must include a clear overview and major components involved.
            {self.__tip_section()}
            You have access to tools which can search the internet, read files, write files and create directories 
            """
            ),
            expected_output='A document outlining the high-level architecture.',
            tools=tools,
            agent=agent,
        )

    def implementation_task(self, agent, tools, context):
        return Task(
            description=dedent(
                f"""
            Implement the solution as per the architect's overview.
            Your final answer must include the code implementing the solution.                          
            {self.__tip_section()}
            You have access to tools which can read files, write files and create directories 
            """
            ),
            expected_output='Python code (py files) implementing the solution.',
            tools=tools,
            agent=agent,
            context=context
        )

    def testing_task(self, agent, tools, context):
        return Task(
            description=dedent(
                f"""
            Write and run test cases for the implemented code. 
            Your final answer must include test scripts and test results.                          
            {self.__tip_section()}
            You have access to tools which can read files, write files and create directories 
            """
            ),
            expected_output='Test scripts and test document for the implemented code.',
            tools=tools,
            agent=agent,
            context=context
        )

    def reviewing_task(self, agent, tools, context):
        return Task(
            description=dedent(
                f"""
            Review the work done by each agent at each step.
            Your final answer must include feedback and necessary revisions.
            You should also know how to run the application which can be useful to the users.
            {self.__tip_section()}
            You have access to tools which can read files, write files and create directories 
            """
            ),
            expected_output='Feedback and revisions for each step of the process. Also a final document which has steps to run the code given which can serve as a documentation for users',
            tools=tools,
            agent=agent,
            context=context
        )
