#lista 04 while e for

#9 -Escrever um programa que produza a saída abaixo na tela, para n linhas e usando um caractere lido do
#teclado.

carac=input('digite o caracter que deseja (ex: * ): ')
n=int(input('digite o número de linhas que se deve repetir o caracter: '))
for i in range(1,n+1):
    print(carac*i)