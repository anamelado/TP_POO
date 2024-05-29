from index import Ataques
from abc import ABC, abstractmethod

class Status(ABC): #a antiga classe mãe Pokemon agora está como Status para legibilidade

    def __init__(self, nome:str, vida:int, nivel:str) -> None:
        self.nome = nome
        self.vida = vida
        self._nivel = nivel

    @property
    def nivel(self):
        return self._nivel
    
    @nivel.setter
    def nivel(self, lvl):
        self._nivel = lvl

    @abstractmethod
    def subir_de_nivel(self):
        pass