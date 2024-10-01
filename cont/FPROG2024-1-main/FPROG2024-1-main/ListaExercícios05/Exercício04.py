#Lista 05 Funções

#4 -Implemente uma função sorteio que receba o intervalo de valores inteiros início e fim como parâmetro
#e sorteie um número dentro do intervalo (considerando intervalo fechado [início, fim])

#import
import random

#função
def sorteioIntervalos(inicio,fim):
    sorteio=random.randint(inicio,fim)
    return sorteio

#main
inicio=int(input('digite o valor inicial do intervalo para o sorteio: '))
fim=int(input('digite o valor final do intervalo para o sorteio: '))
número=sorteioIntervalos(inicio,fim)
print('o número que sorteado dentro do intervalo de (',inicio,'até',fim,') é',número)