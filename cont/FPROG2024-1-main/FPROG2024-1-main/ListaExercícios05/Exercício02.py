#Lista 05 Funções

#2 -Implemente uma função tabuada que receba como parâmetro um número inteiro e escreva a tabuada
#desse número.

#Função
def tabuada(n):
    for i in range(1,11):
        res=n*i
        print(n,'x',i,'=',res)      

#main
n=int(input('digite um número inteiro para descobrir sua tabuada até 10: '))
tabuada(n)