import csv
arquivo = open('pessoas.csv') #abre ou cria o arquivo com nome em ('nome')
reader=csv.reader(arquivo) #le o arquivo
data=list(reader) #coloca o conteudo numa variavel
print(data)


for x in range(len(data)):
    for y in range(len(data[0])):
        print(data[x],[y],end='\t')
    print()


#para imprimir apenas uma coluna
for x in range(len(data)):
    print(data[x][0]) #o zero pode ser substituido por qualquer coluna desejada

#para o trabalho quando for filtrar datas
for x in range(len(data)):
    
    ano = data[x][3] #no lugar do 3 é o indice da coluna de datas
    if ano >=1990 and ano <=2000: #os anos devem ser uma variavel de input para o user escolher o ano do filtro
        print(data[x][0])


















