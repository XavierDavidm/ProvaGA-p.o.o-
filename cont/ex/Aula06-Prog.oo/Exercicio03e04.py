#3 e 4 aula 06

class Pessoa:
    def __init__(self): #nome,sexo,idade,altura,peso
        self.__nome=0
        self.__sexo=0
        self.__idade=0
        self.__altura=0
        self.__peso=0
    
    #nome
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self):
        raise ValueError('erro nome')
    def registarNome(self):
        nome=str(input('digite seu nome completo: '))
        self.__nome=nome
    def getNome(self):
        return self.__nome
    #sexo
    @property
    def sexo(self):
        return self.__sexo
    @sexo.setter
    def sexo(self):
        raise ValueError('erro sexo')
    def registarSexo(self):
        sexo=str(input('digite seu sexo (M/F): '))
        self.__sexo=sexo
    def getSexo(self):
        return self.__sexo
    #idade
    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self):
        raise ValueError('erro idade')
    def registrarIdade(self):
        idade=int(input('digite sua idade: '))
        self.__idade=idade
    def getIdade(self):
        return self.__idade
    #altura
    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self):
        raise ValueError('erro altura')
    def registrarAltura(self):
        altura=float(input('digite sua altura: '))
        self.__altura=altura
    def getAltura(self):
        return self.__altura
    #peso
    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self):
        raise ValueError('erro peso')
    def registrarPeso(self):
        peso=float(input('digite seu peso: '))
        self.__peso=peso
    def getPeso(self):
        return self.__peso

    #criar/ver
    def criarPessoa(self):
        self.registarNome()
        self.registarSexo()
        self.registrarIdade()
        self.registrarAltura()
        self.registrarPeso()
    def visualizar(self):
        print('Nome: ',self.getNome())
        print('Sexo: ',self.getSexo())
        print('Idade: ',self.getIdade())
        print('Altura: ',self.getAltura())
        print('Peso: ',self.getPeso())

    #carregar/salvar
    def carregar(self):
        arquivo=open('pessoa.txt','r')
        nome=arquivo.readline().rstrip('\n')
        self.__nome=nome
        sexo=arquivo.readline().rstrip('\n')
        self.__sexo=sexo
        idade=arquivo.readline().rstrip('\n')
        self.__idade=idade
        altura=arquivo.readline().rstrip('\n')
        self.__altura=altura
        peso=arquivo.readline().rstrip('\n')
        self.__peso=peso
        arquivo.close()
    def salvar(self):
        m=(str(self.__nome))+'\n'+(str(self.__sexo))+'\n'+(str(self.__idade))+'\n'+(str(self.__altura))+'\n'+(str(self.__peso))
        arquivo=open('pessoa.txt','w')
        arquivo.write(m)
        arquivo.close()

pessoa1=Pessoa()
pessoa1.carregar()
pessoa1.visualizar()
pessoa1.registrarIdade()
pessoa1.registrarPeso()
pessoa1.salvar()












