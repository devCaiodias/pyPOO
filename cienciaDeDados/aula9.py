import numpy as np

np.random.seed(42)
A = np.random.normal(loc=5, size=(5,3))
B = np.random.choice(["A", "B", "C"], size=(5,3))
C = np.array([0,1, 2,0,4,5])
D = np.random.normal(size=(5,3))

# Função MEDIA
# print(A, np.mean(A))
# print(A, np.mean(A, axis=-1))

# print()
# Função PERCENTILE
# print(A, np.percentile(A, 0.25))

# print(B, np.unique(B))
# print(C, C.shape, np.count_nonzero(C))


# Funçoes de TRANSFORMAÇÔES

# np.cell: Arredonda os valores de um array para cima.
# np.floor: Arredonda os valores de um array para baixo
# np.round: Arredonda os valores de um array para as casas decimais desejadas
# np.trunc: Remove as casas decimais do valor numérico
# np.abs: Calcula o valor absoluto dos elementos
# np.sign: Obtém os sinais dos números de um array

print()
print(A, np.ceil(A))
print(A, np.round(A, 2))
print(np.trunc(A))
print(D, np.sign(D))


# Função Matemática:

# np.exp: Realiza a exponenciação dos elementos
# np.log: Aplica o log sobre os elementos
# np.expm1: Aplica a função exp(x) - 1 sobre os elementos
# np.log1p: Aplica a função log(x + 1) sobre os elementos
# np.power: Eleva os elementals do array a uma potência
# np.sqrt: Extraí a raiz quadrada dos números de um array
# np.sin/cos/tan: Aplica a função seno/cosseno/tangente sobre os elementos
# np.asin/acos/atan: Aplica a função de arc seno/cosseno/tangente sobre os elementos

print()
print(np.log(A))
print(np.sin(D))

# Elemento a Elemento:

# np.diff: Obtém a diferença entre valores sequenciais do array
# np.cumsum: Obtém a soma dos valores cumulativos
# np.cummin: Obtém o valor mínimo cumulativo do array
# np.cummax: Obtém o valor máximo cumulativo do array
# np.cumprod: Obtém o valor produto cumulativo do array

print()
print(C, np.diff(C))
print(C, np.cumsum(C))