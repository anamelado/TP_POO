from abc import ABC, abstractmethod
from typing import Dict, Tuple

class InterfaceAtaques(ABC):
    multiplicador: Dict[Tuple[str, str], float]

    @abstractmethod
    def definir_ataque(self) -> None:
        pass

    @property
    @abstractmethod
    def tipo(self) -> str:
        pass
