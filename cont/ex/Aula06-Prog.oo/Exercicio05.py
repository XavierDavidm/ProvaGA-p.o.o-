import csv
class Veiculo:
    def __init__(self,codigo,fabricante,modelo,ano,cor,motor,preco): #atributos: codigo,fabricante,modelo,ano,cor,motor,preco
        self.codigo=int(codigo)
        self.fabricante=str(fabricante)
        self.modelo=str(modelo)
        self.ano=int(ano)
        self.cor=str(cor)
        self.motor=float(motor)
        self.preco=float(preco)

class Revenda:
    def __init__(self): #vector
        self.vector=[]   
    def cadastrarVeiculo(self):
        codigo=int(input('digite o codigo do veiculo: '))
        fabricante=str(input('digite a fabricante do veiculo: '))
        modelo=str(input('digite o modelo do veiculo: '))
        ano=int(input('digite o ano do veiculo: '))
        cor=str(input('digite a cor do veiculo: '))
        motor=float(input('digite o motor do veiculo: '))
        preco=float(input('digite o preço do veiculo: '))
        m=(codigo,fabricante,modelo,ano,cor,motor,preco)
        self.vector.append(m)
        veiculo=Veiculo(codigo,fabricante,modelo,ano,cor,motor,preco)
        print(self.vector)
    def listar(self):
        print(len(self.vector)) #teste
        modeloFiltro=str(input('digite o modelo que deseja filtrar a lista: '))
        for i in range(len(self.vector)):
            print('')
    def remover(self):
        pass

    def salvar(self):
        pass

    def carregar(self):
        self.vector=[]
        with open('veiculos.csv', mode='r', encoding='utf-8') as arquivo:
            reader = csv.reader(arquivo, delimiter='\t')
            for linha in reader:
                linhaPronta = [campo.strip() for campo in linha]
                self.vector.append(linhaPronta)
            print(self.vector)





#menu   
revenda=Revenda()
encerrar=False
while encerrar != True:
    print('---MENU---')
    print('1-> Cadastrar')
    print('2-> Listar')
    print('3-> Remover')
    print('4-> Salvar')
    print('5-> Carregar')
    print('0-> Sair')
    resposta=int(input('digite o numero da operação: '))
    if resposta==0:
        encerrar=True
    elif resposta==1:
        print('---Cadastro de Veiculo---')
        revenda.cadastrarVeiculo()
    elif resposta==2:
        print('---Filtro de Veiculos---')
        revenda.listar()
    elif resposta==3:
        pass
    elif resposta==4:
        pass
    elif resposta==5:
        print('---Carregando veiculos---')
        revenda.carregar()
    else:
        print('ERRO')








