#3. Faça um programa para testar se um dado é viciado. Faça o lançamento N vezes (N é um número
#lido pelo usuário, pode ser um número bem grande), armazene cada valor que for sorteado em um
#array com 6 posições e ao final imprima o percentual do resultado de cada face.

import random

N=int(input('digite o número de vezes que deseja lançar o dado: '))
V=[]
V1=[]
V2=[]
V3=[]
V4=[]
V5=[]
V6=[]

for dado in range(N):
    dado=random.randint(1,6)
    if dado==1:
        V1.append(dado)
    elif dado==2:
        V2.append(dado)
    elif dado==3:
        V3.append(dado)
    elif dado==4:
        V4.append(dado)
    elif dado==5:
        V5.append(dado)
    elif dado==6:
        V6.append(dado)
V.append(V1)
V.append(V2)
V.append(V3)
V.append(V4)
V.append(V5)
V.append(V6)
#tamanho T usado para medir o numero de vezes que um valor aparece
T1=len(V1)
T2=len(V2)
T3=len(V3)
T4=len(V4)
T5=len(V5)
T6=len(V6)
#percentual P e Resultado R
def Percetual(T,N):
    P=T/N
    R=round(P*100)
    return R

R=Percetual(T1,N)
print('o total de repetiçoes do valor 1 é',T1,'ou seja',R,'%','de',N)
R=Percetual(T2,N)
print('o total de repetiçoes do valor 2 é',T2,'ou seja',R,'%','de',N)
R=Percetual(T3,N)
print('o total de repetiçoes do valor 3 é',T3,'ou seja',R,'%','de',N)
R=Percetual(T4,N)
print('o total de repetiçoes do valor 4 é',T4,'ou seja',R,'%','de',N)
R=Percetual(T5,N)
print('o total de repetiçoes do valor 5 é',T5,'ou seja',R,'%','de',N)
R=Percetual(T6,N)
print('o total de repetiçoes do valor 6 é',T6,'ou seja',R,'%','de',N)