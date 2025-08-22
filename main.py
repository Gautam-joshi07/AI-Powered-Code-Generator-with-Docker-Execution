from DSA_solver.team.dsa_team import get_dsa_team
import asyncio
from DSA_solver.config.docker_utils import start_docker_container,stop_docker_container
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult

async def main():
    dsa_team, docker = get_dsa_team()
    try:
        await start_docker_container(docker)
        print("Docker container started successfully")
        task = "write a python code for add two numbers and also show expected output"
        async for message in dsa_team.run_stream(task=task):
            if isinstance(message, TextMessage):
                print('=='*20)
                print(message.source, ":", message.content)

            elif isinstance(message, TaskResult):
                print('STop reson:',message.stop_reason)

    except Exception as e:
        print(f"error: {e}")

    finally:
        await stop_docker_container(docker)

if __name__=="__main__":
    asyncio.run(main())