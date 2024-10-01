#2.Faça a multiplicação de todos os elementos da matriz acima por 7.
v1=[1,5,9,2,5]
v2=[7,4,13,21,6] 
v3=[8,-3,5,7,12]
M=[]
M.append(v1)
M.append(v2)
M.append(v3)
print(M)

#lendo e multiplicando x7
for x in range(len(M)):
    for y in range(len(M[0])):
        print(M[x][y]*7, end='\t') #multiplicação por 7
    print()