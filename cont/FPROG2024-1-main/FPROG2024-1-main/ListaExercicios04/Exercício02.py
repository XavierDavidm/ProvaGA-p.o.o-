#lista 04 while e for

#2- Implemente um programa que sorteia um número de 1 a 10 e dá ao usuário 3 tentativas de acertá-lo.
#A cada tentativa errada, o programa informa se o número a adivinhar está abaixo ou acima.

import random
sorteio=random.randint(1,10)
tentativas=0
acerto=False
while acerto!=True:
    while tentativas <3 and acerto!=True:
        resposta=int(input('o computador fez um sorteio de um número de 1 a 10, qual número você acha que é? '))
        if resposta==sorteio:
            print('Você Acertou')
            acerto=True
        else:
            print('Resposta Errada!')
            tentativas=tentativas+1
            acerto=False
            if resposta < sorteio:
                print('dica: o número do sorteio é maior que a sua resposta!')
            else:
                print('dica: o número do sorteio é menor que a sua resposta!')