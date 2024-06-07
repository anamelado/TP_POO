from typing import List, Dict, Union, Type
from index import Pokemon
from abc import ABC, abstractmethod

class Ataques(ABC):

    def __init__(self, tipo: str) -> None:
        self.atk_nome
        self.forca 
        self.__tipo = tipo
        self.definir_ataque()

    @property
    def tipo(self):
        return self.__tipo

    def definir_ataque(self) -> None:
        if self.tipo == 'Elétrico':
            self.atk_nome = 'Choque do trovão'
            self.forca = 10
        elif self.tipo == 'Água':
            self.atk_nome = 'Hidrobomba'
            self.forca = 10
        elif self.tipo == 'Fogo':
            self.atk_nome = 'Lança-chamas'
            self.forca = 10
        elif self.tipo == 'Pedra':
            self.atk_nome = 'Pedra afiada'
            self.forca = 10
        elif self.tipo == 'Gelo':
            self.atk_nome = 'Vento congelante'
            self.forca = 10

    forca: Dict[Union[str, str], float] = {
        ('Elétrico', 'Água'): 2.0,
        ('Elétrico', 'Pedra'): 0.5,
        ('Fogo', 'Gelo'): 2.0,
        ('Fogo', 'Água'): 0.5,
        ('Água', 'Fogo'): 2.0,
        ('Água', 'Elétrico'): 0.5,
        ('Pedra', 'Elétrico'): 2.0,
        ('Pedra', 'Gelo'): 0.5,
        ('Gelo', 'Pedra'): 2.0,
        ('Gelo', 'Fogo'): 0.5
    }

    @abstractmethod
    def atacar(self, pokemon: Type[Pokemon]):
        pass
