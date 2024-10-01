class Sistema:
    def __init__(self):
        self.hotel=None
        #self.cliente=Cliente(self,idCliente,nome,CPF,numero)
        #self.reserva=Reserva(self,idReserva,dataInicio,dataFim)
        #self.quarto=Quarto(self,N,status)
    def menu(self,nomeHotel):
        fechar=False
        print('seja bem-vindo ao sistema do hotel',nomeHotel,'!')
        while fechar!=True:

            print('-MENU-')
            print('Realizar Reserva ---> 1')
            print('Realizar Check-In --> 2')
            print('Realizar Check-Out -> 3')
            print('Verificar Reserva --> 4')
            print('Fechar Sistema -----> 0')
            res=int(input('escolha o número da ação que deseja realizar'))
            if res==1:
                ReservasHotel(self)
            elif res==2:
                #checkin
                pass
            elif res==3:
                #checkout
                pass
            elif res==4:
                #verReserva
                pass
            elif res==0:
                fechar=True
                print('Encerrando Sistema...')

    def criarhotel(self):
        #tributos fixos do hotel
        self.nomeHotel='Viridis Agro'
        self.listaQuartos=(101,102,103,104,201,202,203,204,301,302,303,304)
        self.listaReservas=()
        self.hotel=Hotel

#construtores classes hotel,cliente,reserva,quarto
class Hotel:
    def __init__(self,nomeHotel,listaQuartos,listaReservas):
        self.nomeHotel=str(nomeHotel)
        self.listaQuartos=(listaQuartos)
        self.listaReservas=(listaReservas)

class Cliente:
    def __init__(self,idCliente,nome,CPF,numero):
        self.idCliente=int(idCliente)
        self.nome=str(nome)
        self.CPF=int(CPF)
        self.numero=int(numero)
            
class Reserva:
    def __init__(self,idReserva,dataInicio,dataFim):
        self.idReserva=int(idReserva)
        self.dataInicio=int(dataInicio)
        self.dataFim=int(dataFim)

class Quarto:
    def __init__(self,N,status):
        self.N=int(N)
        self.status=str(status)
    
def ReservasHotel(self):
    nome=input('digite seu Nome: ')
    Cpf=input('digite seu CPF')

#start
sistema=Sistema()
sistema.criarhotel(nomeHotel)
sistema.menu()

