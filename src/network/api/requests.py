import pickle


class Request:... # Allow typing
class Request:
    """Base class for all requests. Do not use"""

    #region properties
    @property
    def description(self):
        return self._description


    @property
    def title(self):
        return self._title


    @property
    def payload(self):
        return self._payload


    @property
    def size(self):
        encoded = self.encode()

        return len(encoded)
    #endregion

    def __init__(self, title: str, payload: any, description: str=""):
        self._title = title
        self._payload = payload
        self._description = description


    def encode(self):
        return pickle.dumps(self)


    @staticmethod
    def decode(request: bytes) -> Request:
        return pickle.loads(request)
