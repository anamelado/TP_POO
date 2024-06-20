from abc import ABC, abstractmethod
from InterfaceTrainer import InterfaceTrainer

class InterfaceCenario(ABC):
    @abstractmethod
    def escolher_pokemon(self) -> None:
        pass

    @abstractmethod
    def novo_inimigo(self) -> 'InterfaceTrainer':
        pass

    @abstractmethod
    def iniciar_batalha(self) -> None:
        pass