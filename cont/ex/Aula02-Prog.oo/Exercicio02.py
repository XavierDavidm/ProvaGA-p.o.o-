class Data:
    def __init__(self,dia,mes,ano):
        if dia > 0 and dia <= 31:
            self.dia=int(dia)
        else:
            self.dia=0
            print('Dia inválido!')
        if mes > 0 and mes <= 12:
            self.mes=int(mes)
        else: 
            self.mes=0
            print('Mês inválido!')
        if ano > 0:
            self.ano=int(ano)
        else:
            self.ano=0
            print('Ano inválido!')

    def displayData(self):
        print("{}/{}/{}" .format(self.dia, self.mes, self.ano))

    #extra: alterar data com validação
    def alterarData(self):
        print(' Dia -> 1','\n','Mes -> 2','\n','Ano -> 3','\n')
        res=int(input('digite o Número que deseja alterar: '))
        if res==1:
            dia=int(input('digite o dia: '))
            if dia > 0 and dia <= 31:
                self.dia=int(dia)
            else:
                self.dia=0
                print('Dia inválido!')

        if res==2:
            mes=int(input('digite o mes: '))
            if mes > 0 and mes <= 12:
                self.mes=int(mes)
            else: 
                self.mes=0
                print('Mês inválido!')

        if res==3:
            ano=int(input('digite o ano: '))
            if ano > 0:
                self.ano=int(ano)
            else:
                self.ano=0
                print('Ano inválido!')

    def getDia(self):
        return dia
    def getMes(self):
        return mes
    
#main
dia=int(input('digite o dia: '))
mes=int(input('digite o mes: '))
ano=int(input('digite o ano: '))
DataTest=Data(dia,mes,ano)

#validação extra
DataValida=False
while DataValida!=True:
    if DataValida!=True:
        resposta='n'
        while resposta!='s':
            DataTest.displayData()
            resposta=input('a data está correta (s/n)? ')
            if resposta!='s':
                DataTest.alterarData()
    DataTest.getDia()
    DataTest.getMes()
    if (dia > 0 and dia <=31) and (mes > 0 and mes <=12):
        DataValida=True
    else:
        DataValida=False
        print('Data inválida!')
