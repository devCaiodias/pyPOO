import numpy

arr15 = numpy.arange(1,10)
# print(arr15)

# # Somar todos os elementos
# print(numpy.sum(arr15))

# # Retornar o produto do elemento
# print(numpy.prod(arr15))

# # Soma acumulada dos elementos
# print(numpy.cumsum(arr15))

arr16 = numpy.array([2,5,8])
arr17 = numpy.array([5,6,2])

# somas dos array
arr18 = numpy.add(arr16, arr17)

# print(arr18)

arr19 = numpy.array([[2,5], [9,8]])
arr20 = numpy.array([[5,6], [6,8]])

print(arr19.shape)
print(arr20.shape)

print(arr19)
print(arr20)

# Multiplicar as duas matrizes
arr21 = numpy.dot(arr19,arr20)

print(arr21)





