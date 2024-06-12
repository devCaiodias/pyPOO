import pandas as pd
import numpy as np

np.random.seed(42)
serie = pd.Series(data=np.random.normal(size=10))
print(serie)
print(serie > 0)
print((serie > 0) & (serie < 1))

print()

serie1 = pd.Series(np.arange(10))
serie2 = pd.Series(np.arange(10), index=np.arange(10, 20))
# print(serie1[serie2 > 5])

serie1 = pd.Series(np.arange(10))
serie2 = pd.Series(np.arange(10))
print(serie1[serie2 > 5])

print(any((serie > 0) & (serie < 1)))
print(all((serie > 0) & (serie < 1)))

print()

serie4 = pd.Series(list("abdefghijklmnopqrstuvwyz"))

print(serie4)
print(serie4.isin(["a", "e", "i", "o", "u"]))
print(serie4[serie4.isin(["a", "e", "i", "o", "u"])])


serie = pd.Series([1,2,3, np.nan, 5, np.nan, 7])
print(np.isnan(serie))
print(serie.isnull())
print(pd.isnull(np.nan))

serie = pd.Series(np.arange(10))
print(serie.where(lambda x: x > 5))

print(serie.where(lambda x: x > 5, "Não é maior que cinco"))

