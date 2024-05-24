import numpy

# Criar um array preenchido com zeros
arr4 = numpy.zeros(10)

print(arr4)

# Retorna 1 nas posiçoes em diagonal e 0 no restante
arr5 = numpy.eye(3)
print(arr5)

# Os valores passados como parametro, formam uma diagonal
arr6 = numpy.diag(numpy.array([1, 2, 3, 4]))

print(arr6)

# Array de valores booleanos
arr7 = numpy.array([True, False, False, True])

print(arr7)

# Array de string
arr8 = numpy.array(['Linguagem PY', 'Limguagem R', 'Limguagem GO'])

print(arr8)

print(numpy.linspace(0,10,15))