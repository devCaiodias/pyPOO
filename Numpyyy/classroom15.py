from re import A
import numpy

arr22 = numpy.diag(numpy.arange(3))
print(arr22)
print(arr22[1,1])
print(arr22[1])
print(arr22[:,2])

arr23 = numpy.arange(10)

print(arr23)

# [start:end:stop]
print(arr23[2:9:3])

a = numpy.array([1,5,6,8])
b = numpy.array([5,4,8,4])

# Comparação item aitem
print(a == b)

# Comparação global
print(numpy.array_equal(arr22, arr23))

print(arr23.min)
print(arr23.max)

# Somando um valor a cada elemnto do array
print(numpy.array([1,2,3, 4]) + 1.5)

arr24 = numpy.array([2.5, 3.5 ,4.5 ,5.5, 6.9])
print(arr24)

# Usando o metado around
arr25 = numpy.around(arr24)

print(arr25)

