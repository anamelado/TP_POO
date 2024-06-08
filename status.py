from abc import ABC, abstractmethod

class Status(ABC): 

    def __init__(self, nome:str, vida:float, nivel:str) -> None:
        self.nome = nome
        self.vida = vida
        self.vida_base = vida
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