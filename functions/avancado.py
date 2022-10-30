import functions.blocos as bl
import functions.uteis as ut
import functions.anotacoes as an

# Recee a opcao e testa a mesma
# Parametros: op -> opcao desejada
def selec_menu_avancado(op):
    try: 
        op = int(op)
    except:
        return 0
    match op:
        case 1:
            blocos = bl.visualizar()
            try:
                doc = int(input("\nDigite o indice de um bloco de notas: "))
                confir = str(input(f"\nTem certeza que deseja deletar o bloco de notas '{ut.ajuste_nome(blocos[doc-1])}'? (S/N): "))
                if confir.lower() == "s":
                    bl.deletar_bloco(ut.ajuste_nome(blocos[doc-1]), doc - 1)
            except:
                print("\nProcesso cancelado por erro na insercao do indice")
                return 0
            return 1
        case 2:
            bloco = bl.visualizar()
            try:
                doc = int(input("\nDigite o indice de um bloco de notas: "))
                bl.visualizar(ut.ajuste_nome(bloco[doc - 1]))
                linha = int(input("\nDigite o indice da anotacao que deseja deletar: "))
                confir = str(input(f"\nTem certeza que deseja deletar a anotacao? (S/N): "))
                if confir.lower() == "s":
                    an.deletar_anotacao(linha, ut.ajuste_nome(bloco[doc - 1]))
            except:
                print("\nProcesso cancelado por erro na insercao do indice")
                return 0
        case _:
            return 0

# Mostra opcoes avançadas dentro dos blocos e dentro das anotações
# Parametros: -
def menu_avancado():
    print("\n          --- Menu Avancado---          \n1. Deletar bloco de notas\n2. Deletar uma anotacao\n")
    return selec_menu_avancado(input("Opcao: "))
    

    