from index import Ataques
from abc import ABC, abstractmethod

class Pokemon(ABC):

    def __init__(self, nome:str, vida:int, tipo:str) -> None:
        self.nome = nome
        self.vida = vida
        self.tipo = tipo

    @abstractmethod
    def atacar(self, pokemon2:'Pokemon', ataque:'Ataques') -> None: 
        pass