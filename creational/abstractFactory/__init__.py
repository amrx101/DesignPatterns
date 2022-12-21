from abc import ABC, abstractmethod

class Button(ABC):

    @abstractmethod
    def press(self):
        raise NotImplementedError

class Key(ABC):

    @abstractmethod
    def press(self):
        raise NotImplementedError


class MacButton(Button):

    def press(self):
        print("Pressed MAC Button")


class MacKey(Key):

    def press(self):
        print("Pressed MAC Key")


class LinuxButton(object):

    def press(self):
        print("Pressed Linux Button")


class LinuxKey(object):

    def press(self):
        print("Pressed Linux Key")


class MacFactory(object):
    """
    This is a Factory Pattern for Mac OS.
    """

    def create(self, choice):
        if choice == "Key":
            return MacKey()
        if choice == "Button":
            return MacButton()


class LinuxFactory(object):
    """
    This is a Factory Pattern for Linux OS.
    """

    def create(self, choice):
        if choice == "Key":
            return LinuxKey()
        if choice == "Button":
            return LinuxButton()


class AbstractFactory(object):
    """
    This AbstractFactory class is Factory pattern
    implemented over the MacFactiry and LinuxFactory
    classes.

    Here we return to the client, an instance of
    MacFactory or LinuxFactory as per clients
    choice.
    """

    @classmethod
    def get_factory(cls, os):
        if os == "mac":
            return MacFactory()
        if os == "linux":
            return LinuxFactory()


if __name__ == "__main__":

    # client wants a MacFactory
    mac_factory = AbstractFactory.get_factory("mac")
    mac_button = mac_factory.create("Button")
    mac_button.press()

    # client wants a LinuxFactory
    linux_factory = AbstractFactory.get_factory("linux")
    linux_key = linux_factory.create("Key")
    linux_key.press()