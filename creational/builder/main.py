from abc import ABC, abstractmethod


class IPizzaBuilder(ABC):
    @abstractmethod
    def addOlive(self, olive: bool):
        pass

    @abstractmethod
    def addStuffedEdge(self, stuffed_edge_name: str):
        pass

    @abstractmethod
    def addMeat(self, meat_name: str):
        pass

    @abstractmethod
    def addTomato(self, tomato: bool):
        pass

    @abstractmethod
    def build(self):
        pass


class Pizza():
    def __init__(self, cheese_name: str, salsa_name: str, meat_name: str = None, tomato: bool = False, olive: bool = False, stuffed_edge_name: str = None):
        self.cheese_name = cheese_name
        self.salsa_name = salsa_name
        self.meat_name = meat_name
        self.tomato = tomato
        self.olive = olive
        self.stuffed_edge_name = stuffed_edge_name

    def __str__(self):
        return f'Pizza com queijo {self.cheese_name}, com molho {self.salsa_name}, com carne {self.meat_name}, com tomate {self.tomato}, com azeitona {self.olive}, com borda recheada de {self.stuffed_edge_name}'


class PizzaBuilder(IPizzaBuilder):
    def __init__(self, cheese_name: str, salsa_name: str):
        self.pizza = Pizza(cheese_name, salsa_name)

    def addOlive(self, olive: bool):
        self.pizza.olive = olive
        return self

    def addStuffedEdge(self, stuffed_edge_name: str):
        self.pizza.stuffed_edge_name = stuffed_edge_name
        return self

    def addMeat(self, meat_name: str):
        self.pizza.meat_name = meat_name
        return self

    def addTomato(self, tomato: bool):
        self.pizza.tomato = tomato
        return self

    def build(self):
        return self.pizza


if __name__ == '__main__':
    pizza = PizzaBuilder('Mussarela', 'Tomate com orégano').addMeat(
        'Picanha').addStuffedEdge('Cheedar').build()

    print(pizza)
