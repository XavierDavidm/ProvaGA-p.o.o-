#exemplos arrays/vetor
#bibliotecas array, numpy, list para python
#1- criando array simples de 10

#array A
A=[1,2,3,4,5,6,7,8,9,10]

#descobrir tamanho
tamanho = len(A) #ou print(len(A)) #usar variavel se fosse nescessario guardar o tamanho
#print pode chamar direto valores e funções que já retornam valor
print('o tamanho do array é de',tamanho)

#somente em python podemos exibir tudo dentro do array só printando ele
print(A)

#acessando elementos dentro do array

#primeiro
primeiro=A[0] #zero é sempre o primeiro elemento(indice/index 0)

#ultimo
ultimo=A[tamanho-1]

#5
quinto=A[5-1]

print(primeiro)
print(ultimo)
print(quinto)

#ou print direto-> print(A[0])

#2
pos=5 #variavel que deseja a quinta posiçao do vertor indice 4

print('elemento na posiçao',pos,'do array',A[pos-1])

#SEMPRE USAR [N-1] PARA NÃO CONFUNDIR POSIÇÃO COM INDICE 
#INDICE SEMPRE COMEÇA EM 0, O TERCEIRO NÚMERO NA LISTA É INDICE 2
#A[3-1] TRARÁ O TERCEIRO DADO DA LISTA

#PARA O PYTHON# não tem isso em algumas outras linguagens
#inicializações alternativas

B=['b']*5 # é a mesma coisa que B=['b','b','b','b','b']

print(B)

C=list(range(5,20,3)) #sequencia começando em 5 até 20 de 3 em 3 números
print(C)

#varredura/percorrer
#lista todos os elementos dentro array em varias linhas
E=list(range(1,6)) #gerando um array com range

#funçao de varredura com for(python)
for i in E: #colocar o array
    print('valor:',i)

#varredura universal usando os indices para ler o array
#percorrer o array acessando os elementos apartir do indice
F=list(range(1,6))
for i in range(len(F)):
    print('F[{}] = {}'.format(i, A[i])) #format é pra ficar bonito em python o print


