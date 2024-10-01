#3. Matriz identidade, na matemática, também conhecida como matriz 𝐼 ou matriz unitária, é uma
#matriz quadrada em que a diagonal principal contém apenas elementos 1 (um) e todos os outros
#elementos são 0 (zero). Crie uma função que gere uma matriz identidade 4x4

MI=[]
nLinhas=4
nColunas=4
def MatrixIdentidade4x4(nLinhas,nColunas):
    for x in range(nLinhas): #cria todos os zeros em 4x4
        novaLinha=[]
        for y in range(nColunas):
            novoElemento=0
            novaLinha.append(novoElemento)
        MI.append(novaLinha)
    for cont in range(4):    #troca os zeros por 1 na diagonal
        (MI[cont][cont])=1
        cont=cont+1
    return MI

MatrixIdentidade4x4(nLinhas,nColunas)
for L in range(len(MI)):      #leitor
    for C in range(len(MI[0])):
        print(MI[L][C], end="\t")
    print()

