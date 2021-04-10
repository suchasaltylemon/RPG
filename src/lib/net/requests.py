import pickle

class _BaseRequest: ...
class _BaseRequest:
    @property
    def name(self):
        return self._name


    @property
    def payload(self):
        return self._payload


    @property
    def description(self):
        return self._description


    def __init__(self, payload: any, name: str, description: str=""):
        self._payload = payload
        self._name = name
        self._description = description


    def __len__(self):
        return len(self.encode())


    def encode(self):
        return pickle.dumps(self)


    @staticmethod
    def decode(req: _BaseRequest):
        return pickle.loads(req)


class ConnectionRequest(_BaseRequest):
    pass

#TODO: Implement Connection request

