import random                                                                                                       # Importa o módulo random para gerar números aleatórios
from pokemon import Pokemon                                                                                         # Importa a classe Pokemon do arquivo pokemon.py
from typing import TYPE_CHECKING, Type
from InterfaceCenario import InterfaceCenario

if TYPE_CHECKING:
    from trainer import Trainer

pokemons_treinador = [                                                                                              # Lista de Pokémon pré-definidos para o jogador escolher
            Pokemon("Pikachu", 100, "1", "Elétrico"),
            Pokemon("Lapras", 80, "1", "Gelo"),
            Pokemon("Charmander", 85, "1", "Fogo"),
            Pokemon("Squirtle", 95, "1", "Água"),
            Pokemon("Eevee", 80, "1", "Pedra")
        ]

pokemons_inimigos =            [                                                                                    # Lista de inimigos
            Pokemon("Onix", 50, "7", "Pedra"),
            Pokemon("Gyarados", 50, "8", "Água"),
            Pokemon("Arcanine", 50, "7", "Fogo"),
            Pokemon("Jolteon", 50, "7", "Elétrico"),
            Pokemon("Lapras", 50, "7", "Gelo")
        ]
class Cenario(InterfaceCenario):                                                                            

    def __init__(self, nome_treinador: str) -> None:
        """
        :param nome_treinador: Nome do treinador
        """
        self.nome_treinador = nome_treinador                                                                        # Define o nome do treinador
        self.qnt_pokemons = self.definir_qnt_pokemons()
        self.pokemons_predefinidos = pokemons_treinador
        self.inimigos_disponiveis = pokemons_inimigos
        self.inimigos_utilizados = []

        self.escolher_pokemon()                                                                                     # Chama o método para o jogador escolher seu Pokémon
        self.iniciar_batalha()                                                                                      # Inicia a batalha

    def escolher_pokemon(self) -> None:
        """
        Permite ao jogador escolher um Pokémon da lista de Pokémon pré-definidos.
        """
        from trainer import Trainer
        print("Escolha seu Pokémon:")                                                                               # Imprime uma mensagem para o jogador escolher seu Pokémon
        for i, pokemon in enumerate(self.pokemons_predefinidos):
            print(f"{i + 1}. {pokemon.nome} (Nível: {pokemon.nivel}, Vida: {pokemon.vida}, Tipo: {pokemon.tipo})")  # Mostra as opções de Pokémon disponíveis

        escolha = int(input("Digite o número do Pokémon escolhido: ")) - 1                                          # Obtém a escolha do jogador
        if escolha < 0 or escolha >= len(self.pokemons_predefinidos):                                               # Verifica se a escolha é válida
            print("Escolha inválida. Digite o número correspondente ao pokémon.")                                   # Imprime uma mensagem de escolha inválida
            return self.escolher_pokemon()                                                                          # Chama recursivamente o método para o jogador escolher novamente

        pokemon_usuario = self.pokemons_predefinidos[escolha]                                                       # Obtém o Pokémon escolhido pelo jogador
        self.usuario = Trainer(self.nome_treinador, pokemon_usuario)                                                # Cria o treinador com o Pokémon escolhido pelo jogador

    def novo_inimigo(self) -> Type['Trainer']:
        """
        :return: Retorna um novo inimigo do tipo Trainer
        Seleciona aleatoriamente um novo Pokémon inimigo entre os disponíveis e o associa a um treinador inimigo.
        """
        from trainer import Trainer
        if not self.inimigos_disponiveis:
            return Trainer("x", random.choice(self.inimigos_utilizados))
        else:
            pokemon_inimigo = random.choice(self.inimigos_disponiveis)
            self.inimigos_disponiveis.remove(pokemon_inimigo)                                                       # Remove o inimigo escolhido da lista disponível
            treinador_inimigo = Trainer("Inimigo", pokemon_inimigo)
            self.inimigos_utilizados.append(treinador_inimigo)                                                      # Adiciona o inimigo utilizado na lista de utilizados
            return treinador_inimigo        

    def definir_qnt_pokemons(self) -> int:
        """
        :return: Retorna a quantidade de Pokémon que o treinador batalhará contra
        Solicita ao jogador a quantidade de Pokémon para a batalha. (1 Pokémon do jogador VS X Pokemóns do inimigo)
        """
        while True:
            try:
                qnt = int(input(f"Você quer batalhar contra quantos pokémons? "))
                if 1 <= qnt <= 10:
                    return qnt
                else:
                    print("Erro. Digite um número de 1 a 10.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro de 1 a 10.") 

    def iniciar_batalha(self) -> None:
        """
        Inicia a batalha entre o Pokémon do jogador e os Pokémon inimigos.
        """
        while self.usuario.pokemon.vida > 0 and int(self.usuario.pokemon.nivel) <= self.qnt_pokemons and self.inimigos_disponiveis:  # Enquanto o Pokémon do jogador estiver vivo e não atingir o nível máximo
            print("\n \n")
            print(self.usuario)                                                                                         # Mostra o estado atual do treinador e do Pokémon
            self.usuario.batalhar(self)
        
        self.fim_de_jogo() 

    def fim_de_jogo(self) -> None:
        """
        Verifica o estado final da batalha e imprime a mensagem apropriada.
        """
        if self.usuario.pokemon.vida <= 0:
            print(f"\n{self.usuario.pokemon.nome} está com {self.usuario.pokemon.vida} de vida. Você perdeu a batalha. \nFim de jogo.")
        elif int(self.usuario.pokemon.nivel) > self.qnt_pokemons:
            print(f"\n{self.usuario.pokemon.nome} atingiu o nível máximo de {self.usuario.pokemon.nivel}, pois derrotou os {self.qnt_pokemons} pokémons! \nA batalha se encerra aqui. \nFim de jogo.")
        elif not self.inimigos_disponiveis:
            print(f"\nTodos os inimigos foram derrotados. Parabéns! \nVitória de {self.usuario.nome}")
        else:
            print("Erro. Fim de jogo.")
