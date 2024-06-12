import pandas as pd
import numpy as np

np.random.seed(42)
serie = pd.Series(np.random.randint(10, size=10))
serie.iloc[np.random.randint(10, size=2)] = np.nan
# print(serie)

# print(serie.fillna(-1))
# serie.fillna(-1, inplace=True)
# print(serie)

print(serie.ffill())
print(serie.bfill())

# np.where(serie.isnull(), np.where(serie, x, y), serie)