#lista 04 while e for

#.1 Faça um algoritmo para:
#a. Gerar e escrever todos os números inteiros do intervalo [0,100].
#b. Gerar e escrever os números pares do intervalo [20,50].
#c. Gerar e escrever os números inteiros do intervalo [25,70] em ordem decrescente.
#d. Gerar e escrever os números ímpares do intervalo [25,95] em ordem decrescente.
#e. Ler 15 números e escrever a soma e a média dos números lidos.
#f. Ler 10 números inteiros e escrever a quantidade de números pares e a quantidade de números
#ímpares lidos.
#g. Sortear 20 números inteiros entre -10 e 10 e imprimi-los acompanhados da mensagem
#“POSITIVO”, “NEGATIVO”, ou “NULO”, conforme o caso. No final, imprimir a quantidade de
#números positivos e negativos lidos.
#h. Ler n números e imprimir no final a soma dos números lidos (obs.: n é a quantidade de números
#que deverão ser lidos e também deve ser lido do teclado)

#1a)
for A in range(0,101):
    print(A)
print('#####')

#1B)
for B in range(20,51,2):
    print(B)
print('#####')

#1C)
for C in range(70,24,-1):
    print(C)
print('#####')

#1D)
for D in range(95,24,-2):
    print(D)
print('#####')

#1E)
numR=0
numS=0
cont=0

while cont<15:
    numR=float(input('digite um número: '))
    cont=cont+1
    print(cont,')',numR)
    numS=numS+numR
    numM=numS/15
print('a soma dos quinze números acima é',numS)
print('a média dos quinze números acima é',numM)

#1F) 
cont=0
numR=0
contP=0
contN=0

while cont<10:
    numR=int(input('digite um número inteiro: '))
    cont=cont+1
    print(cont,')',numR)
    if numR%2:
        contP=contP+1
    else:
        contN=contN+1
print('entre os 10 números digitados acima',contP,'são pares e',contN,'são ímpares')

#1G)
import random
nSort=0
num=0
contPOS=0
contNE=0
contNUL=0
while nSort<20:
    num=random.randint(-10,10)
    if num < 0:
        print(num,'é negativo')
        contNE=contNE+1
    elif num == 0:
        print(num,'é nulo')
        contNUL=contNUL+1
    else:
        print(num,'é positivo')
        contPOS=contPOS+1
    nSort=nSort+1
print('entre os 20 números sorteados',contPOS,'são positivos',',',contNE,'são negativos e',contNUL,'são nulos')

#1H)
num=0
numR=0
nLido=0
numS=0
n=int(input('informe quantos números devem ser lidos: '))
print(n,'números serão lidos abaixo')
while nLido<n:
    numR=float(input('digite um número: '))
    nLido=nLido+1
    print(nLido,')',numR)
    numS=numS+numR
print('a soma de todos os',n,'números é',numS)