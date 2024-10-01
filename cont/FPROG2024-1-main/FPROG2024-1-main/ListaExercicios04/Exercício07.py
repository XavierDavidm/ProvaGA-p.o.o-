#lista 04 while e for

#7 -Descubra, dentre cinco nomes informados pelo usuário, qual o primeiro em ordem alfabética.
def ordenarNomes():
    listaNomes=[]

    for nome in range(0,5):
        nome=input('digite um Nome: ')
        listaNomes.append(nome)

    primeiro=min(listaNomes)
    print('dentre os nomes escolhidos',primeiro,'é o primeiro nome em ordem alfabética')

#executar
ordenarNomes()