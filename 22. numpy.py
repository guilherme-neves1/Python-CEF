# Biblioteca Python - Numpy
# → Usada para trabalhar com números no Python;
# → É uma biblioteca Python que fornece um objeto de matriz multidimensional e uma variedade de rotinas para operações rápidas em matrizes, incluindo matemática, lógica, manipulação de formas, classificação, seleção, E/S, transformadas discretas de Fourier, álgebra linear básica, operações estatísticas básicas, simulação aleatória e muito mais;
# → No núcleo do pacote NumPy está o objeto ndarray.

# NDARRAY
# • É um array especial que quando se coloca valores nele e faz-se uma operação, ocorre uma performance muito maior do que o normal para o Python. 
# • Ele vai encapsular essas matrizes em dimensionais de tipos de dados homogêneos, com muitas operações sendo realizadas em código compilado para a questão de desempenho. 
# • A matriz deve ser homogênea.

# COMANDOS NUMPY
# • ndarray.ndim: o número de eixos (dimensões) da matriz;

# • ndarray.shape: as dimensões da matriz. É uma tupla de inteiros indicando o tamanho da matriz em cada dimensão. 
# Para uma matriz com n linhas e m colunas, o shape será (n, m). O comprimento da tupla shape é, portanto, o número de eixos ndim;

# • ndarray.size: o número total de elementos da matriz. 
# É igual ao produto dos elementos de shape; 

# • ndarray.dtype: um objeto que descreve o tipo dos elementos na matriz. 
# Pode-se criar ou especificar dtype’s usando tipos Python padrão. 
# Além disso, o NumPy fornece seus próprios tipos: numpy.int32, numpy.int16 e numpy.float64 são alguns exemplos;

# • ndarray.itemsize: o tamanho em bytes de cada elemento da matriz. 
# Por exemplo, uma matriz de elementos de tipo float64 tem itemsize 8 (=64/8), enquanto uma de tipo complex32 tem itemsize 4 (= 32/8). 
# É equivalente a ndarray.dtype.itemsize;

# • ndarray.data: o buffer que contém os elementos reais da matriz. 
# Normalmente, não será preciso usar este atributo porque acessaremos os elementos em um array usando recursos de indexação.

# CRIANDO ARRAYS
import numpy as np

a = np.array([2, 3, 4])
print(a)
print(a.dtype) # Tipo de dados dos elementos no array a. Deve retornar int32 ou int64, dependendo do sistema operacional.
print()

b = np.array([1.2, 2.3, 3.4])
print(b)
print(b.dtype)

print()
print(a.shape) # Como a é um array unidimensional com 3 elementos, deve retornar (3,)

# a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
# print(a.shape)
# Aqui a é um array bidimensional (uma matriz) com 3 linhas e 5 colunas. Portanto, a.shape retornará (3, 5). Cada lista interna representa uma linha da matriz.

print()
print(a.ndim) # Como a é um array unidimensional, deve retornar 1.

print()
print(a.dtype.name) # Deve retornar int32 ou int64.

print()
print(a.itemsize) # Tamanho em bytes de cada elemento no array a. Para int32, deve retornar 4. Para int64, deve retornar 8.

print()
print(a.size) # Número total de elementos no array a. Deve retornar 3.

print()
print(type(a)) # Deve retornar <class 'numpy.ndarray'>, que é a classe base para os arrays numpy.

# FORMATAÇÃO
# a = np.array( 1, 2, 3, 4, 5 ) # ERRADO
# a = np.array( [1, 2, 3, 4, 5] ) # CERTO

