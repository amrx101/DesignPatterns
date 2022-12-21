from abc import ABC, abstractmethod


class Cake(ABC):

    @abstractmethod
    def get_flavour(self):
        raise NotImplementedError

    @abstractmethod
    def get_colour(self):
        raise NotImplementedError


class BananaCake(Cake):
    def __init__(self, flavour):
        self._flavour = flavour
        self._color = "yellow"

    def get_flavour(self):
        return self._flavour

    def get_colour(self):
        return self._color


class ChocolateCake(Cake):
    def __int__(self, flavour):
        self._flavour = flavour
        self._colour = "brown"

    def get_flavour(self):
        return self._flavour

    def get_colour(self):
        return self._colour


class CakeFactory(object):

    @classmethod
    def make_cake(cls, choice):
        if choice == "banana":
            return BananaCake()
        elif choice == "chocolate":
            return ChocolateCake()
        else:
            raise ModuleNotFoundError


class CakeClientProblematic(object):
    """
    Cake Client has issues with current implementation.
    """
    def make_cake_problematic(self, choice):
        """
        Problems with make_cake.
        There are following problems with make_cake:
            1. "Details" of how a cake is made should not in my opinion be the responsibility of
                CakeClient class. This detail should be hidden with cake Library.
            2. Imagine, there is a new cake(almond). In current impementation we would need to add
                an elif for this newly introduced cake. Now image this at scale. We can have very
                many flavours, which means. very many elif changes, compilation, etc etc. Not ideal.
        :param choice:
        :return:
        """
        if choice == "banana":
            return BananaCake()

        elif choice == "chocolate":
            return ChocolateCake()

        else:
            raise ModuleNotFoundError


class CakeClient(object):
    def make_cake(self, choice):
        """
        Here No matter if 1billion cakes are implemented tomorrow in the client library,
        we wont have a change. The change will only be with vendor.
        :param choice:
        :return:
        """
        return CakeFactory.make_cake(choice)
