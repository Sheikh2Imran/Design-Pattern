from abc import ABC, abstractmethod

# the abstract creator class
class PizzaStore(ABC):
    def __init__(self) -> None:
        super().__init__()

    # factory method
    @abstractmethod
    def create_pizza(self, type: str):   
        pass

    def order_pizza(self, type):

        pizza = self.create_pizza(type)

        pizza.prepare()
        pizza.cut()
        pizza.bake()

        return pizza

# The concrete creator classes
class NYStylePizzaStore(PizzaStore):
    def create_pizza(self, type):
        ingredient_factory = NYIngredientFactory()

        if type == "cheese":
            pizza = CheesePizza(ingredient_factory)
            return pizza.prepare()

        elif type == "vegie":
            pizza = VegiePizza(ingredient_factory)
            return pizza.prepare()

# the abstract product class
class Pizza(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.name = None
        self.cheese = None
        self.sauce = None

    @abstractmethod
    def prepare(self):
        pass

    def cut(self):
        print("Cutting: ", self.name)

    def bake(self):
        print("Baking: ", self.name)


class CheesePizza(Pizza):
    def __init__(self, ingredient_factory) -> None:
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print("Preparing ", self.name)
        self.cheese = self.ingredient_factory.create_cheese()
        self.sauce = self.ingredient_factory.create_sauce()


class VegiePizza(Pizza):
    def __init__(self, ingredient_factory) -> None:
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print("Preparing ", self.name)
        self.cheese = self.ingredient_factory.create_cheese()
        self.sauce = self.ingredient_factory.create_sauce()


# ingredient factory
class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_cheese():
        pass

    @abstractmethod
    def create_sauce():
        pass


# Concrete ingredient factory
class NYIngredientFactory:
    def create_cheese():
        return PalmCheese()

    def create_sauce():
        return TomatoSauce()


# Concrete ingredient factory
class ChiIngredientFactory:
    def create_cheese():
        return LuluCheese()

    def create_sauce():
        return MarinaraSauce()


# concrete ingredient classes
class LuluCheese:
    def __init__(self) -> None:
        print("You have lulu cheese ingredient")


class PalmCheese:
    def __init__(self) -> None:
        print("You have palm cheese ingredient")


class TomatoSauce:
    def __init__(self) -> None:
        print("You have tomato sauce ingredient")

class MarinaraSauce:
    def __init__(self) -> None:
        print("You have mariana souce ingredient")


if __name__ == "__main__":
    ny_pizza_store = NYStylePizzaStore()
    ny_pizza_store.order_pizza("vegie")
