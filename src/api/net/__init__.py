import socket
import threading

from . import requests as requests
from ..utils import signal as _signal


class _BaseService:
    HEADER_SIZE = 128
    ENCODING = "utf-8"


    def __init__(self, ip, port):
        hostname = socket.gethostbyname(ip)

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.info = (hostname, port)


    # Sends length and request to target socket
    def send(self, target: socket.socket, payload: requests._BaseRequest):
        payload_size = str(len(payload)).encode(self.ENCODING)

        padding = b" " * (self.HEADER_SIZE - len(payload_size))
        header_req = payload_size + padding # Send length of request

        target.send(header_req)
        target.send(payload.encode())


    async def receive(self, target: socket.socket):
        size = int(target.recv(self.HEADER_SIZE))
        message = target.recv(await size)

        return requests._BaseRequest.decode(await message)



class Server(_BaseService):
    def __init__(self, port=7092):
        self.running = False
        self.player_connected = _signal.Event()
        self._threads = []

        super().__init__(socket.gethostname(), port)


    def start(self):
        self.running = True

        t = threading.Thread(target=self._handle_requests)
        self._threads.append(t)
        t.start()


    async def _handle_requests(self):
        while self.running:
            ...




class Client(_BaseService):
    ...
