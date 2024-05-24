import numpy

# Criando uma matriz
# arr9 = numpy.array([[1,2,3], [4,5,6]])

# print(type(arr9))
# print(arr9)
# print(arr9.shape)

# Criando uma matriz 2x3 apenas com numeros 1
arr10 = numpy.ones((2, 3))

print(arr10)

# Lista de listas
lista = [[15,56,68], [14,78,99], [25,69,78]]

# Afunção matrix cria uma matriz a partir de uma lista de listas
arr11 = numpy.matrix(lista)

print(arr11)
# print(arr11.shape)

# Tamanho da matriz 

# print(arr11.size)

# Indexação da Matriz

# print(arr11[2,1])
# print(arr11[0:2,2])
# print(arr11[1,])
# arr11[1,0] = 100
# print(arr11)


x = numpy.array([1,2]) # NumPy decide o tipo de dados
y = numpy.array([1.0,2,0]) # NumPy decide tipo de dados
s = numpy.array([1,2], dtype= numpy.float64) # forçando um tipo de dado em particular

print(x.dtype, y.dtype, s.dtype)

arr12 = numpy.array([[15,56,68], [14,78,99]], dtype = float)

print(arr12)

print(arr12.itemsize)
print(arr12.nbytes)
print(arr12.ndim)

