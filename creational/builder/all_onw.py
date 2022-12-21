from abc import ABC, abstractmethod

class BaseProduct(object):
    """
    This is the base Product Class
    """
    pass


class Product1(BaseProduct):
    def __init__(self):
        self._property1 = None
        self._property2 = None

    @property
    def property1(self):
        return self._property1

    @property1.setter
    def property1(self, prop):
        self._property1 = prop

    @property
    def property2(self):
        return self._property2

    @property2.setter
    def property2(self, prop):
        self._property2 = prop


class Product2(BaseProduct):
    def __init__(self):
        self._property1 = None
        self._property2 = None

    @property
    def property1(self):
        return self._property1

    @property1.setter
    def property1(self, prop):
        self._property1 = prop

    @property
    def property2(self):
        return self._property2

    @property2.setter
    def property2(self, prop):
        self._property2 = prop
"""
Product1 and Product2 are 2 classes with components property1 and property2
Idea is that these props are configurable.
"""

class BuilderInterface(ABC):

    @property
    @abstractmethod
    def product(self):
        raise NotImplementedError

    @abstractmethod
    def build_a(self):
        raise NotImplementedError

    @abstractmethod
    def build_b(selfs):
        raise NotImplementedError


class ConcereteBuilder1(BuilderInterface):
    def __init__(self):
        self._product = Product1()

    def product(self):
        product = self._product
        self._product = Product1()
        return product

    def build_a(self, prop):
        self._product.property1(prop)

    def build_b(self, prop):
        self._product.property2(prop)


class ConcreteBuilder2(BuilderInterface):
    def __init__(self):
        self._product = Product2()

    @property
    def product(self):
        prop = self._product
        self._product = Product2()
        return prop

    @abstractmethod
    def build_a(self, prop):
        self._product.property1(prop)

    @abstractmethod
    def build_b(self, prop):
        self._product.property2(prop)


class Director(object):
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder: BuilderInterface):
        self._builder = builder

    def build_minimal(self):
        self._builder.build_a("A")
        return self._builder.product

    def build(self):
        self._builder.build_a("A")
        self._builder.build_b("B")
        return self._builder.product


class Client(object):
    def __init__(self):
        self._directeor = Director()


    def make_product(self, version):
        if version == 1:
            self._directeor.builder = ConcereteBuilder1()
        else:
            self._directeor.builder = ConcreteBuilder2()
        product = self._directeor.builder.build()
        return product


