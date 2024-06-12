import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

# print(np.concatenate([a, b]))
# print(np.concatenate([a, b], axis=0))
# # print(np.concatenate([a, b], axis=1))

# a = np.array([[1,2,3]])
# b = np.array([[4,5,6]])

# print(np.concatenate([a, b], axis=1))


# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(np.vstack([a, b]))

# a = np.array([[1,2,3]])
# b = np.array([[4,5,6]])
# print(np.vstack([a, b]))

# a = np.array([[1,2,3], [4,5,6]])
# b = np.array([[7,8,9], [10,11,12]])
# print(np.vstack([a, b]))

# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(np.hstack([a, b]))

# a = np.array([[1,2,3]])
# b = np.array([[4,5,6]])
# print(np.hstack([a, b]))

# a = np.array([[1,2,3], [4,5,6]])
# b = np.array([[7,8,9], [10,11,12]])
# print(np.hstack([a, b]))

a = np.array([1,2,3])
b = np.array([4,5,6])
# print(np.append(a, b))

a = np.array([[1,2,3]])
b = np.array([[4,5,6]])
print(np.append(a, b))

a = np.array([[1,2,3], [4,5,6]])
b = np.array([[7,8,9], [10,11,12]])
print(np.append(a, b))

