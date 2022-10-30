from xml.dom import InvalidAccessErr
import functions.globais as gb

# Salva os dados de um bloco e retorna o mesmo
# Parametros: nome -> nome do bloco a ser salvo as anotacoes
def salvar(nome):
    if type(nome) != str:
        return TypeError

    try:
        arqs = []
        with open(gb.caminho + ajuste_nome(nome), 'r') as arq:
            arqs = arq.readlines()
        return arqs    
    except InvalidAccessErr as error:
        return error

# Ajusta nome do bloco para retirar \n caso tenha
# Parametros: nome -> string de entrada
def ajuste_nome(nome):
    if type(nome) != str:
        return TypeError
    
    try:
        return str(nome).replace("\n", "")
    except InvalidAccessErr as error:
        return error