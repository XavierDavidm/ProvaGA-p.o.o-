#.1-Escreva um programa que leia dois números e efetue uma divisão, mas somente se o divisor for
#diferente de zero; quando isto ocorrer, é mostrada uma mensagem de erro apropriada.
numero1=float(input('digite um numero: '))
numero2=float(input('digite um numero: '))
if numero2 != 0:
    total=numero1/numero2
    print(total)
else: 
    print('erro! o numero 0 não é valido para divisão')

#.2- Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que A
#+ C.
A=float(input('digite o valor de A: '))
B=float(input('digite o valor de B: '))
C=float(input('digite o valor de C: '))
if A+B<A+C:
    print('A+B é menor que A+C')
else:
    print('A+B é maior que A+C')

#.3- Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo
#o resultado
numero=float(input('digite um numero positivo ou negativo: '))
if numero >0:
    final=numero*2
    print('o dobro de',numero,'é',final)
else:
    final=numero*3
    print('o triplo de',numero,'é',final)

#.4- Crie um programa que verifica se um número inteiro informado pelo usuário é divisível por 3.
numerodivisivel=int(input('informe um numero para verificar se é divisivel por 3: '))
if numerodivisivel%3==0:
    print(numerodivisivel,'é divisivel por 3')
else:
    print(numerodivisivel,'não é divisivel por 3')

#.5- Faça um algoritmo para receber um número qualquer do usuário e informar na tela se é par ou se
#é ímpar
num=int(input('digite um numero par ou impar: '))
if num%2==0:
    print(num,'é par')
else:
    print(num,'é impar')

#.6- Brincadeira do PAR ou ÍMPAR. Pergunte para o usuário se ele aposta em PAR ou ÍMPAR. Depois
#disso, peça para ele digitar um número de 0 a 5 (como se fosse mostrar os dedos da mão. Sorteie
#um número de 0 a 5 e some com o que o usuário digitou. Se o usuário escolheu PAR e o valor da
#soma for par OU se ele escolheu ÍMPAR e o valor da soma é ímpar, diga que ele venceu. Senão, diga
#que o programa venceu
import random
aposta=int(input('você, aposta em 0 ou 1: '))
numDoUser=int(input('digite um numero de 0 a 5: '))
sorteio=random.randint(0,5)
print('o computador jogou',sorteio)
print('você jogou',numDoUser)
resultadoDaAposta=sorteio+numDoUser
if resultadoDaAposta%aposta==0:
    print('você ganhou')
else:
    print('você perdeu')

#.7- Implementar um programa que calcula o desconto previdenciário de um funcionário. O programa
#deve, dado um salário retornar o valor do desconto proporcional ao mesmo. O cálculo de desconto
#segue a regra: o desconto deve 11% do valor do salário. Entretanto, o valor máximo de desconto é
#318,20. Sendo assim, ou o método retorna 11% sobre o salário ou 318,20.
salario=float(input('informe seu salário: '))
taxaDeDesconto= 0.11
salDesc=salario*taxaDeDesconto
if salDesc > 318.20:
    descontoPrevidencia=318.20
else:
    descontoPrevidencia=salDesc
print('para um salario de',salario,'reais é aplicado',descontoPrevidencia,'reais para o desconto previdenciário')

#.8- Um comerciante comprou um produto e quer vendê-lo com lucros diferentes dependendo do valor
#da compra. Ele quer um lucro de 45% se o valor da compra for menor que R$ 20,00, 35% se o preço
#for de até 50 reais e lucro de 25% se valor for maior. Entrar com o valor do produto e imprimir na
#tela o valor de venda.
produto=float(input('digite o valor do produto que deseja vender: '))
if produto < 20.00:
    taxaLucro=produto*0.45
elif produto <= 50:
    taxaLucro=produto*0.35
else:
    taxaLucro=produto*0.25
precofinal=produto+taxaLucro
print('o produto deve ser vendido por',precofinal,'reais')

#.9-Faça um conversor de câmbio de reais/dólar/euro. O usuário deve informar inicialmente a cotação
#de cada moeda em relação ao real. Depois apresente o seguinte menu:
#1) Converter de Real para Euro
#2) Converter de Real para Dólar
#3) Converter de Euro para Dólar
#4) Converter de Euro para Real
#5) Converter de Dólar para Euro
#6) Converter de Dólar para Real
#Leia o valor a ser convertido na moeda de origem e imprima na tela a quantidade na moeda
#destino.
dolar=float(input('informe a cotação atual do dolar para real: '))
euro=float(input('informe a cotação atual do euro para real: '))
print('1) Converter de Real para Euro')
print('2) Converter de Real para Dólar')
print('3) Converter de Euro para Dólar')
print('4) Converter de Euro para Real')
print('5) Converter de Dólar para Euro')
print('6) Converter de Dólar para Real')
conversaoEscolhida=0
while conversaoEscolhida !=1 and conversaoEscolhida !=2 and conversaoEscolhida !=3 and conversaoEscolhida !=4 and conversaoEscolhida !=5 and conversaoEscolhida !=6:
    conversaoEscolhida=int(input('digite o número da conversão que deseja realizar: '))
    quantidadeMoeda=float(input('digite a quantidade da moeda origem que deseja converter: '))
    CRE=quantidadeMoeda/euro
    CRD=quantidadeMoeda/dolar
    CED=(quantidadeMoeda*euro)/dolar
    CER=quantidadeMoeda/euro
    CDE=(quantidadeMoeda*dolar)/euro
    CDR=quantidadeMoeda*dolar
    if conversaoEscolhida==1:
        print(quantidadeMoeda,'Reais são',CRE,'Euros')
    elif conversaoEscolhida==2:
        print(quantidadeMoeda,'Reais são',CRD,'Dólares')
    elif conversaoEscolhida==3:
        print(quantidadeMoeda,'Euros são',CED,'Dólares')
    elif conversaoEscolhida==4:
        print(quantidadeMoeda,'Euros são',CER,'Reais')
    elif conversaoEscolhida==5:
        print(quantidadeMoeda,'Dólares são',CDE,'Euros')
    elif conversaoEscolhida==6:
        print(quantidadeMoeda,'Dólares são',CDR,'Reais')
    else:
        print('o numero da conversão escolhida não é valido, digite um dos numeros da tabela')

#.10- Dados não precisam ser tão “quadrados”, ou cúbicos para ser mais exato. Faça um programa que
#simule dados de 4, 6, 8, 10, 12 ou 16 faces (apenas estes valores). Peça para o usuário informar no
#começo do programa quantas faces quer, para depois fazer o sorteio.
import random
d2=random.randint(1,2)
d4=random.randint(1,4)
d6=random.randint(1,6)
d8=random.randint(1,8)
d12=random.randint(1,12)
d16=random.randint(1,16)
dadoescolhido=0
while dadoescolhido!=2 and dadoescolhido!=4 and dadoescolhido!=6 and dadoescolhido!=8 and dadoescolhido!=12 and dadoescolhido!=16:
    dadoescolhido=int(input('qual escolha o dado que deseja simular,(2,4,6,8,12 ou 16 lados): '))
    if dadoescolhido == 2:
        print('você jogou um Dado de 2 lados e o resultado foi',d2)
    elif dadoescolhido == 4:
        print('você jogou um Dado de 4 lados e o resultado foi',d4)
    elif dadoescolhido == 6:
        print('você jogou um Dado de 6 lados e o resultado foi',d6)
    elif dadoescolhido == 8:
        print('você jogou um Dado de 8 lados e o resultado foi',d8)
    elif dadoescolhido == 12:
        print('você jogou um Dado de 12 lados e o resultado foi',d12)
    elif dadoescolhido == 16:
        print('você jogou um Dado de 16 lados e o resultado foi',d16)
    else:
        print('O dado escolhido não é valido! por favor escolha outro dado listado')

#.11- Crie um programa para informar quais e quantas notas são necessárias para entregar o mínimo de
#cédulas para um determinado valor informado pelo usuário considerando notas de R$ 100, R$ 50,
#R$ 20, R$ 10 e R$ 5 e R$ 1. Seu programa deve mostrar apenas as notas utilizadas. Por exemplo, ao
#solicitar R$18, o programa deve informar apenas a seguinte informação (note que não foram
#exibidas informações sobre as demais cédulas):
#1 nota(s) de R$ 10.
#1 nota(s) de R$ 5.
#3 nota(s) de R$ 1.
totalNotasUser=int(input('informe a quantia que deseja trasformar em cédulas: '))
notas100=0
notas50=0
notas20=0
notas10=0
notas5=0
notas1=0
while totalNotasUser>=100:
    totalNotasUser=totalNotasUser-100
    notas100=notas100+1
while totalNotasUser>=50:
    totalNotasUser=totalNotasUser-50
    notas50=notas50+1
while totalNotasUser>=20:
    totalNotasUser=totalNotasUser-20
    notas20=notas20+1
while totalNotasUser>=10:
    totalNotasUser=totalNotasUser-10
    notas10=notas10+1
while totalNotasUser>=5:
    totalNotasUser=totalNotasUser-5
    notas5=notas5+1
while totalNotasUser>=1:
    totalNotasUser=totalNotasUser-1
    notas1=notas1+1
if notas100 > 0:
    print(notas100,'nota(s) de R$ 100')
if notas50 > 0:
    print(notas50,'nota(s) de R$ 50')
if notas20 > 0:
    print(notas20,'nota(s) de R$ 20')
if notas10 > 0:
    print(notas10,'nota(s) de R$ 10')
if notas5 > 0:
    print(notas5,'nota(s) de R$ 5')
if notas1 > 0:
    print(notas1,'nota(s) de R$ 1')
if notas1==0 and notas5==0 and notas10==0 and notas20==0 and notas50==0 and notas100==0:
    print('você não digitou um valor valido para converter em cédulas')

#.12- A confederação brasileira de natação irá promover eliminatórias para o próximo mundial. Fazer um
#algoritmo que receba a idade de um nadador e imprima a sua categoria segundo a tabela a seguir:

idade=0
while idade <=0:
    idade=int(input('digite sua idade para saber sua categoria: '))
    if idade >= 5 and idade <=7:
        print('você faz parte da categoria Infantil A')
    elif idade >= 8 and idade <=10:
        print('você faz parte da categoria Infantil B')
    elif idade >= 11 and idade <=13:
        print('você faz parte da categoria Juvenil A')
    elif idade >= 14 and idade <=17:
        print('você faz parte da categoria Juvenil B')
    elif idade >= 18:
        print('você faz parte da categoria Senior')
    elif idade <=0:
        print('idade invalida por favor, digite sua idade corretamente')
    elif idade <=5:
        print('sua idade é baixa demais para entrar em uma categoria')

#.13- Faça um programa que leia a nota do Grau A e do Grau B do aluno e calcule a média final conforme
#as regras da Unisinos. Imprima a média final na tela e diga se o aluno passou por média ou se ficou
#em recuperação (grau C). Se o aluno ficou em recuperação, pergunte se ele quer substituir o Grau
#A ou o Grau B (ele deve digitar ‘a’ ou ‘b’). Leia a nota do Grau C, recalcule a média de acordo com o
#grau substituído e imprima na tela o resultado, informando se ele foi aprovado ou reprovado.
notaGA=-1
notaGB=-1
while notaGA < 0 or notaGB <0 or notaGA > 10 or notaGB > 10:
    notaGA=float(input('digite sua nota do grau A: '))
    notaGB=float(input('digite sua nota do grau B: '))
    mediaF=round(notaGA*1/3 + notaGB*2/3)
    if notaGA < 0 or notaGB < 0 or notaGA > 10 or notaGB > 10:
        print('nota invalida!, por favor informe uma nota de 0 a 10')
    elif mediaF >=6:
        print('sua média final foi',mediaF)
        print('você foi aprovado, parabéns!')
    else:
        print('sua média final foi',mediaF)
        print('Você não foi aprovado, deverá realizar a recuperação(grau C)')
        notaGC=-1
        while notaGC < 0 or notaGC >10:
            notaGC=float(input('digite sua nota do grau C (recuperação): '))
            if notaGC < 0 or notaGC >10:
                print('nota invalida!, por favor informe uma nota de 0 a 10')
            else:
                escolharec=1
                while escolharec !='a' and escolharec !='b':
                    escolharec=input('escolha qual grau deseja substuir (a) ou (b): ')
                    if escolharec !='a' and escolharec!='b':
                        escolharec=1
                        print('por favor escolha qual grau será substituido (a) ou (b)')
                    else:
                        if escolharec =='a':
                            mediaF=round(notaGC*1/3 + notaGB*2/3)
                            escolharec='a'
                            if mediaF >= 6:
                                print('você foi aprovado com',mediaF,'média parabéns!')
                            else:
                                print('sua média final foi',mediaF)
                                print('você foi reprovado mesmo com o grau C')
                        elif escolharec =='b':
                            mediaF=round(notaGA*1/3 + notaGC*2/3)
                            escolharec='b'
                            if mediaF >= 6:
                                print('você foi aprovado com',mediaF,'média parabéns!')
                            else:
                                print('sua média final foi',mediaF)
                                print('você foi reprovado mesmo com o grau C')

