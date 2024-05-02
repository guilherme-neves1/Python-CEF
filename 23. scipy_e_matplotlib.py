# SCIPY
# Scipy é uma biblioteca de computação científica que usa NumPy por baixo.
# Foi criada por Travis Olliphant, o criador do NumPy.
# Fornece mais funções utilitárias para otimização, estatísticas e processamento de sinais.
# A maioria das novas funcionalidades de Data Science estão disponíveis no Scipy.
# Scipy é predominantemente escrito em Python, mas alguns segmentos são escritos em C.

# Importando os módulos necessários
import numpy as np
from scipy import linalg

# Vamos tentar resolver a equação:
#          1x + 2y = 5  
#          3x + 4y = 6

# Criar o array de entrada
A = np.array([[1, 2], [3, 4]])

# Criar o array de soluções
B = np.array([[5], [6]])

# Resolve com o módulo de álgebra linear
X = linalg.solve(A, B)

# Imprime os resultados
print("Solução: ")
print(X)

# Verifica os resultado
print("\n O vetor de resultados deve ser zero: ")
print(A.dot(X)-B)

#          1 * (-4) + 2 * 4,5 = 5
#          3 * (-4) + 4 * 4,5 = 6





