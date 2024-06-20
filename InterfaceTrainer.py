from abc import ABC, abstractmethod
from InterfaceCenario import InterfaceCenario

class InterfaceTrainer(ABC):
    @abstractmethod
    def batalhar(self, cenario: 'InterfaceCenario') -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass