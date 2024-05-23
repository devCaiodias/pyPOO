import numpy

# Criando Arrays Numpy
arr1 = numpy.array([10, 21, 32, 124, 443, 35, 43])
print(arr1)

# Imprimindo um elemento especifico no array
print(arr1[2])

# Indexção
print(arr1[1:4])
print(arr1[1:4+1])

# Cria uma lista de indices
indices = [1, 2, 5, 6]
print(arr1[indices])

# Criando uma mascara boleana para os elementos pares
mask = (arr1 % 2 == 0)
print(mask)
print(arr1[mask])

# Alterando um elemento dp array
arr1[0] = 100

print(arr1)

# Não é possivel incluir elementos de outro tipo
try:
    arr1[0] = 'Novo elemento'
except:
    print('Operação n concluida')