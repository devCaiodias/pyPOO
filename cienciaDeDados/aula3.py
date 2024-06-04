import pandas as pd
import numpy as np

arr = np.array([1,2,3])
print(arr.dtype, arr)

arr1 = np.array([1.0,2.0,3.0])
arr1 = arr1.astype("float")
print(arr1.dtype, arr1)

arr2 = np.array([1,2,3], dtype=np.uint8)
print(arr2.dtype, arr2)


def minimiza_memoria(array: np.array) -> np.ndarray:
    arr = np.array([array])
    arr1 = arr.astype("int8")
    return arr1

print(minimiza_memoria([1,2,3,5]))
