# Criando uma class
class Circulo():
    # valor do PI é constante
    PI = 3.14

    # Quando um objeto desta class for criado, este métado será executado e o valor default do raio será 5:
    def __init__(self, raio = 5) -> None:
        self.raio = raio

    # Esse métado calcula a area:
    def area(self):
        return (self.raio * self.raio) * Circulo.PI
    
    # Métado para gerar um novo raio:
    def setRaio(self, novo_raio):
        self.raio = novo_raio

    # Métado para obter o raio do Circulo
    def getRaio(self):
        return self.raio
    


if __name__ == '__main__':
    # Criando um objeto chamado  Estudandte1 a partir da class Funcionario
    pass

    # Usando o métado da class

    
    