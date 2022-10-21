import globais as gb

# Formata o bloco para a apresentacao na tela
# Parametro: numero -> index da lista do bloco ou das anotacoes / antc -> string da anotacao ou dos nomes dos blocos
def separar(numero, antc: str):
    ln = str(numero) + ". " if numero != 0 else "   "
    for i in antc.split(","):
        ln += i.strip() + ((gb.largura - len(i.strip())) * " ")
    return ln

# Apresenta na tela todas as anotacoes de um bloco caso seja passado um nome por paramtro, senao ele mostra todos os blocos
# Parametro: nome -> nome do bloco em especifico
def visualizar(nome: str = None):
    try:
        doc = open(nome, 'r')
        anotacoes = doc.readlines()
        print(separar(0, anotacoes[0]))
        for i in range(1, len(anotacoes)):
            print(separar(i, anotacoes[i]))
        doc.close()

    except:
        print("\n     --- Blocos de notas ---     ")
        try:
            doc = open(gb.nomeDosBlocos, 'r')
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
        nome = str(input("Titulo: "))
        try:
            doc = open(nome, 'x')
            doc.close()
            return nome
        except:
            print("Ja existe uma anotacao com este nome. Tente outro nome.")

# Gera as colunas para o bloco em questao
# Parametros: -
def colunas():
    array_colunas = []
    op = 1
    print("Digite 0 para cancelar")
    while op != "0":
        op = str(input("Digite o nome de uma coluna: "))
        if op == "0":
            return array_colunas    
        else:
            array_colunas.append(op)

# Gera o bloco
# Parametros: nome -> titulo do bloco / colunas -> colunas do bloco
def gerar_bloco(nome: str, colunas: list()):
    doc = open(nome, 'w')
    blocos = open(gb.nomeDosBlocos, 'a')
    for col in range(len(colunas)):
        doc.write(colunas[col])
        if col < len(colunas) - 1:
            doc.write(',')
    doc.write("\n")
    doc.close()
    blocos.write(nome + "\n")
    blocos.close()