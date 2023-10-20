import regex
import os

padrao = r''

# Nome do arquivo de programa a ser lido
nome_arquivo = 'prog_AUX.py'

try:
    # Abre o arquivo em modo de leitura
    with open(nome_arquivo, 'r') as arquivo:
        # Lê o conteúdo do arquivo como uma string
        codigo_do_programa = arquivo.read()
except FileNotFoundError:
    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
except IOError as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")
else:
    # Agora, você tem o código do programa como uma string
    print("Conteúdo do programa:")
    print(codigo_do_programa)

