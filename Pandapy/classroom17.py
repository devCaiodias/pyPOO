import pandas as pd

dados = {'Estado': ['Santa Catarina', 'Rio de Janeiro', 'Tocantins', 'Bahia', 'Minas Gerais'],
         'Ano': [2004, 2005, 2007, 2008, 2009],
         'Taxa Desemprego' : [1.5, 1.7, 1.6, 2.4, 2.7]}

# print(dados)

# df = pd.DataFrame(data=dados)
# print(df.head())
# print(type(df))

# Reorganizando as colunas
print(pd.DataFrame(dados, columns= ['Estado', 'Taxa Desemprego', 'Ano']))

df2 = pd.DataFrame(dados,
                   columns= ['Estado', 'Taxa Desemprego', 'Taxa Crecimento', 'Ano'],
                   index= ['estado1', 'estado2', 'estado3', 'estado4', 'estado5'])

# print(df2)
# print(df2.values)
# print()
# print(df2.dtypes)

# Imprimindo apenas uma coluna do DataFrame
print(df2['Estado'])
print(df2[['Taxa Desemprego', 'Ano']])
print(df2.index)

# Filtrando pelo index
print(df2.filter(items= ['estado3'], axis=0))

