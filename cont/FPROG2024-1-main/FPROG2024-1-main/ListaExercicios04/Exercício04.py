#lista 04 while e for

#4 -Escrever um programa que calcule todos os números divisíveis por certo valor indicado pelo usuário (o
#resto da divisão por este número deve ser igual a zero), compreendidos em um intervalo também
#especificado pelo usuário. O usuário deve entrar com um primeiro valor correspondente ao divisor e
#após ele vai fornecer o valor inicial do intervalo, seguido do valor final deste intervalo.

divisor=int(input('digite o número divisor: '))
a=int(input('digite o número de inicio do intervalo: '))
b=int(input('digite o número de final do intervalo: '))
print('calculando todos os números divisíveis por',divisor,'dentro do intervalo de',a,'até',b,'...')
for divido in range(a,b+1):
    if divido%divisor==0:
        print(divido,'é divisível por',divisor)