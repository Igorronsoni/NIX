import blocos as bl
import anotacoes as at

def menu_main():
    print("\n          --- Menu ---          \n1. Novo bloco\n2. Visualizar blocos\n3. Nova anotacao\n4. Visualizar anotacoes\n")

def selec(opcao):
    match opcao:
        case 1:
            bl.gerar_bloco(bl.titulo(), bl.colunas())
            return 1
        case 2:
            bl.visualizar()
            return 1
        case 3:
            at.nova()
            return 1
        case 4:
            notas = bl.visualizar()
            nt = int(input("Digite o indice de um bloco de notas: "))
            bl.visualizar(notas[nt -1][:-1])
            return 1
        case _:
            return 0

while True:
    menu_main()
    selec(int(input("Opcao: "))) or print("Tratar erros")
