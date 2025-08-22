

async def start_docker_container(docker):
    print("starting docker container")
    await docker.start()

async def stop_docker_container(docker):
    print("starting docker container")
    await docker.stop()

