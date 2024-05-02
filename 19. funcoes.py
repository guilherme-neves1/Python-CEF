# DEFININDO UMA FUNÇÃO
def hello():
  print("Olá, mundo!")

hello()

print()
# A função definida abaixo utiliza uma instrução condicional para verificar se a entrada da variável nome contém uma vogal e, em seguida, usa um laço for para iterar sobre as letras na string de nome:
def nomes():
  nome = str(input('Digite seu nome: '))
  if set('aeiou').intersection(nome.lower()):
    print('Seu nome contém vogal.')
  else:
    print('Seu nome não contém vogal.')
  for letra in nome:
    print(letra)
# nomes()

print()
# PARÂMETROS NA FUNÇÃO
def adiciona_numeros(x, y, z):
  a = x + y
  b = x + z
  c = y + z
  print(a, b, c)

adiciona_numeros(1, 2, 3)

print()
# ARGUMENTOS NOMEADOS
def profile_info(usuario, seguidores):
  print("Usuário: " + usuario)
  print("Seguidores: " + str(seguidores))

profile_info("José", 100)
profile_info(usuario="Paulo", seguidores=200)

print()
# RETORNANDO UM VALOR
def quadrado(x):
  y = x ** 2
  return y

resultado = quadrado(3)
print(resultado)
print()

def adiciona_numeros(x, y, z):
  a = x + y
  b = x + z
  c = y + z
  return a, b, c
  
somas = adiciona_numeros(1, 2, 3)
print(somas)


