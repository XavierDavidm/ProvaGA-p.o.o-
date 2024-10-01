#01 aula 4

class Pessoa:

    def __init__(self,nome,sexo,corOlhos,pai=None,mae=None):
        self.nome=str(nome)
        self.sexo=str(sexo)
        self.corOlhos=str(corOlhos)
        self.pai=(pai)
        self.mae=(mae)

    #setters e getters:
    def setSexo(self,sexo):
        #sexo=chr(input('digite o sexo da pessoa(M/F): '))    
        if sexo=='M' or sexo=='F':
            self.sexo=sexo 
        else:
            pass    

    def setCorOlhos(self,corOlhos):
        #corOlhos=chr(input('digite a cor dos olhos da pessoa(C/V/A): '))
        if corOlhos=='C' or corOlhos=='V' or corOlhos=='A':
            self.corOlhos=corOlhos
        else:
            pass

        #sexo char para string
    def getSexoStr(self):
        if self.sexo=='M':
            return 'Masculino'     
        elif self.sexo=='F':
            return 'Feminino'

        #corOlhos char para string
    def getCorOlhosStr(self):
        if self.corOlhos=='C':
            return 'Castanho'
            
        elif self.corOlhos=='V':
            return 'Verde'
            
        elif self.corOlhos=='A':
            return 'Azul'

    #geraPessoa
    def geraPessoa(self,nome,sexo,pai):
        if self.sexo=='F' and pai.getSexoStr()=='Masculino':
            if self.getCorOlhosStr()=='Castanho' or pai.getCorOlhosStr()=='Castanho':
                corOlhos='C'
                return Pessoa(nome,sexo,corOlhos,pai,self)
                
    #imprime dado
    

#main teste
pai=Pessoa('yuri','M','C')

mae=Pessoa('vanessa','F','V')

sexo='M'
filho=mae.geraPessoa('jonas',sexo,pai)
print(filho.getSexoStr())


