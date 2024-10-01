#lista 04 while e for

#6 -Crie um algoritmo que sorteie 5 valores entre 0 e 100 e depois imprima o menor, o maior e a média
#dos valores sorteados.
import random
def oGrandeSorteio():
    valoresSorteio= []

    for i in range(0,5):
        valor=random.randint(0,100)
        valoresSorteio.append(valor)

    maior=max(valoresSorteio)
    menor=min(valoresSorteio)
    soma=sum(valoresSorteio)
    media=soma/5

    print(maior,'é o maior número sorteado')
    print(menor,'é o menor número sorteado')
    print(soma,'é a soma entre os números sorteados')
    print(media,'é a média entre os números sorteados')

#executar
oGrandeSorteio()
#exercicio refeito usando funções