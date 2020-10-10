# component
class Abstract_Coffee(object):

    def get_price(self):
        pass

    def get_ingredients(self):
        pass

# concrete components
class Concrete_Coffee(Abstract_Coffee):
    def get_price(self):
        return 1.0

    def get_ingredients(self):
        return "coffee"

# decorator
class Abstract_Decorator(Abstract_Coffee):
    def __init__(self, accepted_coffee):
        self.accepted_coffee = accepted_coffee

    def get_price(self):
        return self.accepted_coffee.get_price()

    def get_ingredients(self):
        return self.accepted_coffee.get_ingredients()


# concrete decorators
class Milk(Abstract_Decorator):
    def __init__(self, accepted_coffee):
        Abstract_Decorator.__init__(self, accepted_coffee)

    def get_price(self):
        return self.accepted_coffee.get_price() + 0.3

    def get_ingredients(self):
        return self.accepted_coffee.get_ingredients()+ " with milk"


class Vanilla(Abstract_Decorator):
    def __init__(self, accepted_coffee):
        Abstract_Decorator.__init__(self, accepted_coffee)

    def get_price(self):
        return self.accepted_coffee.get_price() + 0.7

    def get_ingredients(self):
        return self.accepted_coffee.get_ingredients()+ " with vanilla"

# driver method
if __name__=="__main__":
    myCoffee = Concrete_Coffee()
    print("Coffee main price: ", myCoffee.get_price(), "Coffee main ingredients: ", myCoffee.get_ingredients())

    milkCoffee = Milk(myCoffee)
    print("Coffee price: ", milkCoffee.get_price(), "Coffee ingredients: ", milkCoffee.get_ingredients())

    vanillaCoffee = Vanilla(myCoffee)
    print("Coffee price: ", vanillaCoffee.get_price(), "Coffee ingredients: ", vanillaCoffee.get_ingredients())

    vanillaMilkCoffee = Vanilla(milkCoffee)
    print("Coffee price: ", vanillaMilkCoffee.get_price(), "Coffee ingredients: ", vanillaMilkCoffee.get_ingredients())

