from director import Director
from builder import ConcreteBuilderA, ConcreteBuilderB


class Client(object):
    def __init__(self):
        self._director = Director()

    def build(self, type):
        if type == "A":
            self.buildA()
        else:
            self.buildB()
        return self._director.product()

    def buildA(self):
        self._director.builder = ConcreteBuilderA()
        self._director.build()

    def buildB(self):
        self._director.builder = ConcreteBuilderB()
        self._director.build()