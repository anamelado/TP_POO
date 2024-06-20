from typing import Type
from ataques import Ataques
from status import Status
from InterfacePokemon import InterfacePokemon

class Pokemon(InterfacePokemon, Status, Ataques):

    def __init__(self, nome: str, vida: int, nivel: str, tipo: str) -> None:
        Status.__init__(self, nome, vida, nivel)
        Ataques.__init__(self, tipo)

    def subir_de_nivel(self):
        self.nivel = str(int(self.nivel) + 1)
        self.vida = self.vida_base
        self.status_up(self.nivel)

    def atacar(self, pokemon: Type['InterfacePokemon']):
            self.definir_ataque()
            fator = self.multiplicador.get((self.tipo, pokemon.tipo), 1.0)
            dano = self.forca * fator
            pokemon.vida -= dano
            print(f"{self.nome} usou {self.atk_nome}! {pokemon.nome} agora tem {pokemon.vida} de vida.")

    def status_up(self, nivel):
        self.vida += int(nivel) * 5
        self.forca += int(nivel) * 2.5
