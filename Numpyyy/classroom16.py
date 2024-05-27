import numpy

arr26 = numpy.array([[1, 2, 3 , 4], [5,6,7,8]])
print(arr26)

# 'Achatando' a matrize
arr27 = arr26.flatten()
print(arr27)

arr28 = numpy.array([1,2,3])

print(arr28)

# Repetindo os elementos de um arrays
print(numpy.repeat(arr28, 3))

# Repetindo os elementos de um arrays
print(numpy.tile(arr28, 3))


arr29 = numpy.array([5,6])

arr30 = numpy.copy(arr29)
print(arr30)