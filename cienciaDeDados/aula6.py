import numpy as np
import pandas as pd

np.random.seed(42)
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
m1 = np.random.randint(1,10, size=(3,3))
m2 = np.random.randint(1,10, size=(3,3))

print(m1)
print(m2)
print()

# Soma
print(arr1 + arr2)
print(np.add(arr1, arr2))

# subtração

print(arr1 - arr2)
print(np.subtract(arr1, arr2))

# Multiplicação (escalar)

print(arr1 * 2)
print(arr1 * 2.1)
print(np.multiply(arr1, 2))

# Multiplicação (element-wise)

print(arr1 * arr2)
print(np.multiply(arr1, arr2)) 

# Multiplicação (produto vetorial)

print(sum(arr1 * arr2))
print(np.dot(arr1, arr2))

print(np.cross(arr1, arr2))

print(m1@m2)
print(np.matmul(m1, m2))

# Divisão

print(arr1 / arr2)
print(np.divide(arr1, arr2))

# Exponenciação

print(arr1 ** 2)
print(arr1 ** arr2)
print(np.power(arr1, arr2))

# Modulo de vetor

print(sum(arr1 * arr1) ** 0.5)
print(np.linalg.norm(arr1))

# Determinante de uma matriz

print(np.linalg.det(m1))

# Matriz inversa
print(np.linalg.inv(m1))

# Matriz transporta
print(np.transpose(m1))
print(m1.T)

arr3 = np.array([1,2,3,4])

# arr3 + arr1 

arr3 = np.array([[1,2,3], [4, 5,6]])

print(arr3 + arr1)

x = np.arange(4)
xx = x.reshape(4,1)
y = np.ones(5)
z = np.ones((3, 4))

print((xx + y).shape)
print(xx + y)

print((x + z).shape)
print(x + z)
