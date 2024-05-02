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

