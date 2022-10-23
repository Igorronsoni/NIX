import functions.blocos as bl
import functions.anotacoes as at

def menu_main():
    print("\n          --- Menu ---          \n1. Novo bloco\n2. Visualizar blocos\n3. Nova anotacao\n4. Visualizar anotacoes\n")

def selec(opcao):
    match opcao:
        case 1:
            bl.gerar_bloco()
            return 1
        case 2:
            bl.visualizar()
            return 1
        case 3:
            at.nova()
            return 1
        case 4:
            at.visualizar()
            return 1
        case _:
            return 0

while True:
    menu_main()
    selec(int(input("Opcao: "))) or print("Tratar erros")
