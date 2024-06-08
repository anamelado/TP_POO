import random
from pokemon import Pokemon

class Trainer:
    def __init__(self, nome: str, pokemon: Pokemon):
        self.nome = nome
        self.pokemon = pokemon

    def batalhar(self, cenario: 'Cenario'):
        outro_treinador = cenario.novo_inimigo()
        if self.pokemon and outro_treinador.pokemon:
            print(f"Batalha entre {self.nome} e {outro_treinador.nome}!")
            while self.pokemon.vida > 0 and outro_treinador.pokemon.vida > 0:
                self.pokemon.atacar(outro_treinador.pokemon)
                if outro_treinador.pokemon.vida <= 0:
                    print(f"{outro_treinador.nome}'s {outro_treinador.pokemon.nome} foi derrotado!")
                    self.pokemon.subir_de_nivel()
                    break
                outro_treinador.pokemon.atacar(self.pokemon)
                if self.pokemon.vida <= 0:
                    print(f"{self.nome}'s {self.pokemon.nome} foi derrotado!")
                    break
        else:
            print("Um dos treinadores não tem Pokémon para batalhar!")

    def __str__(self):
        return f"Treinador {self.nome} com Pokémon: {self.pokemon.nome}"
    
class Cenario:
    max_nivel = 3
    def __init__(self, nome_treinador: str):
        self.nome_treinador = nome_treinador
        self.pokemons_predefinidos = [
            Pokemon("Pikachu", 100, "1", "Elétrico"),
            Pokemon("Bulbasaur", 90, "1", "Água"),
            Pokemon("Charmander", 85, "1", "Fogo"),
            Pokemon("Squirtle", 95, "1", "Água"),
            Pokemon("Eevee", 80, "1", "Pedra")
        ]
        self.inimigos = [
            Pokemon("Onix", 1, "7", "Pedra"),
            Pokemon("Gyarados", 1, "8", "Água"),
            Pokemon("Arcanine", 1, "7", "Fogo"),
            Pokemon("Jolteon", 1, "7", "Elétrico"),
            Pokemon("Lapras", 1, "7", "Gelo")
        ]
        self.escolher_pokemon()
        self.iniciar_batalha()

    def escolher_pokemon(self):
        print("Escolha seu Pokémon:")
        for i, pokemon in enumerate(self.pokemons_predefinidos):
            print(f"{i + 1}. {pokemon.nome} (Nível: {pokemon.nivel}, Vida: {pokemon.vida}, Tipo: {pokemon.tipo})")

        escolha = int(input("Digite o número do Pokémon escolhido: ")) - 1
        if escolha < 0 or escolha >= len(self.pokemons_predefinidos):
            print("Escolha inválida!")
            return self.escolher_pokemon()

        pokemon_usuario = self.pokemons_predefinidos[escolha]
        self.usuario = Trainer(self.nome_treinador, pokemon_usuario)

    def novo_inimigo(self):
        pokemon_inimigo = random.choice(self.inimigos)
        treinador_inimigo = Trainer("Inimigo", pokemon_inimigo)
        return treinador_inimigo

    def iniciar_batalha(self):
        while self.usuario.pokemon.vida > 0 and int(self.usuario.pokemon.nivel) < self.max_nivel:
            print("\n \n")
            print(self.usuario)
            
            self.usuario.batalhar(self)
        if self.usuario.pokemon.vida == 0 :
            print ("Derrota!")
        else:
            print("Vitoria!")

cenario = Cenario("Joao")
