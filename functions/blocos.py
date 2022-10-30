import os
import functions.globais as gb
import functions.uteis as ut
import functions.anotacoes as an

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
        with open(gb.caminho + ut.ajuste_nome(nome), 'r') as doc:
            anotacoes = doc.readlines()
            print(f"\n     --- {nome} ---     ")
            print(separar(0, anotacoes[0]))
            for i in range(1, len(anotacoes)):
                print(separar(i, anotacoes[i]))

    except:
        print("\n     --- Blocos de notas ---     ")
        try:
            with open(gb.caminho + gb.nomeDosBlocos, 'r') as doc:
                blocos = doc.readlines()
                for i in range(len(blocos)):
                    print(f"{i + 1}. {blocos[i][:-1]}")
                return blocos
        except:
            print("Nao existem blocos de notas ainda")
    
    return 1

# Gera um titulo para o bloco em questao
# Parametros: -
def titulo():
    while True:
        print("\n          --- Novo Bloco ---          \nOBS: Para cancelar a criacao do bloco, digite a palavra 'cancelar'")
        nome = str(input("Titulo: "))
        if "cancelar" in nome.lower() and len(nome) < 10:
            if str(input("Tem certeza que deseja cancelar a criacao do bloco? (S/N): ")).lower() == "s":
                return None
        if not os.path.exists(gb.caminho):
            os.mkdir("logs/docs")
        try:
            with open(gb.caminho + nome.capitalize(), 'x') as doc:
                pass
            return nome.capitalize()
        except:
            print("Ja existe um bloco com este nome. Tente outro nome.")

# Gera as colunas para o bloco em questao
# Parametros: -
def colunas():
    array_colunas = []
    op = ""
    print("OBS: Digite '0' para terminar a insercao de colunas")
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
        print("\nCancelado com sucesso")
        return 1
    col = colunas()
    with open(gb.caminho + ut.ajuste_nome(nome), 'w') as doc:
        with open(gb.caminho + ut.ajuste_nome(gb.nomeDosBlocos), 'a') as blocos:
            for cl in range(len(col)):
                doc.write(col[cl])
                if cl < len(col) - 1:
                    doc.write(gb.separador)
            doc.write("\n")
            blocos.write(nome + "\n")
    print(f"\nBloco {nome} criado com SUCESSO")
    return 1

# Deleta um bloco de notas
# Parametro: nome -> nome do bloco em especifico / linha -> linha em que o bloco vai estar dentro do bloco geral
def deletar_bloco(nome: str, linha):
    if os.path.exists(gb.caminho + nome):
        os.remove(gb.caminho + nome)
        an.deletar_anotacao(linha, gb.nomeDosBlocos)
        print(f"\nBloco '{nome}' apagado com SUCESSO")

    else:
        print("\nO bloco de notas selecionado nao existe")
        return 0

    return 1
    
