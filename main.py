import functions.avancado as av 
import functions.blocos as bl
import functions.anotacoes as at
import functions.uteis as ut

def menu_main():
    print("\n          --- Menu ---          \n1. Novo bloco\n2. Visualizar blocos\n3. Nova anotacao\n4. Visualizar anotacoes\n5. Opcoes avancadas\n")

def selec(opcao):
    try: 
        opcao = int(opcao)
    except:
        return 0
    match opcao:
        case 1:
            return bl.gerar_bloco()
        case 2:
            return bl.visualizar()
        case 3:
            return at.nova()
        case 4:
            notas = bl.visualizar()
            if notas is not None:
                try:
                    nt = int(input("Digite o indice de um bloco de notas: "))
                    bl.visualizar(ut.ajuste_nome(notas[nt -1]))
                except:
                    print("\nProcesso cancelado por erro na insercao do indice")
            return 1
        case 5:
            return av.menu_avancado()
        case _:
            return 0

while True:
    menu_main()
    selec(input("Opcao: ")) or print("\nHouve um erro inesperado")
