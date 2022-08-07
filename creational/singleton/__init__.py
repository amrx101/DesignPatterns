class Singleton(object):
    instance = None

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def Instantiate(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = cls(*args, **kwargs)
        return cls.instance

