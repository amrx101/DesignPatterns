import collections
from abc import ABC, abstractmethod


class ObserverIfc(ABC):
    """
    ObserverIFC,
    Every Obserrver has to implement the method which
    states what to do upon being nootfied by the Subject,

    Think Subs in PubSub (handle_event)
    """

    @abstractmethod
    def change_state(self):
        raise NotImplementedError


class SubjectIfc(ABC):
    """
    Every Subject has to implement a method:
    1. To add aobservers (register)
    2. To remove Observers (de-register)
    3. MNotify.

    Think of EVent Managers. We add subscribers to event maangers.
    """

    @abstractmethod
    def add_observer(self, observer):
        raise NotImplementedError

    @abstractmethod
    def remove_observer(self, observer):
        raise NotImplementedError

    @abstractmethod
    def notify(self):
        raise NotImplementedError


class Subject(SubjectIfc):

    def __init__(self):
        self._observers = set()

    def add_observer(self, observer):
        self._observers.add(observer)

    def remove_observers(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            try:
                observer.change_state()
            except Exception as e:
                pass


class Observer1(ObserverIfc):

    def change_state(self, *args, **kwargs):
        print("Change State called")


class Observer2(ObserverIfc):

    def change_state(self):
        print("Change state 2")


if __name__ == "__main__":
    sb = Subject()
    c1 = Observer1()
    c2 = Observer2()
    sb.add_observer(c1)
    sb.add_observer(c2)
    sb.notify()
