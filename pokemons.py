from index import Ataques

class Pokemon:

    def __init__(self, nome:str, vida:int, tipo:str) -> None:
        self.nome = nome
        self.vida = vida
        self.tipo = tipo

    def atacar(self, pokemon2:'Pokemon', ataque:'Ataques') -> None: 
        print(f"{self.nome} usou {ataque.nome}")