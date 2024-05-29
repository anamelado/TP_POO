from ataques import Ataques
from status import Status
from abc import abstractmethod

class Pokemon(Status, Ataques):

    def __init__(self, nome: str, vida: int, nivel: str, tipo) -> None:
        super().__init__(nome, vida, nivel, tipo)
        

   # @abstractmethod
   # def status_up(self, nivel):
   #     pass