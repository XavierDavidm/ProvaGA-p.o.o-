#4. Escreva um algoritmo que preenche uma matriz 4x6 com valores inteiros aleatórios entre -10 e
#10. Calcule as somas:
#a. dos elementos da segunda linha
#b. dos elementos da quinta coluna
#c. da multiplicação dos elementos da primeira linha pelos elementos da quarta linha
#d. dos elementos só das colunas com índices pares
#e. dos elementos só das linhas com índices ímpares
import random
M=[]
nLinhas=4
nColunas=6

def geradorM(nLinhas,nColunas):
    for x in range(nLinhas):
        novaLinha=[]
        for y in range(nColunas):
            novoElemento=random.randint(-10,10)
            novaLinha.append(novoElemento)
        M.append(novaLinha)
    return M

geradorM(nLinhas,nColunas)
print(M)
#a.
print(sum(M[2-1]))

#b.
soma5=()
for cont in range(4):
    valor=(M[cont],[4])
    valor.append(soma5)
    cont+=1
print(sum(soma5))








