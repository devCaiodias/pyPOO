import numpy

# Criando Arrays Numpy
arr2 = numpy.array([1, 2, 3, 4, 5])
print(arr2)
print(arr2.cumsum())
print(arr2.cumprod())
print(numpy)

# A função arange cria um array Numpy contendo uma progressão aritmetica a partir de um intervalo - atart, stop, step 
arr3 = numpy.arange (0, 50, 5)

print(arr3)

# Verificando o tipo do objetos
print(type(arr3))

# formato do Array
print(numpy.shape(arr3))
print(arr3.dtype)


# Criar um array preenchido com zeros

arr4 = numpy.zeros(10)
