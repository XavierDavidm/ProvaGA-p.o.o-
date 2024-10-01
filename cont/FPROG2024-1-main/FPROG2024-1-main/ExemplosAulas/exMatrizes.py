#matriz(tabela) ou (lista de listas)
    #0  #1  #3  #4 ---->colulas
M=[[12, 11, 10, 9], #0->linha
   [8,  7,  6,  5], #1
   [4,  3,  2,  1]] #2

#ou
#M=[[12,11,10,9],[8,7,6,5],[4,3,2,1]]

print(M)
print(len(M))    #-->n de linhas(n de arrays)
print(len(M[0])) #-->n de colunas(n de elementos)

#acesso #relembrar os pares ordenados (x,y)
print(M[0][0]) #sempre usando os indices(M[Linha][coluna])
print(M[2][1])

#varredura #L=linha #C=coluna
for L in range(len(M)):
    for C in range(len(M[0])):
        print(M[L][C], end="\t")
    print()