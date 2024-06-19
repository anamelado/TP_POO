from pokemon import Pokemon                                                                                 # Importa a classe Pokemon do arquivo pokemon.py
from cenario import Cenario

class Trainer:
    def __init__(self, nome: str, pokemon: Pokemon) -> None:
        """
        :param nome: Nome do treinador
        :param pokemon: Instância da classe Pokemon
        """
        self.nome = nome                                                                                    # Define o nome do treinador
        self.pokemon = pokemon                                                                              # Define o Pokémon do treinador

    def batalhar(self, cenario: 'Cenario') -> None:                                                         # Define o método de batalha do treinador
        """
        :param cenario: Instância da classe Cenario, representando o cenário da batalha
        """
        outro_treinador = cenario.novo_inimigo()                                                            # Obtém um novo treinador inimigo do cenário 
        if self.pokemon and outro_treinador.pokemon:                                                        # Verifica se ambos os treinadores possuem Pokémon
            print(f"Batalha entre {self.nome} e {outro_treinador.nome}!")                                   # Imprime uma mensagem sobre a batalha
            while self.pokemon.vida > 0 and outro_treinador.pokemon.vida > 0:                               # Enquanto os Pokémon estiverem vivos
                self.pokemon.atacar(outro_treinador.pokemon)                                                # O Pokémon do treinador ataca o Pokémon do outro treinador
                if outro_treinador.pokemon.vida <= 0:                                                       # Se o Pokémon do outro treinador for derrotado
                    print(f"{outro_treinador.pokemon.nome} de {outro_treinador.nome} foi derrotado! Parabéns!")  # Imprime uma mensagem de derrota do inimigo
                    self.pokemon.subir_de_nivel()                                                           # O Pokémon do treinador sobe de nível
                    break                                                                                   # Sai do loop de batalha
                outro_treinador.pokemon.atacar(self.pokemon)                                                # O Pokémon do outro treinador ataca o Pokémon do treinador
                if self.pokemon.vida <= 0:                                                                  # Se o Pokémon do treinador for derrotado
                    print(f"{self.pokemon.nome} de {self.nome} foi derrotado. Fim de jogo.")                             # Imprime uma mensagem de derrota do treinador
                    break                                                                                   # Sai do loop de batalha
        else:
            print("Um dos treinadores não tem Pokémon para batalhar.")                                      # Imprime uma mensagem caso um dos treinadores não tenha Pokémon

    def __str__(self) -> str:
        """
        :return: Retorna uma representação em string do treinador
        """
        return f"Treinador {self.nome} com Pokémon: {self.pokemon.nome}"                                    # Define a representação em string do treinador
