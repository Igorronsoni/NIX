import functions.blocos as bl
import functions.globais as gb
import functions.uteis as ut

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
    try:
        nt = int(input("Digite o indice de um bloco de notas: "))
    except:
        print("\nProcesso cancelado por erro na insercao do indice")
        return
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

        anotacao += temp.capitalize()

        if coluna != len(cl) - 1:
            anotacao += gb.separador

    doc.close()
    gerar(bloco,anotacao)

# Gera lista de anotacoes
def visualizar():
    notas = bl.visualizar()
    if notas is not None:
        try:
            nt = int(input("Digite o indice de um bloco de notas: "))
        except:
            print("\nProcesso cancelado por erro na insercao do indice")
            return
        bl.visualizar(notas[nt -1][:-1])

# Deleta anotacao em especifico
# Parametros: linha -> numero da linha a ser deletado do bloco / bloco -> bloco em que esta esta anotacao
def deletar_anotacao(linha, bloco):
    arq = ut.salvar(bloco)
    with open(gb.caminho + ut.ajuste_nome(bloco), 'w') as new_bloco:
        new_arq = list()
        for ln in range(len(arq)):
            if ln != linha:
                new_arq.append(arq[ln])
        new_bloco.writelines(new_arq)