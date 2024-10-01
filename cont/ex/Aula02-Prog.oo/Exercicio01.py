class Retangulo:
    def __init__(self,base,altura):
        self.base=int(base)

        self.altura=int(altura)

    def calcularArea(self):
        area=int(self.base*self.altura)
        print(area)           #print direto no metodo

    def calcularPerimetro(self):
        perimetro=int(2*(self.base+self.altura))
        return(perimetro)     #return

    calcularArea
    calcularPerimetro

base=10
altura=5

ret=Retangulo(base,altura)

ret.calcularArea()
#ou
print(ret.calcularPerimetro())