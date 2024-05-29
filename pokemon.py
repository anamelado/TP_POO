from ataques import Ataques
from status import Status
from abc import abstractmethod

class Pokemon(Status, Ataques):

    def __init__(self, nome: str, vida: int, nivel: str, tipo: str) -> None:
        Status.__init__(self, nome, vida, nivel)
        Ataques.__init__(self, tipo)
    
    @abstractmethod
    def status_up(self, nivel):
        pass