# Caminho do projeto
PROJECT_DIR = /Users/aninhamelado/Desktop/python/POO/TP_POO

# Nome do ambiente virtual
VENV = $(PROJECT_DIR)/venv

# Interpretador Python a ser usado
PYTHON = $(VENV)/bin/python

# Regras
.PHONY: all setup install run clean

# Regra padrão
all: setup install run

# Configura o ambiente virtual
setup:
	python3 -m venv $(VENV)

# Instala as dependências
install: setup
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install pygame==2.5.2

# Executa o jogo
run:
	$(PYTHON) $(PROJECT_DIR)/main.py

# Limpa o ambiente
clean:
	rm -rf $(VENV)
	find $(PROJECT_DIR) -type f -name '*.pyc' -delete
	find $(PROJECT_DIR) -type d -name '__pycache__' -delete
