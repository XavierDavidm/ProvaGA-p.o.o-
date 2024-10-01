#lista 04 while e for

#3- Elabore um programa que lê um número de 1 a 9 e mostra a tabuada de multiplicação do número.
def tabuada(n):
    for i in range(1,11):
        res=n*i
        print(n,'x',i,'=',res)

continuar=True

while continuar!=False:
    escolhaT=int(input('digite o número da tabuada que deseja: '))
    print('exibindo a tabuada do número',escolhaT,'...')
    tabuada(escolhaT)
    repetir=0
    while repetir !='s' and repetir !='n':
        repetir=input('Calcular outro número (s/n)?')
        if repetir=='s':
            continuar=True
        elif repetir=='n':
            continuar=False
            print('encerrando programa...')
        else:
            print('Erro! por favor digite s ou n')
            repetir=0