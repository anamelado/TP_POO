from cenario import Cenario

def main() -> None:
    while True:
        nome_jogador = input("Digite o seu nome de jogador: ")
        if nome_jogador.strip():  
            break
        else:
            print("Nome inválido. Por favor, digite um nome de jogador válido.")

    Cenario(nome_jogador)


main()