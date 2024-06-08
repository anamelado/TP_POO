from typing import Dict, Tuple                                                                          # Importa Dict e Tuple do módulo typing

class Ataques():                                                                                        # Define a classe Ataques

# Define um dicionário que mapeia tuplas de tipos de ataques para um fator de multiplicação
    multiplicador: Dict[Tuple[str, str], float] = {
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

    def __init__(self, tipo: str) -> None:                                                              # Define o método de inicialização da classe Ataques
        self.atk_nome = ''                                                                              # Inicializa o nome do ataque como uma string vazia
        self.forca = 0                                                                                  # Inicializa a força do ataque como 0
        self.__tipo = tipo                                                                              # Define o tipo de ataque (com o prefixo "__" para indicar que é privado)
        self.definir_ataque()                                                                           # Chama o método definir_ataque para configurar o nome e a força do ataque

    @property                                                                                           # Define um método getter (propriedade) para acessar o tipo de ataque
    def tipo(self):
        return self.__tipo                                                                              # Retorna o tipo de ataque
    
    def definir_ataque(self) -> None:                                                                   # Define o método definir_ataque
        if self.tipo == 'Elétrico':                                                                     # Se o tipo de ataque for elétrico
            self.atk_nome = 'Choque do trovão'                                                          # Define o nome do ataque como "Choque do trovão"
            self.forca = 10                                                                             # Define a força do ataque como 
        elif self.tipo == 'Água':                                                                       # Se o tipo de ataque for água
            self.atk_nome = 'Hidrobomba'                                                                # Define o nome do ataque como "Hidrobomba"
            self.forca = 10                                                                             # Define a força do ataque como 10
        elif self.tipo == 'Fogo':                                                                       # Se o tipo de ataque for fogo
            self.atk_nome = 'Lança-chamas'                                                              # Define o nome do ataque como "Lança-chamas"
            self.forca = 10                                                                             # Define a força do ataque como 10
        elif self.tipo == 'Pedra':                                                                      # Se o tipo de ataque for pedra
            self.atk_nome = 'Pedra afiada'                                                              # Define o nome do ataque como "Pedra afiada"
            self.forca = 10                                                                             # Define a força do ataque como 10
        elif self.tipo == 'Gelo':                                                                       # Se o tipo de ataque for gelo
            self.atk_nome = 'Vento congelante'                                                          # Define o nome do ataque como "Vento congelante"
            self.forca = 10                                                                             # Define a força do ataque como 10
