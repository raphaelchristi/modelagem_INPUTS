import regex as re
import os

dic_model = {}
new_list_inputs = []
padrao_geral = r'.*input.*'
padrao_count = r'.*='
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

#filtra os elementos que recebem algo
list_inputs = re.findall(padrao_geral,codigo_do_programa)
print(list_inputs)

for i in range(len(list_inputs)):
    new_list_inputs[i] = re.findall(padrao_count,list_inputs[i])

print(new_list_inputs)
#for i in range(len(list_inputs)):
#               
#               dic_model[i+1] = list_inputs[i]
#



