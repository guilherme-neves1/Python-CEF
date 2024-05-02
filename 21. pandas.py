# Biblioteca do Python - PANDAS

# 1 - Tipos de operações
# Tenha em mente que o Pandas é focado no uso final, para o analista de dados, enquanto o NumPy está no nível básico.
# Com o Pandas, é possível realizar as cinco etapas típicas no processamento e análise de dados, independentemente da origem dos dados:
# • Carregar, por exemplo, um tipo de arquivo Excel ou outro tipo de arquivo mais complicado;
# • Preparar, limpar base de dados, converter números;
# • Manipular;
# • Modelar; e
# • Analisar os dados.
# Obs.: essa biblioteca é utilizada para análise de dados já na fase final.

# 2 - Estruturas de Dados
# O Pandas lidará com três estruturas de dados importantes, que são as Series, DataFrame e Panel.

# I. Series: Uma Series é um array unidimensional capaz de armazenar qualquer tipo de dados (inteiros, strings, números de ponto flutuante, objetos Python, etc.). As etiquetas dos eixos são chamadas coletivamente de índice. Uma série do pandas pode ser criada usando o seguinte construtor:
# pandas.Series( data, index, dtype, copy)

import pandas as pd
s = pd.Series()
print(s)
print()

import numpy as np
data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data)
print(s)
print()

data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data, index=[100, 101, 102, 103])
print(s)
print()

data = {'a': 0., 'b': 1., 'c': 2.}
s = pd.Series(data)
print(s)
print()

# II. DataFrame: Um DataFrame é uma estrutura de dados bidimensional, ou seja, os dados são alinhados de forma tabular em linhas e colunas. O DataFrame do pandas pode ser criado usando vários inputs, como listas, dicionários, Series, ndarrays, outro DataFrame, etc. Aqui está o construtor básico de um DataFrame:
# pandas.DataFrame( data, index, columns, dtype, copy)

df = pd.DataFrame()
print(df)
print()

data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)
print()

data = [['José', 10], ['Pedro', 12], ['Paulo', 13]]
df = pd.DataFrame(data, columns=['Nome', 'Idade'])
print(df)
print()

# III. Panel: Um Panel é uma estrutura de dados tridimensional. Os termos “Panel data” e “dados longitudinais” são usados ​​intercambiavelmente. No entanto, a partir da versão 0.20.0 do pandas, o suporte para o Panel está descontinuado e não é mais recomendado para uso. Em vez disso, é preferível usar estruturas MultiIndex DataFrame para manipulação de dados tridimensionais.
# pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)
# EM DESUSO
