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

print()
# MATPLOTLIB
# Matplotlib é uma biblioteca de plotagem de gráficos de baixo nível em python que serve como uma utilidade de visualização.
# Foi criada por John D. Hunter.
# Matplotlib é principalmente escrita em python, mas alguns segmentos são escritos em C, Objective-C e Javascript para compatibilidade de plataforma.
# Matplotlib é uma biblioteca poderosa usada para criar visualizações estáticas, animadas e interativas.
# Oferece extensas opções de personalização para controlar todos os aspectos do gráfico, como estilos de linha, cores, marcadores, rótulos e anotações.
# Integra-se perfeitamente com NumPy, facilitando a plotagem de arrays de dados diretamente.
# Produz gráficos de alta qualidade adequados para publicação com controle refinado sobre a estética do gráfico.

# FUNÇÃO COM COORDENADAS PARA GERAR M GRÁFICO SIMPLES EM MATPLOTLIB

import matplotlib.pyplot as plt
import numpy as np

# • GRÁFICO SIMPLES
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])

plt.show() # Comando para visualizar o gráfico

# • GRÁFICO MAIS ELABORADO
x = np.linspace(0, 2, 100)

# Cria uma figura e os eixos.
fig, ax = plt.subplots()

# Plota dados nos eixos.
ax.plot(x, x, label='linear')

# Plota mais dados nos eixos.
ax.plot(x, x**2, label='quadratic')

# ... e mais algun dados
ax.plot(x, x**3, label='cubic')

# Adiciona um rótulo x aos eixos.
ax.set_title("Simple Plot")

# Adiciona uma legenda.
ax.legend()

plt.show()
