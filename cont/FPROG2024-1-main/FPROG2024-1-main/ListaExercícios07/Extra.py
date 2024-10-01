#gerador de matrix baseado em n de linhas e colunas dados pelo user
import random

M=[]
nLinhas=int(input('digite o número de linhas: '))
nColunas=int(input('digite o número de Colunas: '))

#gerador
for x in range(nLinhas):
    novaLinha=[]
    for y in range(nColunas):
        novoElemento=random.randint(0,100)
        novaLinha.append(novoElemento)
    M.append(novaLinha)

#leitor com formatação
for x in range(len(M)):
    for y in range(len(M[0])):
        print(M[x][y], end='\t')
    print()