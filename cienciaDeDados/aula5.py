import numpy as np
import pandas as pd

# Mutabilidade

arr = np.array([1,2,3])
# arr.append(4) isso aki da erro
# arr[2] = 5
# arr[1] = 9.5
# arr[0] = '5'
# print(arr)

a = np.arange(12, dtype='int64')
b = a.reshape(3,4)
c = a[::2]
print(a)
print()
print(b)
print()
print(c)

a[0] = 1
print(a)
print()
print(b)
print()
print(c)


print(f"a: dtype={a.dtype} / shape:{a.shape} / size:{a.size} / itemsize:{a.itemsize} / strides:{a.strides}")
print(f"b: dtype={b.dtype} / shape:{b.shape} / size:{b.size} / itemsize:{b.itemsize} / strides:{b.strides}")

print(f"a: dtype={a.dtype} / shape:{a.shape} / size:{a.size} / itemsize:{a.itemsize} / strides:{a.strides}")
print(f"c: dtype={c.dtype} / shape:{c.shape} / size:{c.size} / itemsize:{c.itemsize} / strides:{c.strides}")

def muda_a(a):
    a[1] = 15564

print(a)
muda_a(a)
print(a)
print()
print(b)
print()
print(c)

def matriz_quadrada(tamanho:int, tipo:str):
    arr = np.zeros(shape=(tamanho, tamanho))

    if tipo == "Q":
        arr[0,:] = 1
        arr[-1,:] = 1
        arr[:,0] = 1
        arr[:,-1] = 1
    
    if tipo == 'V':
        arr[:, 0] = 1
        arr[:, -1] = 1

    if tipo == 'H':
        arr[0,:] = 1
        arr[-1,:] = 1

    if tipo == 'P':
        arr = np.ones(shape=(tamanho, tamanho))

        arr[0,:] = 0
        arr[-1,:] = 0
        arr[:,0] = 0
        arr[:,-1] = 0

    return arr

print(f'Tipo Q:\n{matriz_quadrada(2, "Q")}\n')
print(f'Tipo V:\n{matriz_quadrada(4, "V")}\n')
print(f'Tipo H:\n{matriz_quadrada(4, "H")}\n')
print(f'Tipo P:\n{matriz_quadrada(4, "P")}\n')