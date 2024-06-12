from unittest import result
import pandas as pd
import numpy as np

np.random.seed(42)

serie1 = pd.Series(data=np.random.normal(size=5))
serie2 = pd.Series(data=np.random.normal(size=5), index=np.arange(4, -1, -1))
serie3 = pd.Series(data=np.random.normal(size=5), index=np.arange(10, 15))
serie4 = pd.Series(data=np.random.normal(size=5), index=np.arange(4, 9))

print(serie1)
print(serie2)
print(serie3)

print()

print(serie1 + serie2)
print(serie1 + serie3)
print(serie1 + serie4)

print()

# Soma

print(serie1 + serie2)
print(serie1 + 2)
print(serie1.add(serie2))
print(serie1.add(np.array([1,2,3,4,5]))) # pode ser array, lista ou tuple
print(serie1.add(serie4, fill_value=0))

print()

# Subtração

print(serie1 - serie2)
print(serie1.sub(serie2))
print(serie1.subtract(serie2))

print()

# Multiplicação

print(serie1 * serie2)
print(serie1 * serie4)
print(serie1.mul(serie2))

print()

# Multiplicação (produto vetorial)

print(serie1.dot(serie2))

print()

# Divisão

print(serie1 / serie2)
print(serie1.div(serie2))

print()

# Exponenciação

print(serie1 ** serie2)
print(serie1 ** 2)
print(serie1.pow(serie2))

print()

# Execicio

p = pd.Series([1,2,3,4,5,6,7,8,9,10])
q = pd.Series([10,9,8,7,6,5,4,3,2,1])

def calculando_euclidiana(serie1, serie2):
    
    return np.sqrt(sum((serie1 - serie2)**2))

resultado = calculando_euclidiana(p, q)

print(resultado)