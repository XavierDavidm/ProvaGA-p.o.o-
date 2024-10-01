class Veiculo:
    def __init__(self, codigo, fabricante, modelo, ano, cor, motor, preco):
        self.codigo = codigo
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.motor = motor
        self.preco = preco

    def serializar(self):
        return f"{self.codigo}\t{self.fabricante}\t{self.modelo}\t{self.ano}\t{self.cor}\t{self.motor}\t{self.preco}"

    @staticmethod
    def deserializar(linha):
        codigo, fabricante, modelo, ano, cor, motor, preco = linha.strip().split("\t")
        return Veiculo(codigo, fabricante, modelo, int(ano), cor, float(motor), float(preco))


class Revenda:
    def __init__(self):
        self.__veiculos = []

    def cadastrar(self, veiculo):
        self.__veiculos.append(veiculo)

    def listar(self, modelo):
        return [veiculo for veiculo in self.__veiculos if veiculo.modelo == modelo]

    def remover(self, codigo):
        self.__veiculos = [veiculo for veiculo in self.__veiculos if veiculo.codigo != codigo]

    def salvar(self, arquivo):
        with open(arquivo, 'w') as f:
            for veiculo in self.__veiculos:
                f.write(veiculo.serializar() + "\n")

    def carregar(self, arquivo):
        self.__veiculos.clear()
        with open(arquivo, 'r') as f:
            for linha in f:
                veiculo = Veiculo.deserializar(linha)
                self.cadastrar(veiculo)


def menu():
    revenda = Revenda()
    while True:
        print("\nMenu:")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Remover")
        print("4. Salvar")
        print("5. Carregar")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            codigo = input("Código: ")
            fabricante = input("Fabricante: ")
            modelo = input("Modelo: ")
            ano = int(input("Ano: "))
            cor = input("Cor: ")
            motor = float(input("Motor: "))
            preco = float(input("Preço: "))
            veiculo = Veiculo(codigo, fabricante, modelo, ano, cor, motor, preco)
            revenda.cadastrar(veiculo)
        
        elif opcao == '2':
            modelo = input("Modelo a listar: ")
            veiculos = revenda.listar(modelo)
            for v in veiculos:
                print(v.serializar())
        
        elif opcao == '3':
            codigo = input("Código do veículo a remover: ")
            revenda.remover(codigo)
        
        elif opcao == '4':
            revenda.salvar("veiculos.txt")
        
        elif opcao == '5':
            revenda.carregar("veiculos.txt")
        
        elif opcao == '0':
            break


if __name__ == "__main__":
    menu()