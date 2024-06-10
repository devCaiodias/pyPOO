import numpy

numpy.random.seed(42)
arr = numpy.random.randint(0,100, size=10)
print(arr)

print(arr > 50)

print((arr > 50) & (arr < 70))

print(arr[(arr > 50) & (arr < 75)])


numpy.random.seed(42)
arr = numpy.random.randint(0,100, size=10)

print(all((arr > 50) & (arr < 75 )))
print(numpy.all((arr > 50) & (arr < 75 )))

print(any((arr > 50) & (arr < 75 )))
print(numpy.any((arr > 50) & (arr < 75 )))


print(arr.reshape(2,5) < 70)

print(numpy.all(arr.reshape(2,5) < 70))
print(numpy.all(arr.reshape(2,5) < 70, axis=0))


# Excicio 
import numpy as np

array1 = np.random.choice([1,2,3,4,5,6,7,8,9,10,np.nan], size=(5,5))

# Replace all np.nan values with 0
array1[np.isnan(array1)] = 0

print(array1)