# Criando uma class
class Funcionarios:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def listFunc(self):
        print(f'Funcionario(a) {self.nome}, Tem salario de R${self.salario}, e o cargo é {self.cargo}')

if __name__ == '__main__':
    # Criando um objeto chamado  Estudandte1 a partir da class Funcionario
    func = Funcionarios('Caio', 2000, 'Cientista de dados')

    # Usando o métado da class
    func.listFunc()

    print('Usando Atributos')

    # tem nome
    print(hasattr(func,"nome"))
    # tem salario
    print(hasattr(func,"salario"))
    # mudando o valor do salario para 4500
    print(setattr(func,"salario", 4500))
    # tem salario
    print(hasattr(func,"salario"))
    # mostrar salario
    print(getattr(func,"salario"))
    # deletar o salario
    print(delattr(func,"salario"))
    # tem salario
    print(hasattr(func,"salario"))

    
    