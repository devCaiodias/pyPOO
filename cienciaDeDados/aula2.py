import numpy as np

array = np.array([1,2,3,4,5])
print(array)

matriz = np.array([[1,2,3], [4,5,6]])
print(matriz)

print(
    f"array: dtype:{array.dtype} / shape:{array.shape} / size:{array.size} "
    f"/ itemsize:{array.itemsize} / strides:{array.strides}"
)

# print(
#     f"matriz: dtype:{matriz.dtype} / shape:{matriz.shape} / size:{matriz.size} "
#     f"/ itemsize:{matriz.itemsize} / strides:{matriz.strides}"
# )

# Criando um array prenchido com zero
# print(np.zeros(shape=(3, 2)))

# # Criando um array prenchido com one 
# print(np.ones(shape=(3)))

# # Criando matriz identidade com o tamanho especifico
# print(np.eye(4))

# print(np.arange(1,10,2))

# # Criando um array entre dois numeros espaçados linearmente
# print(np.linspace(5,10, num=5))

# # Criando um array entre dois numeros espaçados logaritimicamente
# print(np.logspace(0,1,3))

# # Criando um array aleatorio entre valores menor e maiores
# print(np.random.randint(0, 10, size=(5, 5)))

# # Criando um array aleatorio com valores baseados em uma distribuição normal
# print(np.random.normal(1, 2, 10))

# a = np.arange(12)
# a = a.reshape(3,4)
# print(a)

# Execicio 

matriz_ex = np.linspace(5, 11, 16).reshape(4,4)
print(matriz_ex)
amarzenamento = matriz_ex.itemsize * matriz_ex.size
print("Amazenamento do array: ", amarzenamento)