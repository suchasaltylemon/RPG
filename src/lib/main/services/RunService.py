from . import Service

import os


@Service
class RunService:
    def __init__(self):
        pass


    def is_running(self):
        return os.getenv("SERVER") is not None


    def is_server(self):
        return os.getenv("SERVER") == "True"


    def is_client(self):
        return os.getenv("SERVER") == "False"
