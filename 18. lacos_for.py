# LAÇOS FOR
# for [variável de iteração] in [sequência]:
# [faça alguma coisa]

for i in range(0, 5):
  print(i)

print()

# RANGE
# range( [start], [stop], [step] ) → Entre 1 e 3 argumentos inteiros.
# - [start] indica o valor inteiro no qual a sequência começa; se não estiver incluído, o start começa com 0;
# - [stop] é sempre necessário e é o número inteiro máximo da sequência, mas não está incluído;
# - [step] define quanto aumentar (ou diminuir, no caso de números negativos) na próxima iteração, se for omitido, será por padrão 1;

# Somente com [stop]:
for i in range(6):
  print(i)

print()

# Somente com [start] e [stop]:
for i in range(20, 25):
  print(i)

print()

# Com [start], [stop] e [step]:
for i in range(0, 15, 3):
  print(i)

print()

# Decrescente
for i in range(50, 0, -10):
  print(i)

print()

# LAÇOS FOR EM DADOS SEQUENCIAIS
# LISTAS

animais = ['gato', 'cachorro', 'papagaio', 'canguru']
for animal in animais:
  print(animal)

print()

# Adicionar itens na lista
animais = ['gato', 'cachorro', 'papagaio', 'canguru']
for item in range(len(animais)): # 4
  animais.append('animal')
print(animais) 
# Para cada item, imprima um 'animal'

print()

inteiros = []
for i in range(10):
  inteiros.append(i)
print(inteiros)

print()

# Percorrer uma lista de strings
nome = 'animal'
for letra in nome:
  print(letra)

print()

# BIBLIOTECA
cliente = {'nome': 'José', 'idade': '31', 'cidade': 'Brasília', 'UF': 'DF'}
for chave in cliente:
  print (chave + ': ' + cliente[chave])

print()

# LAÇOS ANINHADOS
# Um laço aninhado é um laço que ocorre dentro de outro laço

minha_lista = []
for x in [20, 40, 60]:
  for y in [2, 4, 6]:
    minha_lista.append(x * y)
print(minha_lista) 

print()

lista_numeros = [1, 2, 3]
lista_letras = ['a', 'b', 'c']
for numero in lista_numeros:
  print(numero)
  for letra in lista_letras:
    print(letra)

print()

lista_de_listas = [['cavalo', 'vaca', 'gato'],[0, 1, 2],[9.9, 8.8, 7.7]]
for lista in lista_de_listas:
  print(lista)

print()

lista_de_listas = [['cavalo', 'vaca', 'gato'],[0, 1, 2],[9.9, 8.8, 7.7]]
for lista in lista_de_listas:
  for item in lista:
    print(item)

print()

# BREAK, CONTINUE e PASS
# BREAK
numero = 0
for numero in range(10):
  numero = numero + 1
  print(numero)
  if numero == 5:
    break
print('Fora do laço, BREAK')

print()

# CONTINUE
numero = 0
for numero in range(10):
  numero += 1
  if numero == 5:
    continue
  print(numero)
print('Fora do laço, CONTINUE')

print()

#PASS
numero = 0
for numero in range(10):
  numero = numero + 1
  if numero == 5:
    pass
  print(numero)
print('Fora do laço')

print()

# DESAFIO
# 1. Crie um laço for que imprima os valores de 0 a 9.

for i in range(0, 10):
  print(i)

print()
# 2. Crie um laço for que imprima os valores de 9 a 0 reduzindo 2 unidades por vez.
for i in range (9, 0, -2):
  print(i)

print()
# 3. Crie um laço for que imprime a lista ['joao', 'maria', 'pedro', 'paulo'] em ordem inversa.
nomes = ['joao', 'maria', 'pedro', 'paulo']
for i in range(len(nomes)-1, -1, -1):
  print(nomes[i])
  print(i)

# 4. Usando laços for aninhados, imprima a tabuada de 0 a 5.

# tabuada = []
# for x in [1, 2, 3, 4, 5]:
#   for y in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     tabuada.append(x * y)

# print(tabuada)

for i in range(11):
  for j in range(11):
    print("{} * {} = {}".format(i, j, i*j))

print()

# 5. Crie um laço for que itera de 1 a 10 porém só imprime os números pares usando a instrução continue.

# for i in range(11):
#   if i % 2 == 0:
#     print(i)
#   continue

for i in range(11):
  if i % 2 != 0:
    continue
  print("{} é par".format(i))
