class Pais:

    def __init__(self,listaVizinhos):
        self.__codigoIso=0
        self.__nome=0
        self.__populacao=0
        self.__dimensao=0
        self.__listaVizinhos=listaVizinhos

    #codigo iso get/set
    @property
    def codigoIso(self):
        return self.__codigoIso
    @codigoIso.setter
    def codigoIso(self):
        raise ValueError('erro ISO')
    def registarIso(self):
        iso=str(input('digite o código ISO do país: '))
        self.__codigoIso=iso
    def getIso(self):
        return self.__codigoIso
    
    #nomePais get/set
    @property
    def nome(self):
       return self.__nome
    @nome.setter
    def nome(self):
        raise ValueError('erro nomePais')
    def registrarNomePais(self):
        nome=str(input('digite o nome do país: '))
        self.__nome=nome
    def getNomePais(self):
        return self.__nome

    #populacao get/set
    @property
    def populacao(self):
        return self.__populacao
    @populacao.setter
    def populacao(self):
        raise ValueError('erro POP')
    def registrarPopulacao(self):
        pop=int(input('digite a população do país: '))
        self.__populacao=pop
    def getPop(self):
        return self.__populacao

    #dimensao get/set
    @property
    def dimensao(self):
        return self.__dimensao
    @dimensao.setter
    def dimensao(self):
        raise ValueError('erro dimensao')
    def registrarDimensao(self):
        dim=int(input('digite a dimensão do país: '))
        self.__dimensao=dim
    def getDimensao(self):
        return self.__dimensao

    #listaVizinhos
    @property
    def ListaVizinhos(self):
        return self.__listaVizinhos
    @ListaVizinhos.setter
    def ListaViznhos(self):
        raise ValueError('erro listavizinho')
    def getListaVizinhos(self):
        return self.__listaVizinhos

    #metodos adicionais
    #verificar se dois paises são iguais
    def VerificarIgual(self,pais2):
        if self.__codigoIso == pais2.getIso():
            print('Representa o Mesmo país!')
        else:
            print('São países diferentes!')
    
    #verificar se dois paises são vizinhos
    def VerificarFronteira(self,pais2):
        vizinho=False
        for x in self.ListaVizinhos:
            if pais2.getNomePais()==x:
                vizinho=True
                break
        if vizinho:      
            print(self.__nome,'é vizinho de',pais2.getNomePais())
        else:
            print(self.__nome,'NÃO é vizinho de',pais2.getNomePais())

    #metodo para testes
    def CriarPaisCompleto(self):
        #self.registarIso()
        self.registrarNomePais()
        #self.registrarPopulacao()
        #self.registrarDimensao()

#main test
lista1=('chile','uruguai','argentina','guiana')
lista2=('brasil','chile','uruguai')
pais1=Pais(lista1)
pais2=Pais(lista2)
pais1.CriarPaisCompleto()
pais2.CriarPaisCompleto()
pais1.VerificarFronteira(pais2)
















