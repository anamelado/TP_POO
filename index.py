from pokemon import Pokemon
from status import Status
from ataques import Ataques
from typing import Type

class Pokemon(Status, Ataques):
    def subir_de_nivel(self):
        self.nivel = int(self.nivel) + 1
        self.status_up(self.nivel)
    
    def atacar(self, pokemon: Type[Pokemon]):
        pokemon.vida -= self.forca
    
    def status_up(self, nivel):
        self.vida += nivel*0,5
        self.forca += nivel*0,5

