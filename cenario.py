from index import Pokemon
import  random

class Trainer:
    def __init__(self, nome: str, pokemon: Pokemon):
        self.nome = nome
        self.pokemon = pokemon

    def batalhar(self, outro_treinador: 'Trainer'):
        if self.pokemon and outro_treinador.pokemon:
            print(f"Batalha entre {self.nome} e {outro_treinador.nome}!")
            while self.pokemon.vida > 0 and outro_treinador.pokemon.vida > 0:
                self.pokemon.atacar(outro_treinador.pokemon)
                if outro_treinador.pokemon.vida <= 0:
                    print(f"{outro_treinador.nome}'s {outro_treinador.pokemon.nome} foi derrotado!")
                    break
                outro_treinador.pokemon.atacar(self.pokemon)
                if self.pokemon.vida <= 0:
                    print(f"{self.nome}'s {self.pokemon.nome} foi derrotado!")
                    break

    def __str__(self):
        return f"Treinador {self.nome} com Pokémon: {self.pokemon}"
    
    class Cenario:
        def __init__(self, nome_treinador: str):
            self.nome_treinador = nome_treinador
            self.pokemons_predefinidos = [
                Pokemon("Pikachu", 100, "5", "Elétrico"),
                Pokemon("Piplup", 90, "5", "Água"),
                Pokemon("Charmander", 85, "5", "Fogo"),
                Pokemon("Squirtle", 95, "5", "Água"),
                Pokemon("Geodude", 80, "5", "Pedra")
        ]
            self.inimigos = [
                Pokemon("Onix", 120, "7", "Pedra"),
                Pokemon("Gyarados", 110, "8", "Água"),
                Pokemon("Arcanine", 100, "7", "Fogo"),
                Pokemon("Jolteon", 90, "7", "Elétrico"),
                Pokemon("Lapras", 95, "7", "Gelo")
        ]

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

    def iniciar_batalha(self):
        pokemon_inimigo = random.choice(self.inimigos)
        treinador_inimigo = Trainer("Inimigo", pokemon_inimigo)

        print("\nEstado inicial:")
        print(self.usuario)
        print(treinador_inimigo)

        self.usuario.batalhar(treinador_inimigo)

        print("\nEstado final:")
        print(self.usuario)
        print(treinador_inimigo)

class Cenario:
    def __init__(self, nome_treinador: str):
        self.nome_treinador = nome_treinador
        self.pokemons_predefinidos = [
            Pokemon("Pikachu", 100, "5", "Elétrico"),
            Pokemon("Bulbasaur", 90, "5", "Água"),
            Pokemon("Charmander", 85, "5", "Fogo"),
            Pokemon("Squirtle", 95, "5", "Água"),
            Pokemon("Eevee", 80, "5", "Pedra")
        ]
        self.inimigos = [
            Pokemon("Onix", 120, "7", "Pedra"),
            Pokemon("Gyarados", 110, "8", "Água"),
            Pokemon("Arcanine", 100, "7", "Fogo"),
            Pokemon("Jolteon", 90, "7", "Elétrico"),
            Pokemon("Lapras", 95, "7", "Gelo")
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

    def iniciar_batalha(self):
        pokemon_inimigo = random.choice(self.inimigos)
        treinador_inimigo = Trainer("Inimigo", pokemon_inimigo)

        print("\nEstado inicial:")
        print(self.usuario)
        print(treinador_inimigo)

        self.usuario.batalhar(treinador_inimigo)

        print("\nEstado final:")
        print(self.usuario)
        print(treinador_inimigo)
