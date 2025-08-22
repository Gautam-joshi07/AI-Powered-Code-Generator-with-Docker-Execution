import streamlit as st

from team.dsa_team import get_dsa_team
import asyncio
from config.docker_utils import start_docker_container,stop_docker_container
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult

st.title("AI-Powered Code Generator with Docker Execution")
st.write("welcome to DSA Problem solver")
task = st.text_input("enter your DSA problem")

async def run(team, docker, task):
    try:
         
        await start_docker_container(docker)
        async for message in team.run_stream(task=task):
            if isinstance(message, TextMessage):
                  print(msg:= f"{message.source}:{message.content}")
                  yield msg
            elif isinstance(message, TaskResult):
                  print(msg:= f"Stop Reason: {message.stop_reason}")
                  yield msg 

        print("Task Completed")
    except Exception as e:
        print("Error:{e}")
        yield f"Error: {e}"
    finally:
        await stop_docker_container(docker)


if st.button("Run"):
      
      st.write("Running the task")
      team, docker = get_dsa_team()
      async def collect_message():
            async for msg in run(team,docker,task):
                if isinstance(msg,str):
                    if msg.startswith("user:"):
                         with st.chat_message('user',avatar='https://cdn-icons-png.flaticon.com/128/9821/9821708.png'):
                            st.markdown(msg)
                    elif msg.startswith('problem_solver'):
                         with st.chat_message('assistant',avatar='https://cdn-icons-png.flaticon.com/128/9821/9821474.png'):
                              st.markdown(msg)
                    elif msg.startswith('CodeExecutorAgent'):
                         with st.chat_message('assistant',avatar='https://cdn-icons-png.flaticon.com/128/3917/3917705.png'):
                              st.markdown(msg)
                elif isinstance(msg, TaskResult):

                    st.markdown(f"Stop reason: {msg.stop_reason}")


      asyncio.run(collect_message())