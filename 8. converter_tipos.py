# INTEIRO PARA FLUTUANTE
n = 10
print(n)
print(type(n))

f = float(n)

print(f)
print(type(f))
print()

# FLUTUANTE PARA INTEIRO
print(int(10.0))
# Python não efetua arredondamento
print(int(325.7))
print()

# NÚMEROS PARA STRINGS
m = 73
print("O usuário atual escreveu " + str (m) + " linhas de código")

h = 1.85
print("Sua altura é " + str (h) + " metros.")
print()

# STRINGS PARA NÚMEROS
a = "10"
b = "35"
c = int(b) - int(a)
print(c)

p1 = "5.2"
p2 = "7.3"
soma = float(p1) + float(p2)
print("A soma dos pontos é " + str(soma))
print()

# LISTA PARA TUPLA
lista = ["abacate", "uva", "laranja"]
tupla = tuple(lista)
print(tupla)

print(tuple("Olá Mundo!"))
print()

# TUPLA PARA LISTA
t = ("abacate", "uva", "laranja")
l = list(t)
print(l)

print(list('aluno'))
print()

# DESAFIO
# 1. Crie uma variável i com o valor 1Ø, crie outra variável f com o valor de i convertido para um float.
# 2. Imprima o texto: "O valor de i é 1Ø e o valor de f é 1Ø.Ø", convertendo os valores das variáveis.
# 3. Converta a string "32.7" e armazene em uma variável do tipo float.
# 4. Converta o inteiro 5ØØØ em uma lista. Dica: Converta primeiro para uma string.

i = 10
f = float(i)

print("O valor de i é " + str(i) + " e o valor de f é " + str(f))

g = float("32.7")

print(g)
print(type(g))

h = list(str(5000))
print(h)
