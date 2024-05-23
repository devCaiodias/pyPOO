# Criando Super class
class Veiculo():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        pass

    def frear(self):
        pass

# Sub class
class Carro(Veiculo):

    def acelerar(self):
        print('O carro está acelerando')

    def frear(self):
        print('o carro está freando.')

# Sub class
class Moto(Veiculo):

    def acelerar(self):
        print('O moto está acelerando')

    def frear(self):
        print('o moto está freando.')

# Sub class
class Aviao(Veiculo):

    def acelerar(self):
        print('O avião está acelerando')

    def frear(self):
        print('o avião está freando.')

    def decolar(self):
        print('o avião está decolando')

if __name__ == '__main__':
    
    # Criando os objetos
    listas_veiculos = [Carro('Porshe', "911 Turbo"), Moto('honda', 'CR 1000R black Edicion'), Aviao('Boeing', '757')]


    for item in listas_veiculos:
        
        # O métado acelerar tem comportamento diferente dependendo do tipo do objeto
        item.acelerar()

        # O métado frear tem comportamento diferente dependendo do tipo do objeto
        item.frear()

        # Executando o metado decolar somente se o objeto for instanciado da class Aviao
        if isinstance(item, Aviao):
            item.decolar() 

        print('---')