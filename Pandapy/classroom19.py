from numpy import dtype
import pandas as pd
import numpy as np

dados = {'Estado': ['Santa Catarina', 'Rio de Janeiro', 'Tocantins', 'Bahia', 'Minas Gerais'],
         'Ano': [2004, 2005, 2007, 2008, 2009],
         'Taxa Desemprego' : [1.5, 1.7, 1.6, 2.4, 2.7]}

# Reorganizando as colunas
print(pd.DataFrame(dados, columns= ['Estado', 'Taxa Desemprego', 'Ano']))

df2 = pd.DataFrame(dados,
                   columns= ['Estado', 'Taxa Desemprego', 'Taxa Crecimento', 'Ano'],
                   index= ['estado1', 'estado2', 'estado3', 'estado4', 'estado5'])

print(df2.head())
print(df2.dtypes)

# Resumo estatística da Dataframe
print()
print(df2.describe())

# print(df2.isna())
# print(df2['Taxa Crecimento'].isna())

df2['Taxa Crecimento'] = np.arange(5.)
print(df2)
print(df2.dtypes)
print(df2['Taxa Crecimento'].isna())

# Resumo estatística da Dataframe
print()
print(df2.describe())
