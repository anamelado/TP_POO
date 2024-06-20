# TP_POO

# Simulador de Batalhas de Pokémon

## Resumo
Este é um simulador de batalhas de Pokémon desenvolvido em Python. O jogo permite que você escolha um Pokémon, enfrente treinadores inimigos e participe de batalhas até que seu Pokémon seja derrotado ou atinja o nível máximo.

## Estrutura do Projeto
O projeto está estruturado da seguinte forma:

ataques.py: Contém a classe Ataques e a interface InterfaceAtaques.
status.py: Contém a classe Status.
pokemon.py: Contém a classe Pokemon que herda da interface InterfacePokemon, de Status e Ataques.
trainer.py: Contém a classe Trainer e a interface InterfaceTrainer.
cenario.py: Contém a classe Cenario e a interface InterfaceCenario.
main.py: Arquivo principal que inicia o jogo.

## Requisitos
Python 3.7 ou superior.

## Instalação
Clone o repositório:

sh
Copiar código
git clone https://github.com/anamelado/TP_POO.git
cd TP_POO

sh
Copiar código
pip install -r requirements.txt
Executando o Jogo
Para iniciar o jogo, execute o arquivo cenario.py:

sh
Copiar código
python cenario.py

## Como Jogar
Ao iniciar o jogo, você será solicitado a escolher um Pokémon dentre as opções disponíveis.
Após escolher seu Pokémon, a batalha começará contra o computador, gerando treinadores inimigos aleatórios.
Durante a batalha, seu Pokémon e o Pokémon do inimigo se atacarão alternadamente até que um deles seja derrotado.
Se seu Pokémon vencer a batalha, ele subirá de nível e enfrentará outro treinador inimigo.
O jogo continua até que seu Pokémon seja derrotado ou atinja o nível máximo.

## Classes e Interfaces
1. Ataques e InterfaceAtaques
A classe `Ataques` define os tipos de ataques e suas forças. A interface `InterfaceAtaques` garante que qualquer classe que implemente ataques possua os métodos `definir_ataque` e a propriedade `tipo`.

2. Status
A classe `Status` é uma classe abstrata que define os atributos básicos de um Pokémon (nome, vida, nível).

3. Pokemon e InterfacePokemon
A classe `Pokemon` herda de Status e Ataques e implementa métodos para subir de nível, atacar e atualizar status. A interface `InterfacePokemon` garante que qualquer classe que represente um Pokémon implemente os métodos essenciais para o funcionamento do jogo, como `subir_de_nivel` e `atacar`.

4. Trainer e InterfaceTrainer
A classe `Trainer` representa um treinador de Pokémon e possui métodos para batalhar e exibir informações do treinador. A interface `InterfaceTrainer` garante que qualquer treinador implemente esses métodos.

5. Cenario e InterfaceCenario
A classe `Cenario` define o cenário de batalha, permitindo que o jogador escolha um Pokémon e enfrente treinadores inimigos. A interface `InterfaceCenario` garante que qualquer cenário implemente métodos para escolher Pokémon, gerar novos inimigos e iniciar batalhas.

## Contato
Para quaisquer dúvidas ou sugestões, entre em contato com seu-email@dominio.com.