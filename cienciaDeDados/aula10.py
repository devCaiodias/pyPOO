import timeit
from matplotlib import axes
import numpy as np

func = np.vectorize(pyfunc= lambda a, b: a + b if a < b else a - b,
                    otypes=[float],
                    doc="""
                        Dados dosis array a e b calcula o valor da soma
                        dos dois caso a < b e a subtração caso contrario

                        :param a: array de dados a
                        :param b: array de dados b
                        :return: array com o resultado da operação
                        """,
                    cache=False,
                    # signature="(n), (m) -> (k)"
                    )

print(func(1.0,2.0))
print(func(2.0,1.0))

print(func(np.array([1,5,3]), np.array([2,4,6,])))

func1 = np.vectorize(
    pyfunc=lambda x: 1/ (1 + np.exp(-x)),
    otypes=[float],
    doc='''
        Aplica a transformação sigmoid sob o array

        :param x: array de dados
        :return: array de dados transformados        
        ''',
        cache=False,
        signature="(n)->(n)"
)

# print(func1(2))
print(func1(np.array([1,2,3])))

print(np.apply_along_axis(
     func1d=lambda x: 1 / (1 + np.exp(-x)),
     axis=0,
     arr=np.array([1,2,3,4])
))

print(
    np.apply_over_axes(
        func=lambda x, axes: x.any(axes),
        axes=(2,1),
        a=np.random.choice([True, False], size=(10, 5, 3))
    )
)