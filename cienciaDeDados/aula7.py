import numpy as np

arr = np.array([1,2, np.nan, 4])

print(arr)

print(np.isnan(arr))

# print(np.zeros(3) / 0)

arr = np.array([1,2, np.inf, 4 , -np.inf])

print(arr)
print(np.isfinite(arr))

print(np.pi)
print(np.e)