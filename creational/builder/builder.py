from .product import Product
from abc import ABC, abstractmethod


class BuilderInterface(ABC):
    def __init__(self):
        self._product = Product()

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value

    @abstractmethod
    def build_component_1(self):
        pass

    @abstractmethod
    def build_component_2(self):
        pass

    @abstractmethod
    def build_component_3(self):
        pass

    def build(self):
        self.build_component_1()
        self.build_component_2()
        self.build_component_3()


class ConcreteBuilderA(BuilderInterface):

    def build_component_1(self):
        self.product.component_1 = "AC1"

    def build_component_2(self):
        self.product.component_2 = "AC2"

    def build_component_3(self):
        self.product.component_3 = "AC3"


class ConcreteBuilderB(BuilderInterface):

    def build_component_1(self):
        self.product.component_1 = "BC1"

    def build_component_2(self):
        self.product.component_2 = "BC2"

    def build_component_3(self):
        self.product.component_3 = "BC3"