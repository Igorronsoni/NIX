import os
import functions.globais as gb

# Formata o bloco para a apresentacao na tela
# Parametro: numero -> index da lista do bloco ou das anotacoes / antc -> string da anotacao ou dos nomes dos blocos
def separar(numero, antc: str):
    ln = str(numero) + ". " if numero != 0 else "   "
    for i in antc.split(gb.separador):
        ln += i.strip() + ((gb.largura - len(i.strip())) * " ")
    return ln

# Apresenta na tela todas as anotacoes de um bloco caso seja passado um nome por paramtro, senao ele mostra todos os blocos
# Parametro: nome -> nome do bloco em especifico
def visualizar(nome: str = None):
    try:
        doc = open(gb.caminho + nome, 'r')
        anotacoes = doc.readlines()
        print(f"\n     --- {nome} ---     ")
        print(separar(0, anotacoes[0]))
        for i in range(1, len(anotacoes)):
            print(separar(i, anotacoes[i]))
        doc.close()

    except:
        print("\n     --- Blocos de notas ---     ")
        try:
            doc = open(gb.caminho + gb.nomeDosBlocos, 'r')
            blocos = doc.readlines()
            for i in range(len(blocos)):
                print(f"{i + 1}. {blocos[i][:-1]}")
            doc.close()
            return blocos
        except:
            print("Nao existem blocos de notas ainda")

# Gera um titulo para o bloco em questao
# Parametros: -
def titulo():
    while True:
        print("Para cancelar a criacao do bloco, digite a palavra 'cancelar'")
        nome = str(input("Titulo: "))
        if "cancelar" in nome.lower() and len(nome) < 10:
            if str(input("Tem certeza que deseja cancelar a criacao do bloco? (S/N): ")).lower() == "s":
                return None
        if not os.path.exists(gb.caminho):
            os.mkdir("logs/docs")
        try:
            doc = open(gb.caminho + nome.capitalize(), 'x')
            doc.close()
            return nome.capitalize()
        except:
            print("Ja existe um bloco com este nome. Tente outro nome.")

# Gera as colunas para o bloco em questao
# Parametros: -
def colunas():
    array_colunas = []
    op = 1
    print("Digite 0 para terminar")
    while op != "0":
        op = str(input("Digite o nome de uma coluna: "))
        if op == "0":
            return array_colunas    
        else:
            array_colunas.append(op)

# Gera o bloco
# Parametros: nome -> titulo do bloco / colunas -> colunas do bloco
def gerar_bloco():
    nome = titulo()
    if nome is None:
        print("Cancelado com sucesso")
        return
    col = colunas()
    doc = open(gb.caminho + nome, 'w')
    blocos = open(gb.caminho + gb.nomeDosBlocos, 'a')
    for cl in range(len(col)):
        doc.write(col[cl])
        if cl < len(col) - 1:
            doc.write(gb.separador)
    doc.write("\n")
    doc.close()
    blocos.write(nome + "\n")
    blocos.close()

# Deleta um bloco de notas
# Parametro: nome -> nome do bloco em especifico
def deletar(nome: str):
    confir = str(input(f"\nTem certeza que deseja deletar o bloco de notas '{nome[:-1]}'? (S/N): "))
    if confir.lower() == "s":

        if os.path.exists(gb.caminho + nome[:-1]):
            os.remove(gb.caminho + nome[:-1])
            doc = open(gb.caminho + gb.nomeDosBlocos, 'r')
            arqs = doc.readlines()
            doc.close()
            with open(gb.caminho + gb.nomeDosBlocos, 'w') as file:
                newDoc = list()
                for line in arqs:
                    if line != nome:
                        newDoc.append(line)
                file.writelines(newDoc)
            print("\nBloco de notas apagado com SUCESSO")

        else:
            print("\nO bloco de notas selecionado nao existe")
                
    return 1
    
