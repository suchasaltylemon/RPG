# lol

class Service:
    def __new__(cls, targetCls, *_, **__):
        if not hasattr(targetCls, "_singleton"):
            setattr(targetCls, "_singleton", targetCls())

            targetCls.__call__ = lambda *_: targetCls._singleton

        return targetCls._singleton

