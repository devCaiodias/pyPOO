from turtle import color
import numpy
import csv
from pathlib import Path
from matplotlib import pyplot as plt

FILECAMINHO = Path(__file__).parent / 'dataset.csv'

with open(FILECAMINHO, 'r') as file:
    leitor = csv.reader(file)

    for linha in leitor:
        # print(linha)
        pass

    arr13 = numpy.loadtxt(FILECAMINHO, delimiter=',', usecols= (0,1,2,3), skiprows= 1)

    print(arr13)
    print(type(arr13))

    # Carregando um plot a partir de um arquivo usando o Numpy
    var1, vars2 = numpy.loadtxt(FILECAMINHO, delimiter=',', usecols=(0,1), skiprows= 1, unpack= True)

    # Gerando um plot a partir de um arquivo unsando o Nunpy
    plt.plot(var1, vars2, 'o', markersize= 6,color ='red')
    plt.show()
