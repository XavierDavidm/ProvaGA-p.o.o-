#Lista 05 Funções

#5 -Utilizando o template de menus mostrado em aula, faça um programa que simule uma calculadora
#simples, mostrando ao usuário as opções
#somar,
#subtrair,
#multiplicar e
#dividir dois números reais. Cada
#uma das operações deve ser executada em funções que recebam como parâmetro os dois números,
#lidos do usuário. As funções devem retornar o resultado para o programa principal, que o exibirá na
#tela. OBS.: Apenas chame a função de dividir se o divisor for diferente de zero (divisão por zero não
#existe!).

#funções
def somar(n1,n2):
    resposta=n1+n2
    return resposta

def subtrair(n1,n2):
    resposta=n1-n2
    return resposta

def multiplicar(n1,n2):
    resposta=n1*n2
    return resposta

def dividir(n1,n2):
    resposta=n1/n2
    return resposta

#main
encerrar=False
print('bem vindo a calculadora, escolha abaixo a operação entre dois números que deseja realizar')
while encerrar!=True:
    print('1 - somar')
    print('2 - subtrair')
    print('2 - multiplicar')
    print('3 - dividir')
    print('0 - encerrar programa')
    tarefa=int(input('por favor digite o número da opção que desejar executar: '))
    if tarefa==1:
        n1=float(input('digite o número que deseja somar: '))
        n2=float(input('digite o outro número que deseja somar: '))
        resposta=somar(n1,n2)
        print('a soma de',n1,'e',n2,'é',resposta)
        encerrar=False

    elif tarefa==2:
        n1=float(input('digite o número que deseja subtrair: '))
        n2=float(input('digite o outro número que deseja subtrair: '))
        resposta=subtrair(n1,n2)
        print('a subtração de',n1,'e',n2,'é',resposta)
        encerrar=False

    elif tarefa==3:
        n1=float(input('digite o número que deseja multiplicar: '))
        n2=float(input('digite o outro número que deseja multiplicar: '))
        resposta=multiplicar(n1,n2)
        print('a multiplicação de',n1,'e',n2,'é',resposta)
        encerrar=False

    elif tarefa==4:
        divisor=0
        while divisor==0:
            n1=float(input('digite o número que deseja dividir: '))
            n2=float(input('digite o outro número que será o divisor: '))
            if n2 ==0:
                print('ERRO! é impossível dividir qualquer número por 0, escolha outro número para ser o divisor.')
                divisor=0
            else:
                resposta=dividir(n1,n2)
                divisor=1
        print('a divisão de',n1,'e',n2,'é',resposta)
        encerrar=False

    elif tarefa==0:
        print('Encerrando o Programa.....')
        encerrar=True

    else:
        print('ERRO! por favor digite o número válido correspondente a uma das operações listadas no menu.')
        encerrar=False