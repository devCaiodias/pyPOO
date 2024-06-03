import pandas as pd
import sklearn
from sklearn.datasets import load_iris

data = load_iris()

# E então carrengando o dataset iris como Dataframe do pandas
df = pd.DataFrame(data['data'], columns= data['feature_names'])
df['species'] = data['target']

print(df.head())

# Para criar um grafico de linhas com todas as variáveis do dataframe, basta fazer isso:
print(df.plot())

# Que tal um scatter plot com dessas variaveis?
print(df.plot.scatter(x= 'sepal length (cm)', y='sepal width (cm)'))

columns = ['sepal length (cm)', 'sepal width (cm)'  ,'petal length (cm)'  ,'petal width (cm)']
print(df[columns].plot.area())