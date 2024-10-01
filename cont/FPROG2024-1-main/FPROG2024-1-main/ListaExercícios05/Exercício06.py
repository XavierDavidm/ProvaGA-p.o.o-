#Lista 05 Funções

#6 -Utilizando o template de menus mostrado em aula, faça um programa que simule um sistema de lootbox
#simples. As opções para o usuário são
#abrir uma caixa e
#consultar itens coletados. Ao abrir uma caixa, o
#usuário irá receber 1 item comum, raro ou lendário, conforme a probabilidade da tabela abaixo:
#Tipo de item Probabilidade de obtenção
#Comum 80 %
#Raro 19%
#Lendário 1%
#Ao obter o item, deverá se atualizar o inventário do jogador contabilizando o número de itens comuns,
#raros e lendários que ele possui. Ao consultar os itens coletados, deverá ser mostrado ao usuário a
#quantidade de itens de cada tipo que ele possui.
#Exemplos de tela:
#1 – Abrir uma caixa
#2 – Consultar itens
#0 - Sair
#Escolha uma opção: 1
#Você coletou 1 item comum!
#1 – Abrir uma caixa
#2 – Consultar itens
#0 - Sair
#Escolha uma opção: 2
#Itens comuns: 9
#Itens raros: 2
#Itens lendários: 0

#import
import random

#funções

def abrirCaixa(contComum,contRaro,contLendario):
    itemSort=random.randint(1,101)
    if itemSort <= 1:
        contLendario=contLendario+1
        print('você coletou um item lendário')
    elif itemSort <=19 and itemSort >1:
        contRaro=contRaro+1
        print('você coletou um item Raro')
    else:
        contComum=contComum+1
        print('você coletou um item comum')
    return contComum,contRaro,contLendario

def inventario(contComum,contRaro,contLendario):
    print('#Itens comuns:',contComum)
    print('#Itens comuns:',contRaro)
    print('#Itens comuns:',contLendario)

#main
contComum=0
contRaro=0
contLendario=0
encerrar=False
print('jogo rpg loot')
print('')
while encerrar!=True:
    print('MENU de ações:')
    print('')
    print('1 - abrir uma caixa')
    print('2 - consultar inventário')
    print('0 - sair do jogo')
    print('')
    tarefa=float(input('digite o número da ação que seja realizar do menu: '))
    if tarefa==1:
        contComum,contRaro,contLendario=abrirCaixa(contComum,contRaro,contLendario)
        encerrar=False

    elif tarefa==2:
        inventario(contComum,contRaro,contLendario)
        encerrar=False

    elif tarefa==0:
        print('encerrando jogo.....')
        encerrar=True
    else:
        print('ERRO! comando não reconhecido, use uma das opções do menu.')
        encerrar=False














