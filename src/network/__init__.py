from .api import requests
import ref as enum

from typing import List
import socket
import threading

class _BaseService:
    def __init__(self, ip: str, port: int):
        self.info = (ip, port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def send(self, target: socket.socket, message: requests.Request):
        size = str(message.size).encode("utf-8")
        size += b" " * (enum.Etc.HEADER_SIZE.value - len(size))

        target.send(size)
        target.send(message.encode())


    def receive(self, target: socket.socket):
        size = int(target.recv(enum.Etc.HEADER_SIZE.value).decode("utf-8"))
        encoded_request = target.recv(size)

        request = requests.Request.decode(encoded_request)
        return request


class Client(_BaseService):
    def __init__(self, ip: str, port: int):
        super().__init__(socket.gethostbyname(ip), port)
        self.server: socket.socket = None


    def connect(self):
        self.socket.connect(self.info)
        self.server = self.socket


    def send(self, message):
        super().send(self.server, message)


    def receive(self):
        return super().receive(self.server)


class Server(_BaseService):
    def __init__(self, port: int):
        super().__init__(socket.gethostbyname(socket.gethostname()), port)

        self.socket.bind(self.info)
        self.raw_connections: List[socket.socket] = []


    def run(self):
        self.socket.listen(-1)
        print("Listening on {}:{}".format(*self.info))

        threading.Thread(target=self._handle_requests).start()


    def _handle_requests(self):
        running = True

        while running:
            socket, info = self.socket.accept()

            username = self.receive(socket)
            print(username.payload)

