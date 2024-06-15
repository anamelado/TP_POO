from ataques import Ataques                                                                 # Importa a classe Ataques do arquivo ataques.py
from status import Status                                                                   # Importa a classe Status do arquivo status.py
from typing import Type                                                                     # Importa o tipo Type do módulo typing

class Pokemon(Status, Ataques):                                                             # Define a classe Pokemon como uma subclasse de Status e Ataques
    
    def __init__(self, nome: str, vida: int, nivel: str, tipo: str) -> None:                # Define o método de inicialização da classe Pokemon
        Status.__init__(self, nome, vida, nivel)                                            # Chama o método de inicialização da classe Status
        Ataques.__init__(self, tipo)                                                        # Chama o método de inicialização da classe Ataques
    
    def subir_de_nivel(self) -> None:                                                       # Define o método subir_de_nivel
        self.nivel = str(int(self.nivel) + 1)                                               # Aumenta o nível do Pokémon em 1
        self.vida = self.vida_base                                                          # Reseta a vida do Pokémon para o valor base
        self.status_up(self.nivel)                                                          # Chama o método status_up para atualizar os atributos do Pokémon conforme o novo nível
    
    def atacar(self, pokemon: Type['Pokemon']) -> None:                                     # Define o método atacar
        fator = self.multiplicador.get((self.tipo, pokemon.tipo), 1.0)                      # Calcula o fator de multiplicação do ataque com base nos tipos dos Pokémon
        dano = self.forca * fator                                                           # Calcula o dano do ataque
        pokemon.vida -= dano                                                                # Reduz a vida do Pokémon adversário de acordo com o dano causado
        print(f"{self.nome} atacou {pokemon.nome} com {self.atk_nome}! {pokemon.nome} agora tem {pokemon.vida} de vida.")  # Imprime uma mensagem sobre o ataque realizado
    
    def status_up(self, nivel) -> None:                                                     # Define o método status_up
        self.vida += int(nivel) * 5                                                         # Aumenta a vida do Pokémon com base no novo nível
        self.forca += int(nivel) * 2.5                                                      # Aumenta a força do Pokémon com base no novo nível
