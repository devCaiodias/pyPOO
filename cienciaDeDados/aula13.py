import pandas as pd
import numpy as np

por_dirc = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}
serie_dirc = pd.Series(data=por_dirc)
# print(serie_dirc)

# print(serie_dirc[1])
# print(serie_dirc[[1, 2]])
# print(serie_dirc["b"])
# print(serie_dirc[["b", "c"]])

serie_complexa = pd.Series(
    data=[1,2,3],
    index=[3,2,1]
    )

print(serie_complexa)

# print(serie_complexa[3])
# print(serie_complexa.iloc[0])
# print(serie_complexa.iloc[[1,2]])
# print(serie_complexa.iloc[1:])

# print(serie_dirc["b":])
# print(serie_dirc["b":"c"])
# print(serie_dirc["b":"e":2])
# print(serie_dirc["e":"b":-2])

# print(serie_dirc)
# serie_dirc["b" : "c"] = 3
# print(serie_dirc)

print(por_dirc)

s1 = serie_dirc["b":"c"]
s1[:1] = 20
print(serie_dirc)

def muda_serie(serie):
    serie.iloc[-1] = np.inf
muda_serie(serie_dirc)
print(serie_dirc)

print(serie_complexa.loc[3])


