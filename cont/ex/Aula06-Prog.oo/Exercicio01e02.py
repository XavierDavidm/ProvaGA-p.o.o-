#1 manipulação de arquivos
def criarUser():
    v=()
    nome=str(input('digite seu nome completo: '))
    sexo=str(input('digite seu sexo (M/F): '))
    idade=int(input('digite sua idade: '))
    altura=float(input('digite sua altura: '))
    peso=float(input('digite seu peso: '))

    nome=str(nome)
    sexo=str(sexo)
    idade=str(idade)
    altura=str(altura)
    peso=str(peso)

    v=(nome,sexo,idade,altura,peso)
    arquivo=open('usuario.txt','a')
    arquivo.writelines('\n' + '\n'.join(v))
    arquivo.close()

def lerUser():
    arquivo=open('usuario.txt','r')
    nome=arquivo.readline()
    sexo=arquivo.readline()
    idade=arquivo.readline()
    altura=arquivo.readline()
    peso=arquivo.readline()

    print('nome: ',nome)
    print('sexo: ',sexo)
    print('idade: ',idade)
    print('altura: ',altura)
    print('peso: ',peso)
#user=criarUser()
user=lerUser()

























