from abc import ABC, abstractmethod
from typing import Type

class InterfacePokemon(ABC):

    @abstractmethod
    def subir_de_nivel(self) -> None:
        pass

    @abstractmethod
    def atacar(self, pokemon: Type['InterfacePokemon']) -> None:
        pass

    @abstractmethod
    def status_up(self, nivel: str) -> None:
        pass

