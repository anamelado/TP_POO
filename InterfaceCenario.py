from abc import ABC, abstractmethod

class InterfaceCenario(ABC):
    @abstractmethod
    def escolher_pokemon(self) -> None:
        pass

    @abstractmethod
    def novo_inimigo(self):
        pass

    @abstractmethod
    def iniciar_batalha(self) -> None:
        pass