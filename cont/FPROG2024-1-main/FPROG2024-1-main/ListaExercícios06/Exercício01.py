#1. Criar um vetor de 10 números v e inicialize-o sorteando valores de 10 a 90 para cada elemento.
#Depois disso, implemente algoritmos para:
#a. Imprimir o vetor
#b. Verificar se existe o valor 50 neste vetor (apenas dizer se encontrou ou não)
#c. Verificar o número de ocorrências do valor 50 neste vetor.
#d. Calcular a média dos valores do vetor
#e. Encontrar o maior e o menor valor dos elementos do vetor.
#f. Imprimir a soma e o produto acumulado dos valores dos elementos do vetor
#g. Imprimir o vetor em ordem inversa
#h. Copiar os elementos em ordem inversa para outro vetor.
#i. Crie outros dois vetores com 10 elementos, vPares e vImpares. Copie para vPares todos os
#elementos pares e para vImpares todos os elementos ímpares. Depois disso, imprima o
#conteúdo de vPares e vImpares.

#gerador de array aleatório com 10 elementos 
import random
V=[]
for i in range(10):
    n=random.randint(10,90)
    V.append(n)

#a)
print(V)

#b)
cont50=0
verificar50=False
for i in V:
    if i==50:
        verificar50=True
        cont50=cont50+1
if verificar50==True:
    print('o array V contém o número 50')
else:
    print('o array V não contém o número 50')

#c)
print('o número de ocorrencias do valor 50 é de',cont50)

#d)
mediaV=sum(V)/10
print('a média do array V é de',mediaV)

#e)
print('o maior valor do array V é',max(V))
print('o menor valor do array V é',min(V))

#f)
#tive problemas com o produto já que são 10 elementos o programa estava se perdendo na contagem
#então importei a biblioteca decimal
from decimal import Decimal
produtoV= Decimal(1)
for elemento in V:
    produtoV *= Decimal(elemento)
    #print(produtoV) #passo a passo da multiplicação
print('a soma do array V é',sum(V))
print('o produto do array V é',produtoV)

#g) e #h)
Vinvertido=V[::-1]
print('o inverso do array V é',Vinvertido)

#i)
vPar=[]
vImpar=[]
for elemento in V:
    if elemento%2==0:
        vPar.append(elemento)
    else:
        vImpar.append(elemento)
print('os elementos pares contidos no array V são:',vPar)
print('os elementos impares contidos no array V são:',vImpar)