# Criando class Animal - Super-class
class Animal():
    def __init__(self):
        print('Animal criado.')

    def imprimir(self):
        print("Este é um Animal")

    def comer(self):
        print('Hora de comer')
    
    def emitir_som(self):
        pass

# Criando a class Cachorro - Sub-class
class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Objeto Cachorro criado.')

    def emitir_som(self):
        print('AU AU!')

# Criando a class Gato - Sub-class
class Gato(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Objeto Gato criado.')

    def emitir_som(self):
        print('MIAU MIAU!')

if __name__ == '__main__':
    # Criando objeto (Instanciado a class)
    rex = Cachorro()
    # Criando objeto (Instanciado a class)
    zeze = Gato()

    # Executando métado que emite som
    rex.emitir_som()
    zeze.emitir_som()

    # Executando o métado da class Cachorro (sub-class)
    rex.imprimir()

    # Executando o métado da class Animal (sub-class)
    rex.comer()

    # Executando o métado da class Gato (sub-class)
    zeze.comer()
    
    