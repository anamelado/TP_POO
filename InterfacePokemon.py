from abc import ABC, abstractmethod
from typing import Type

class InterfacePokemon(ABC):

    @property
    @abstractmethod
    def nome(self) -> str:
        pass

    @property
    @abstractmethod
    def vida(self) -> int:
        pass

    @vida.setter
    @abstractmethod
    def vida(self, vida: int) -> None:
        pass

    @property
    @abstractmethod
    def nivel(self) -> str:
        pass

    @nivel.setter
    @abstractmethod
    def nivel(self, nivel: str) -> None:
        pass

    @property
    @abstractmethod
    def tipo(self) -> str:
        pass

    @abstractmethod
    def subir_de_nivel(self) -> None:
        pass

    @abstractmethod
    def atacar(self, pokemon: Type['InterfacePokemon']) -> None:
        pass

    @abstractmethod
    def status_up(self, nivel: str) -> None:
        pass