#.14- Criar um programa para identificar o valor a ser pago por um plano de saúde dada a idade do
#conveniado considerando que todos pagam R$ 300 e mais um adicional (se tiver dependentes)
#conforme a seguinte tabela:
#a) crianças com menos de 10 anos pagam R$100;
#b) dependentes com idade entre 10 e 30 anos pagam R$220;
#c) dependentes com idade entre 31 e 60 anos pagam R$ 395; e
#d) dependentes com mais de 60 anos pagam R$ 480
dependente=0                                          
totalplano=300+dependente
temdependente=-1
while temdependente !='S' and temdependente !='N':
        temdependente=input('você possui dependente(s) (S) ou (N): ')
        if temdependente == 'N':
            totalplano=300
            print('o total do seu plano é',totalplano)
        elif temdependente == 'S':
            idadeDependente=-1
            while idadeDependente < 0:
                totalplano=300+dependente
                idadeDependente=int(input('coloque a idade do dependente: '))  
                if idadeDependente < 0:
                    print('idade inválida, por favor coloque uma idade válida')
                elif idadeDependente <= 10:
                    dependente=100
                    totalplano=300+dependente
                    print('o total a pagar pelo convenio é: ',totalplano)
                elif idadeDependente > 10 and idadeDependente <= 30:
                    dependente=220
                    totalplano=300+dependente
                    print('o total a pagar pelo convenio é: ',totalplano)
                elif idadeDependente >= 31 and idadeDependente <= 60:
                    dependente=395
                    totalplano=300+dependente
                    print('o total a pagar pelo convenio é: ',totalplano)
                elif idadeDependente > 60:
                    dependente=480
                    totalplano=300+dependente
                    print('o total a pagar pelo convenio é: ',totalplano)
                
        else:
            print('resposta inválida, por favor responda se possui ou não dependentes usando (S) ou (N)')

#.15- Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço
#normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir
#para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.
#1 - À vista em dinheiro, recebe 15% de desconto
#2 - À vista no cartão de crédito, recebe 10% de desconto
#3 - Em duas vezes, preço normal de etiqueta sem juros
#4 - Em três vezes, preço normal de etiqueta mais juros de 10%
etiqueta=-1
while etiqueta < 0:
    etiqueta=float(input('digite o valor da etiqueta do produto: '))
    if etiqueta < 0:
        print('valor do produto inválido, por favor registre o valor correto')
formaDePagamento=-1
while formaDePagamento!='dinheiro' and formaDePagamento!='cartão' and formaDePagamento!='cartão2x' and formaDePagamento!='cartão3x':
    print('À vista em dinheiro(15% de desconto)',          '(dinheiro)') 
    print('À vista no cartão de crédito(10% de desconto)', '(cartão)')
    print('Em duas vezes(sem juros)',                      '(cartão2x)')
    print('Em três vezes(juros de 10%)',                   '(cartão3x)')
    formaDePagamento=input('digite a forma de pagamento que deseja (por favor digite a opção entre parenteses): ')
    if formaDePagamento=='dinheiro':
        totalfinalproduto=etiqueta*0.85
        print('você pagou em dinheiro à vista',totalfinalproduto,'reais')
    elif formaDePagamento=='cartão':
        totalfinalproduto=etiqueta*0.90
        print('você pagou no cartão à vista',totalfinalproduto,'reais')
    elif formaDePagamento=='cartão2x':
        totalfinalproduto=etiqueta
        print('você pagou no cartão em duas vezes',totalfinalproduto,'reais')     
    elif formaDePagamento=='cartão3x':
        totalfinalproduto=etiqueta*1.10
        print('você pagou no cartão em tres vezes',totalfinalproduto,'reais')
    else:
        print('forma de pagamento inválida, por favor insira novamente a forma de pagamento que deseja de acordo com a tabela a seguir')

#fim lista de exercícios 03!