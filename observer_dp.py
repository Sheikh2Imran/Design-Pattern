from abc import ABC, abstractmethod


class SubjectInterface(ABC):

    @abstractmethod
    def register(self, observer_obj):
        pass

    @abstractmethod
    def remove(self, observer_obj):
        pass

    def notify(self):
        pass


class ConcreteSubject(SubjectInterface):

    def __init__(self) -> None:
        super().__init__()
        self.observers = list()

    def register(self, observer_obj):
        self.observers.append(observer_obj)

    def remove(self, observer_obj):
        self.observers.remove(observer_obj)

    def notify(self):
        for observer_obj in self.observers:
            observer_obj.update()




