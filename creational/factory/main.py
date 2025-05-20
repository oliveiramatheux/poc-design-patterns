from abc import ABC, abstractmethod

# === Product ===


class Transport(ABC):
    @abstractmethod
    def deliver(self) -> None:
        """Operação que cada transporte concreto deve implementar."""
        pass

# === ConcreteProducts ===


class Truck(Transport):
    def deliver(self) -> None:
        print("🚚 Entrega por terra: carregando em um caminhão.")


class Ship(Transport):
    def deliver(self) -> None:
        print("🚢 Entrega por mar: carregando em um navio.")

# === Creator ===


class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        """
        Factory Method.
        Subclasses concretas decidem qual objeto Transport criar.
        """
        pass

    def plan_delivery(self) -> None:
        """
        Método de template que usa o produto criado
        pela factory method.
        """
        transport = self.create_transport()
        # o cliente chama apenas a interface do produto
        transport.deliver()

# === ConcreteCreators ===


class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()    # gera Truck


class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()     # gera Ship

# === Client Code ===


def client_code(logistics: Logistics) -> None:
    """
    Recebe um Creator genérico e não precisa saber
    qual produto concreto será entregue.
    """
    logistics.plan_delivery()


if __name__ == "__main__":
    # Exemplo de uso: decide em tempo de execução
    for logistics in (RoadLogistics(), SeaLogistics()):
        client_code(logistics)
