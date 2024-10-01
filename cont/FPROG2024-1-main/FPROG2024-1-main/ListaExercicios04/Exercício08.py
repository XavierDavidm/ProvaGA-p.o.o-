#lista 04 while e for

#8 -Fazer um programa que calcule e imprima o fatorial de um número fornecido pelo usuário. Repetir a
#execução do programa tantas até o usuário responder não. O fatorial de um número inteiro positivo é
#definido como o número multiplicado por ele menos 1, menos 2, etc até o valor 1.
#Por exemplo, o fatorial de 4 é 4x3x2x1=24

#funçao factorial
def factorial():
    cont=1+int(input('digite um número inteiro para saber seu factorial: '))
    fact=1
    contI=cont-1
    while cont !=1:
        cont=cont-1
        fact=cont*fact
    print('o factorial de',contI,'é',fact)

#main
continuar=True
while continuar != False:
    factorial()
    resposta=0
    while resposta !='s' and resposta !='n':
        resposta=input('digite se deseja continuar ou fechar o programa usando (s/n): ')
        if resposta !='s' and resposta !='n':
            print('ERRO! por favor utilize somente s ou n para responder se deseja continuar')
            resposta=0
        elif resposta == 'n':
            continuar=False
            print('Encerrando programa.....')
        else:
            continuar=True