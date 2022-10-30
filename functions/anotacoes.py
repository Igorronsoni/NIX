import functions.blocos as bl
import functions.globais as gb
import functions.uteis as ut

# Inicia o processo de gerar uma nova anotacao
# Parametros: - 
def nova():
    notas = bl.visualizar()
    try:
        nt = int(input("Digite o indice de um bloco de notas: "))
        bloco = ut.ajuste_nome(notas[nt -1])
        with open(gb.caminho + bloco, 'r') as doc:
            cl = doc.readlines()[0].split(gb.separador)
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
                        return 1

                anotacao += temp.capitalize()

                if coluna != len(cl) - 1:
                    anotacao += gb.separador

        with open(gb.caminho + bloco, 'a') as doc:
            doc.write(anotacao + "\n")
        print("\nAnotacao inserida com SUCESSO")
    except:
        print("\nProcesso cancelado por erro na insercao do indice")
    
    return 1
    
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