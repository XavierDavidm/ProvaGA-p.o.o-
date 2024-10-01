#1. Dados os vetores 𝑣1 = [1,5,9,2,5], 𝑣2 = [7,4,13,21,6] e 𝑣𝑣3 = [8, −3,5,7,12], faça um programa
#que copie o conteúdo dos vetores dados para uma matriz de tamanho 3x5 de forma a obter o
#seguinte resultado:

v1=[1,5,9,2,5]
v2=[7,4,13,21,6] 
v3=[8,-3,5,7,12]

M=[]
M.append(v1)
M.append(v2)
M.append(v3)

#varredura tabela
for i in range(len(M)):
    for j in range(len(M[0])):
        print(M[i][j], end="\t")
    print()