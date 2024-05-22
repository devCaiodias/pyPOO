# Criando um novo tipo de objeto chamado carro
class Carro():
    pass

if __name__ == '__main__':
    # Intancia da class
    ferrari = Carro()

    print(type(ferrari))


# Criando uma class
class Estudantes():
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

if __name__ == '__main__':
    # Criando um objeto chamado  Estudandte1 a partir da class Estudantes
    Estudante1 = Estudantes('Bob', 15, 1.2)

    # Atributos da class Estudante1, utiliznado por cada objeto criado a partir desta class
    print(Estudante1.nome)
    print(Estudante1.idade)
    print(Estudante1.nota)
    