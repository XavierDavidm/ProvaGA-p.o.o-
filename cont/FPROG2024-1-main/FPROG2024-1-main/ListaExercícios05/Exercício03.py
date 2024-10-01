#Lista 05 Funções

#3 -Implemente uma função mediaUnisinos que receba como parâmetro as notas do Grau A e do Grau B e
#retorne o resultado do grau final.

#funções
def mediaUni(grauA,grauB):
    grauF=(grauA+ 2*grauB)/3.0
    return grauF

def validação(nota):
    if nota < 0 or nota > 10:
        print('ERRO! digite uma nota válida entre o e 10')
        valido=False
    else:
        valido=True
    return valido
    

#main + validação
valido=False
while valido!=True:
    grauA=float(input('digite sua nota do Grau A: '))
    valido=validação(grauA)

valido=False
while valido!=True:
    grauB=float(input('digite sua nota do Grau B: '))
    valido=validação(grauB)

grauF=mediaUni(grauA,grauB)
print('sua média é',grauF)