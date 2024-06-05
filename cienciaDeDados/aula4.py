import numpy as np
import pandas as pd

# indexação


arr = np.arange(1, 10)

matriz = np.random.normal(1,2,(3,3))
print(arr)
print(matriz)

print(arr[0])
print(matriz[2][-1])
print(matriz[1])
print(arr[::2])
print(matriz[:,1])

# Execicio

def converter(array, passo, janela):
    convertida = [array[passo*i:passo*i+janela] for i, x in enumerate(array) if passo*i+janela <= array[-1]]
    return np.array(convertida)

arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
passo = 2
janela = 4
print(converter(arr1,passo, janela))
