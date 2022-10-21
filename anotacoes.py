from blocos import visualizar
import globais as gb

# Gera uma nova anotacao dentro de um bloco
# Parametros: bloco -> nome do bloco / anotacao -> string da anotacao
def gerar(bloco, anotacao):
    doc = open(bloco, 'a')
    doc.write(anotacao)
    doc.close()

# Inicia o processo de gerar uma nova anotacao
# Parametros: - 
def nova():
    notas = visualizar()
    nt = int(input("Digite o indice de um bloco de notas: "))
    bloco = notas[nt -1][:-1]
    doc = open(bloco, 'r')
    cl = doc.readlines()[0].split(",")
    anotacao = ""
    for coluna in range(0, len(cl)):
        if "\n" not in cl[coluna]:
            col = cl[coluna]
        else: 
            col = cl[coluna][:-1]
        anotacao += str(input(col + ": "))
        
        if coluna != len(cl) - 1:
            anotacao += ","
    doc.close()
    gerar(bloco,anotacao)
     