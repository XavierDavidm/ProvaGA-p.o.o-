#resposta=1
#while resposta != 'S' and resposta != 'N':
#    resposta=input('responda sim(S) ou não(N)')
#    if resposta == 'S':
#        print('voce respodendeu sim')
#    elif resposta == 'N':
#        print('você respondeu não')
#    else:
#        print('resposta invalida')

#enquanto o user não digitar S ou N o programa repete a pergunta usando a condição while
   
#contador com while: escrever o nome 10 vezes
#nome=input('digite seu nome: ')
#variavel para contar quantidade de vezes que o nome foi escrito 
#cont=0
#while cont<10:
#    print(nome)
#    cont=cont+1 #incremento em 1 unidade

#Faça um programa que permita o usuário
#entrar com uma senha no máximo em 3
#tentativas
#– Quais são as condições para a repetição?
#• Quando a repetição deve parar?
#senhaCadastrada=123
#senha=-10
#tentativas=0
#while senhaCadastrada != senha and tentativas <=3:
#    senha=int(input('digite sua senha: '))
#    if senhaCadastrada == senha:
#        print('olá sua senha esta correta!')
#    elif tentativas >=2:
#        print('você digitou a senha incorreta 3 vezes, aguarde 1h para tentar novamente')
#        tentativas=4
#    else:
#        print('senha invalida tente novamente!')
#        tentativas = tentativas + 1

# modelo simples sem print da quantidade de tentativas restantes


#comando for (VARIAVEL) in range(start,stop,step)
#counter=0
#for counter in range(0,10,1):
#    print(counter)

#SIMULAÇÃO CORRIDA DE HAMSTERS
import random
hamster1=0
hamster2=0
vencedor=0
while vencedor==0:
    #ham1
    nSort=random.randint(1,5)
    if nSort ==1:
        hamster1=hamster1+1
    elif nSort ==2:
        hamster1=hamster1+2
    elif nSort ==3:
        pass
    elif nSort ==4:
        hamster1=hamster1-1
    else:
        hamster1=hamster1-2
    #limite de 0 e 12
    if hamster1 < 0:
        hamster1=0
    if hamster1 > 12:
        hamster1=12

    #ham2
        nSort=random.randint(1,5)
    if nSort ==1:
        hamster2=hamster2+1
    elif nSort ==2:
        hamster2=hamster2+2
    elif nSort ==3:
        pass
    elif nSort ==4:
        hamster2=hamster2-1
    else:
        hamster2=hamster2-2
    #limite2
    if hamster2 < 0:
        hamster2=0
    if hamster2 > 12:
        hamster2=12
    
    #ganhador
    if hamster1==12:
        vencedor=1
    if hamster2==12:
        if vencedor==0:
            vencedor=2
        else: 
            vencedor=3

    print('hamster1: ')
    for n in range(hamster1):
        print('* ',end = '')
    print()
    print('hamster2: ')
    for n in range(hamster2):
        print('* ',end = '')
    print()
    print('--------------------')
    if vencedor==1:
        print('o hamster 1 venceu')
    elif vencedor==2:
        print('o hamster 2 venceu')
    else:
        print('empate ambos chegaram ao mesmo tempo')
    

























