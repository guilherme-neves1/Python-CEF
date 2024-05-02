# 1 - VALOR ABSOLUTO → abs()
km_inicial = 125
km_final = 33
print("Diferença: " + str(km_final - km_inicial))
# Diferença: -92

distancia_percorrida = abs(km_final - km_inicial)
print("A distância percorrida foi: " + str(distancia_percorrida) + "km.")
# A distância percorrida foi: 92km.
print()

# 2 - DIVISÃO DO INTEIRO E MÓDULO → divmod()
a = 10
b = 3
print(divmod(a, b))
# Basicamente executamos: (a // b, a % b).
print()

# Exemplo:
# → Digamos que escrevemos um livro com 80.000 palavras.
# → Com nosso editor, temos a opção de 300 ou 250 palavras por página e gostaríamos de ter uma ideia de quantas páginas teríamos em cada caso.
# → Com divmod(), podemos ver imediatamente quantas páginas teríamos e quantas palavras sobrariam em uma página adicional.
# • Se dividirmos 80 mil palavras por 300, quantas páginas teriam o livro e quantas palavras sobrariam?
# • Se dividirmos 80 mil palavras por 250, quantas páginas teriam o livro e quantas palavras sobrariam?

palavras = 80000
por_pagina_A = 300
por_pagina_B = 250
msg = "Com a opção {0} são necessárias {1[0]} páginas e sobram {1[1]} palavras"

# Opção A
resA = divmod(palavras, por_pagina_A) # (a, b) = (266, 200).
print(msg.format("A", resA))
# 1[0] → palavras // por_pagina_A
# 1[1] → palavras % por_pagina_A
# Com a opção A são necessárias 266 páginas e sobram 200 palavras
print()

resB = divmod(palavras, por_pagina_B)
print(msg.format("B", resB))
# "B" → [0]
# resB → [1] 
# resB {1[0]} → palavras // por_pagina_B
# resB {1[1]} → palavras % por_pagina_B
print()

# 3 - POTENCIAÇÃO → pow()
horas = 24
total_bacterias = pow(2,horas) # 2 elevado a 24

print(str(total_bacterias) + " bactérias")
# 16777216 bactérias
print()

# 4 - ARREDONDAMENTO → round()
i = 17.34989436516001
print(round(i, 4)) # Arredonde "i" para 4 casas decimais
print()

# Exemplo:
# Três amigos foram a um restaurante que deseja dividir uma conta de R$ 87,93 uniformemente, além de adicionar uma gorjeta de 20%:
conta = 87.93
taxa = 0.2
nmr_pessoas = 3

total_conta = conta + (conta * taxa)
valor_individual = total_conta / nmr_pessoas

print("Valor sem arredondar: " + str(valor_individual))
# Valor sem arredondar: 35.172000000000004
print()

valor_individual2 = round(valor_individual, 2)
print("Valor arredondado: " + str(valor_individual2))
# Valor arredondado: 35.17
print()

# É possível arredondar um número com 0 como valor decimal, pode-se fazer isso usando 0 como o segundo parâmetro na função round():
exemplo = round(345.9874590348545304636, 0)
print(exemplo) # 346.0
print()

# 5 - SOMA → sum()
lista_alguns_floats = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
print(sum(lista_alguns_floats))

tuplas = (8, 16, 64, 512)
print(sum(tuplas))

dicionario = {-10: 'x', -20: 'y', -30: 'z'}
print(sum(dicionario))

# Na soma do dicionário, a soma ocorre pelas chaves e não pelos valores.
print(sum({-10: 30, -20: 'y', -30: 'z'}))

# A função sum() pode receber até 2 argumentos
alguns_floats = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9] # 49.5
print(sum(alguns_floats, 0.5)) # 50.0

print(sum({-10: 'x', -20: 'y', -30: 'z'}, 60)) # -60 + 60 = 0

# DESAFIO
# 1. Calcule o valor absoluto de 100-500.
# 2. Calcule a divisão inteira e o resto de 53 e 7.
# 3. Calcule 10 elevado a 10.
# 4. Arredonde 5.47484 para uma casa decimal.
# 5. Some a lista [1, 5, 99, 45, 33]

print(abs(100 - 500))
print(divmod(53, 7))
print(pow(10, 10))
print(round(5.47484, 1))
print(sum([1, 5, 99, 45, 33]))
