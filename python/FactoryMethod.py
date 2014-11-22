#!/usr/bin/python


class Pizza:
    name = ""
    dough = ""
    sauce = ""
    toppings = []

    def prepare(self):
        print "Preparing %s" % self.name
        print "    dough: %s" % self.dough
        print "    sauce: %s" % self.sauce
        print "    add toppings:"
        for n in self.toppings:
            print "        %s" % n

    def bake(self):
        print "Bake for 25 minutes at 350."

    def cut(self):
        print "Cutting into diagonal slices."

    def box(self):
        print "Put into official box."

    def get_name(self):
        return self.name


class PizzaStore:
    def order_pizza(self, pizza_type):
        self.pizza = self.create_pizza(pizza_type)
        self.pizza.prepare()
        self.pizza.bake()
        self.pizza.cut()
        self.pizza.box()
        return self.pizza

    def create_pizza(self, pizza_type):
        pass


class NYStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = "NY Style Cheese Pizza"
        self.dough = "NY Dough"
        self.sauce = "NY Sauce"
        self.toppings.append("NY toopping A")
        self.toppings.append("NY toopping B")


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = "Chicago Style Cheese Pizza"
        self.dough = "Chicago Dough"
        self.sauce = "Chicago Sauce"
        self.toppings.append("Chicago toopping A")

    def cut(self):
        print "Cutting into square slices."


class NYStyleClamPizza(Pizza):
    def __init__(self):
        self.name = "NY Style Clam Pizza"
        self.dough = "NY Dough"
        self.sauce = "NY Sauce"
        self.toppings.append("NY toopping A")
        self.toppings.append("NY toopping B")


class ChicagoStyleClamPizza(Pizza):
    def __init__(self):
        self.name = "Chicago Style Clam Pizza"
        self.dough = "Chicago Dough"
        self.sauce = "Chicago Sauce"
        self.toppings.append("Chicago toopping A")

    def cut(self):
        print "Cutting into square slices."


class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return NYStyleCheesePizza()
        elif pizza_type == "clam":
            return NYStyleClamPizza()
        else:
            return None


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return ChicagoStyleCheesePizza()
        elif pizza_type == "clam":
            return ChicagoStyleClamPizza()
        else:
            return None

if __name__ == "__main__":
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()

    pizza = ny_store.order_pizza("cheese")
    print "Mike ordered a %s." % pizza.get_name()
    print

    pizza = chicago_store.order_pizza("clam")
    print "John ordered a %s." % pizza.get_name()
    print

