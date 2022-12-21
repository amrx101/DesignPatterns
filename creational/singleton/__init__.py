import threading


class SingletonMeta(type):

    _instances = dict()

    def __call__(cls, *args, **kwargs):
        print("CLS IS", cls)
        if cls in SingletonMeta._instances:
            return SingletonMeta._instances[cls]

        with threading.Lock():
            instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            SingletonMeta._instances[cls] = instance
        print(cls._instances)
        return SingletonMeta._instances[cls]


class ClientA(metaclass=SingletonMeta):

    def __init__(self, a, b):
        self._a = a
        self._b = b


class ClientB(metaclass=SingletonMeta):

    def __init__(self, a=None, b=None):
        self._a = a
        self._b = b


if __name__ == "__main__":
    ca1 = ClientA(10, 11)
    ca2 = ClientA(11, 12)
    assert id(ca1) == id(ca2)
    print(ca1._b, ca2._b)

    cb1 = ClientB()
    cb2 = ClientB()
    assert id(cb1) == id(cb2)
    assert id(ca1) != id(cb1)