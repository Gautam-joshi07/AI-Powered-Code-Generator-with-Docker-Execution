from settings import get_model_client
from autogen_agentchat.agents import AssistantAgent


model_client = get_model_client()
def get_problem_solver_agent():
    """
        Function to get the problem solver agent
        This agent is responsible for solving DSA problem
        It will work with the code_executor_agent to execute the code
    """
    problem_solver_agent = AssistantAgent(
        name="problem_solver",
        model_client=model_client,
        system_message="""
            you are a problem solver agent thta isa an expert in solving DSA problem
            you will be working with code executor agent to execute code.
            you will be given a task and you should.
            at the begining of your response you have to specify your plan to solve the task.
            Then you should give code in a code block (Python).
            make sure that we have atleast 5 test cases for the code you write.
            after successfully run code explain it

            Once the code and explanation is done, you should ask the code executor agent to sav the code in a file
            like this
            ```python
            code = '''
                print("hello world")
            '''
            with open('solution.py','w') as f:
                f.write(code)
                print("Code saved successfully in solution.py")
            ```
            If the code executor fails, you should ask the code executor agent to retry the code execution.
            make sure to provide code in block.

            After all these  stop execution using 'STOP'.
        """
    )
    return problem_solver_agent