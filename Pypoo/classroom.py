#  criando a class livro com parametro no metado construtor
class Livro():
    def __init__(self, title, iabn):
        self.title =  title
        self.iabn = iabn
        print("Construtor chamado para criar um objetivo desta class.")

    def imprimir(self, title, iabn):
        print(f"Este é livro: {title} e IABN: {iabn}")

if __name__ == '__main__':
    pass
    # criando o objeto Livro2 que é uma instancia da class Livro()
    # livro2 = Livro("O poder do habito", 1551565)

    # print(livro2.title)
    # print(livro2.iabn)
    # Metádo do objeto Livro2
    # livro2.imprimir(livro2.title, livro2.iabn)


# Criando a class
class Algoritimo():

    def __init__(self, tipo_algo):
        self.tipo_algo = tipo_algo
        print("Construtor chamado para criar um objetivo desta class.")


if __name__ == '__main__':
    # criando o objeto Livro2 que é uma instancia da class Livro()
    algo1 = Algoritimo(tipo_algo='Random foret')
    algo2 = Algoritimo(tipo_algo='Deep Learning')

    # Atributo da class
    print(algo1.tipo_algo)
    print(algo2.tipo_algo)


