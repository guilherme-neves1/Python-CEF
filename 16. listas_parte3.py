# MÉTODOS DE LISTAS
# list.copy()
# Os métodos de listas alteram diretamente a lista. 
# Para evitar isso, deve-se criar uma cópia e fazer as operações sobre essa cópia.
peixes = ['tilápia', 'bacalhau', 'sardinha', 'enguia']
peixes2 = peixes.copy()

peixes2.append('lambari')

print(peixes)
print(peixes2)
print()

# list.reverse()
peixes = ['tilápia', 'bacalhau', 'sardinha', 'enguia']
peixes.reverse()
print(peixes)
print()

# list.count()
peixes = ['tilápia', 'bacalhau', 'sardinha', 'enguia']
print(peixes.count('tilápia')) # 1

peixes.append('tilápia')
print(peixes)
print(peixes.count('tilápia')) # 2
print()

# list.sort()
# O método sort serve para ordenar os itens da lista em ordem alfabética, numérica, etc.
peixes = ['tilápia', 'bacalhau', 'sardinha', 'enguia']
peixes.sort();
print(peixes)
print()

# list.clear()
# Limpa a lista → []
peixes = ['tilápia', 'bacalhau', 'sardinha', 'enguia']
peixes.clear();
print(peixes)
print()

# DESAFIO 
# 1. Crie uma lista de nomes de países: Brasil, Nova Zelândia, Austrália, França.
paises = ['Brasil', 'Nova Zelândia', 'Austrália', 'França']
print(paises)

# 2. Insira na primeira posição o país 'Suécia'.
paises.insert(0, 'Suécia')
print(paises)

# 3. Remova o último elemento e o imprima.
print(paises.pop())
print(paises)

# 4. Faça uma cópia da lista.
paises2 = paises.copy()
print(paises2)

# 5. Ordene a lista de forma invertida.
paises.sort()
paises.reverse()
print(paises)
print()

# INSTRUÇÕES CONDICIONAIS
# IF ELSE
nota = 60
if nota >= 65:
  print("Passou")
else:
  print("Reprovou")

# ELIF
nota = 65
if nota > 65:
  print("Passou")
elif nota == 65:
  print("Passou no limite")
else:
  print("Reprovou")

# Exemplo
nota = 72
if nota >= 90:
  print("A")
elif nota >= 80:
  print("B")
elif nota >= 70:
  print("C")
elif nota >= 60:
  print("D")
else:
  print("Reprovou")
  