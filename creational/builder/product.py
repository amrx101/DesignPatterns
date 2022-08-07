class Product(object):
    def __init__(self):
        self._component_1 = None
        self._component_2 = None
        self._component_3 = None

    @property
    def component_1(self):
        return self._component_1

    @component_1.setter
    def component_1(self, value):
        self._component_1 = value

    @property
    def component_2(self):
        return self._component_2

    @component_2.setter
    def component_2(self, value):
        self._component_2 = value

    @property
    def component_3(self):
        return self._component_3

    @component_3.setter
    def component_3(self, value):
        self._component_3 = value
