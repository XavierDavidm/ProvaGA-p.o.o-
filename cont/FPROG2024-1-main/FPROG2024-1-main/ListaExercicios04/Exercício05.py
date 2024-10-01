#lista 04 while e for

#5 -. Para x alunos da Unisinos, ler as notas do grau A e grau B e calcular a média considerando o sistema
#de notas da Unisinos. Se o aluno estiver aprovado escrever “APROVADO”. Caso contrário, ler o grau C
#e pedir qual o grau que deve ser substituído (A ou B, maiúsculo ou minúsculo), recalcular a média. Se
#estiver aprovado, escrever “APROVADO”, caso contrário escrever “REPROVADO”. No final escrever a
#média geral dos alunos.

#funções
def mediaUni(grauA, grauB):
    media=(grauA+ 2*grauB)/3.0
    return media
def somaGeral(notaF,somageral):
    somageral=notaF+somageral
    return somageral

#variaveis
nAlunos=int(input('digite o número de alunos cujas notas serão avaliadas: '))
aluno=0
grauA=0
grauB=0
notaF=0
grauC=0
media=0
somageral=0
#main#
for aluno in range(1,nAlunos+1):
    grauA=float(input('digite a nota do grau A: '))
    grauB=float(input('digite a nota do grau B: '))
    mediaUni(grauA,grauB)
    notaF=mediaUni(grauA,grauB)
    if notaF >= 6:
        print('a média final do aluno',aluno,'foi',notaF)
        print('o aluno',aluno,'foi Aprovado!')
    elif notaF < 6:
        print('a média final do aluno',aluno,'consderando o grau A e B foi',notaF)
        print('o aluno',aluno,'ainda não foi aprovado!')
        escolhaGrau=0
        grauC=0
        notaValida=False
        while escolhaGrau !='a' and escolhaGrau !='b' or notaValida !=True:
            grauC=float(input('informe a nota do grauC: '))
            escolhaGrau=input('escolha um grau para substituir pelo grauC, (a/b): ')
            if grauC < 0 or grauC >10:
                print('Erro! por favor registre uma nota válida entre 0 a 10')
                notaValida=False
            elif escolhaGrau=='a':
                notaF=mediaUni(grauC,grauB)
                notaValida=True
            elif escolhaGrau=='b':
                notaF=mediaUni(grauA,grauC)
                notaValida=True
            else:
                print('Erro! escolha a ou b para ser substituido')
                notaValida=False
            
        if notaF >=6:
            print('a média final do aluno',aluno,'foi',notaF)
            print('o aluno',aluno,'foi Aprovado!')
        else:
            print('a média final do aluno',aluno,'foi',notaF)
            print('o aluno',aluno,'foi Reprovado!')

    somageral=somaGeral(notaF,somageral)

mediaGeral=somageral/nAlunos
print(mediaGeral,'pontos foi a média geral entre todos os',nAlunos,'alunos avaliados')