class Director(object):

    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, value):
        self._builder = value

    def build(self):
        self.builder.build()

    def product(self):
        return self.builder.product
