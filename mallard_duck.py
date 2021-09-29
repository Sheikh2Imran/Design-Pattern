from abc import abstractmethod


# interface
class FlyBehavior:
    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I am flying!")


# interface
class QuackBehavior:
    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print("I am quacking !")


# base class
class Duck:
    def __init__(self):
        self.fly_behavior = FlyBehavior()
        self.quack_behavior = QuackBehavior()
        
    def set_fly_behavior(self, fb):
        self.fly_behavior = fb
        
    def set_quack_behavior(self, qb):
        self.quack_behavior = qb

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def swim(self):
        print("All ducks swim, even decoys!")


class MallardDuck(Duck):
    def __init__(self):
        super(MallardDuck, self).__init__()
        self.set_fly_behavior(FlyWithWings())
        self.set_quack_behavior(Quack())

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()


if __name__ == "__main__":
    mallard_duck = MallardDuck()
    print(mallard_duck.perform_fly())
    print(mallard_duck.perform_quack())
