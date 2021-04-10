import lib.utils.io as io
import lib
import os


def create_server(port=7092):
    server = lib.net.Server(port)
    os.environ["SERVER"] = "True"

    return server


def create_client(ip, port=7092):
    client = lib.net.Client(ip, port)
    os.environ["SERVER"] = "False"

    return client


def run():
    option = io.Input.multichoice("Client or Server:", ["Server", "Client"])

    port = io.Input.ask("Port", 7092, int)
    if option == 0:
        server = create_server(port)

    else:
        ip = io.Input.ask("IP")
        client = create_client(ip, port)
