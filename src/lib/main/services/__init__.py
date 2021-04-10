# lol

class Service:
    def __new__(cls, targetCls, *_, **__):
        if not hasattr(targetCls, "_singleton"):
            setattr(targetCls, "_singleton", targetCls())

        return lambda *_: targetCls._singleton

from . import RunService
