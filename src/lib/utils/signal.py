import threading


class Event:
    def __init__(self):
        self._funcs = []
        self._threads = []


    def wait(self):
        e = threading.Event()

        self._threads.append(e)
        e.wait()


    # Decorator
    def connect(self, func):
        self._funcs.append(func)


    def _fire(self, *args):
        for t in self._threads:
            t.set()

        self._threads = []

        for func in self._funcs:
            func(*args)
