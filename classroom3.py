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
    circ = Circulo()

    # Usando o métado da class
    print(circ.getRaio())

    # criando outro objeto chamado circ1, Uma instancia da class Circulo()
    # Agora sobrescrevendo o valor do atributo
    circ1 =  Circulo(7)

    # Imprimindo o raio
    print(f'O raio é {circ1.getRaio()}')

    # Imprimindo a area
    print(f'O area é {circ1.area()}')

    # Gerando um novo valor para o raio do circulo
    circ1.setRaio(3)

    # Imprimindo o novo raio
    print(f'Novo raio igual a, {circ1.getRaio()}')

    
    