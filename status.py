from abc import ABC, abstractmethod                                         # Importa a classe ABC e o decorador abstractmethod do módulo abc

class Status(ABC):                                                          # Define a classe Status como uma subclasse de ABC (classe abstrata base)

    def __init__(self, nome:str, vida:float, nivel:str) -> None:            # Define o método de inicialização da classe Status
        self.nome = nome                                                    # Atribui o nome do Pokémon
        self.vida = vida                                                    # Atribui a vida do Pokémon
        self.vida_base = vida                                               # Define a vida base do Pokémon
        self._nivel = nivel                                                 # Atribui o nível do Pokémon (com o prefixo "_" para indicar que é protegido)

    @property                                                               # Define um método getter (propriedade) para acessar o nível do Pokémon
    def nivel(self):
        return self._nivel                                                  # Retorna o nível do Pokémon
    
    @nivel.setter                                                           # Define um método setter para modificar o nível do Pokémon
    def nivel(self, lvl):
        self._nivel = lvl                                                   # Define o novo nível do Pokémon

    @abstractmethod                                                         # Define um método abstrato que deve ser implementado nas subclasses
    def subir_de_nivel(self):                                               # Método abstrato para aumentar o nível do Pokémon
        pass                                                                # Corpo do método vazio, deve ser implementado nas subclasses
