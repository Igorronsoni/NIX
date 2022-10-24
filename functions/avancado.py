import functions.blocos as bl

# Mostra opcoes avançadas dentro dos blocos e dentro das anotações
# Parametros: -
def menu_avancado():
    print("\n          --- Menu Avancado---          \n1. Deletar bloco de notas\n")
    try:
        op = int(input("Opcao: "))
    except:
        print("\nProcesso cancelado por erro na insercao do indice")
        return

    match op:
        case 1:
            blocos = bl.visualizar()
            try:
                doc = int(input("Digite o indice de um bloco de notas: "))
                bl.deletar(blocos[doc - 1])
            except:
                print("\nProcesso cancelado por erro na insercao do indice")
                return
            return 1
        case _:
            return 0