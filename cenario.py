import random                                                                                               # Importa o módulo random para gerar números aleatórios
from pokemon import Pokemon                                                                                 # Importa a classe Pokemon do arquivo pokemon.py

class Trainer:
    def __init__(self, nome: str, pokemon: Pokemon) -> None:
        self.nome = nome                                                                                    # Define o nome do treinador
        self.pokemon = pokemon                                                                              # Define o Pokémon do treinador

    def batalhar(self, cenario: 'Cenario') -> None:                                                         # Define o método de batalha do treinador
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
        return f"Treinador {self.nome} com Pokémon: {self.pokemon.nome}"                                    # Define a representação em string do treinador

class Cenario:
    max_nivel = 3                                                                                         # Define o nível máximo para a batalha

    def __init__(self, nome_treinador: str) -> None:
        self.nome_treinador = nome_treinador                                                                # Define o nome do treinador
        self.pokemons_predefinidos = [                                                                      # Lista de Pokémon pré-definidos para o jogador escolher
            Pokemon("Pikachu", 100, "1", "Elétrico"),
            Pokemon("Bulbasaur", 90, "1", "Água"),
            Pokemon("Charmander", 85, "1", "Fogo"),
            Pokemon("Squirtle", 95, "1", "Água"),
            Pokemon("Eevee", 80, "1", "Pedra")
        ]
        self.inimigos = [                                                                                   # Lista de inimigos
            Pokemon("Onix", 50, "7", "Pedra"),
            Pokemon("Gyarados", 50, "8", "Água"),
            Pokemon("Arcanine", 50, "7", "Fogo"),
            Pokemon("Jolteon", 50, "7", "Elétrico"),
            Pokemon("Lapras", 50, "7", "Gelo")
        ]
        self.escolher_pokemon()                                                                             # Chama o método para o jogador escolher seu Pokémon
        self.iniciar_batalha()                                                                              # Inicia a batalha

    def escolher_pokemon(self) -> None:
        print("Escolha seu Pokémon:")                                                                               # Imprime uma mensagem para o jogador escolher seu Pokémon
        for i, pokemon in enumerate(self.pokemons_predefinidos):
            print(f"{i + 1}. {pokemon.nome} (Nível: {pokemon.nivel}, Vida: {pokemon.vida}, Tipo: {pokemon.tipo})")  # Mostra as opções de Pokémon disponíveis

        escolha = int(input("Digite o número do Pokémon escolhido: ")) - 1                                          # Obtém a escolha do jogador
        if escolha < 0 or escolha >= len(self.pokemons_predefinidos):                                               # Verifica se a escolha é válida
            print("Escolha inválida. Digite o número correspondente ao pokémon.")                                                                              # Imprime uma mensagem de escolha inválida
            return self.escolher_pokemon()                                                                          # Chama recursivamente o método para o jogador escolher novamente

        pokemon_usuario = self.pokemons_predefinidos[escolha]                                                       # Obtém o Pokémon escolhido pelo jogador
        self.usuario = Trainer(self.nome_treinador, pokemon_usuario)                                                # Cria o treinador com o Pokémon escolhido pelo jogador

    def novo_inimigo(self) -> Trainer:
        pokemon_inimigo = random.choice(self.inimigos)                                                              # Escolhe um inimigo aleatório
        treinador_inimigo = Trainer("Inimigo", pokemon_inimigo)                                                     # Cria um treinador inimigo com o Pokémon escolhido aleatoriamente
        return treinador_inimigo                                                                                    # Retorna o treinador inimigo

    def iniciar_batalha(self) -> None:
        while self.usuario.pokemon.vida > 0 and int(self.usuario.pokemon.nivel) < self.max_nivel:               # Enquanto o Pokémon do jogador estiver vivo e não atingir o nível máximo
            print("\n \n")
            print(self.usuario)                                                                                     # Mostra o estado atual do treinador e do Pokémon
            self.usuario.batalhar(self) 

Cenario = Cenario("Jogador")
