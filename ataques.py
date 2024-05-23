from typing import List, Dict, Union
from index import Pokemon

class Ataques:

    def __init__(self, nome:str, forca:int, tipo:str, pokemon:'Pokemon') -> None:
        self.nome = nome
        self.forca = forca
        self.tipo = pokemon.tipo

    def tipo(self) -> None:
        if self.tipo == 'Elétrico':
            self.nome = 'Choque do trovão'
            self.forca = 10
        elif self.tipo == 'Água':
            self.nome = 'Hidrobomba'
            self.forca = 10
        elif self.tipo == 'Fogo':
            self.nome = 'Lança-chamas'
            self.forca = 10
        elif self.tipo == 'Pedra':
            self.nome = 'Pedra afiada'
            self.forca = 10
        elif self.tipo == 'Gelo':
            self.nome = 'Vento congelante'
            self.forca = 10

    forca: Dict[tuple[str, str], float] = {
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