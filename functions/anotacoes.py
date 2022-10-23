import functions.blocos as bl
import functions.globais as gb

# Gera uma nova anotacao dentro de um bloco
# Parametros: bloco -> nome do bloco / anotacao -> string da anotacao
def gerar(bloco, anotacao):
    doc = open(gb.caminho + bloco, 'a')
    doc.write(anotacao + "\n")
    doc.close()

# Inicia o processo de gerar uma nova anotacao
# Parametros: - 
def nova():
    notas = bl.visualizar()
    nt = int(input("Digite o indice de um bloco de notas: "))
    bloco = notas[nt -1][:-1]
    doc = open(gb.caminho + bloco, 'r')
    cl = doc.readlines()[0].split(",")
    anotacao = ""
    print(f"\n          --- {bloco} ---          \nOBS: Para cancelar a anotacao, digite a palavra 'cancelar'")
    for coluna in range(0, len(cl)):
        if "\n" not in cl[coluna]:
            col = cl[coluna]
        else: 
            col = cl[coluna][:-1]
        temp = str(input(col + ": "))
        
        if "cancelar" in temp.lower() and len(temp) < 10:
            if str(input("\nTem certeza que dejesa cancelar? (S/N): ")).lower() == "s":
                print("\nAnotacao CANCELADA com sucesso")
                doc.close()
                return

        anotacao += temp
        if coluna != len(cl) - 1:
            anotacao += ","

    doc.close()
    gerar(bloco,anotacao)

# Gera lista de anotacoes
def visualizar():
    notas = bl.visualizar()
    if notas is not None:
        nt = int(input("Digite o indice de um bloco de notas: "))
        bl.visualizar(notas[nt -1][:-1])
     