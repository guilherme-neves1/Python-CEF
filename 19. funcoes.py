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
print()

# COM 'return' O PRINT NÃO SERÁ NEM EXECUTADO
def meu_laco():
  for x in range(0, 25):
    print(x)
    if x == 5:
      return 
  print("Esta linha não será executada.")

meu_laco()

print()
# COM 'break' O PRINT SERÁ EXECUTADO
def meu_laco():
  for x in range(0, 25):
    print(x)
    if x == 5:
      break
  print("Esta linha será executada.")

meu_laco()

print()
# MAIN()
# A inclusão de uma função main(), embora não seja necessária, pode estruturar nossos programas Python de uma maneira lógica que coloca os componentes mais importantes do programa em uma única função;
def ola():
  print("Olá mundo!")

def main():
  print("Esta é a função principal.")
  ola()

main()

print()
# No Python, '__main__' é o nome do escopo em que o código de nível superior será executado;
# • Quando um programa é executado a partir da entrada padrão, de um script ou de um prompt interativo, seu __name__ é definido como '__main__'. 
# • Por causa disso, existe uma convenção para usar a seguinte construção:
# if __name__ == '__main__':
# Código a ser executado quando este for o programa principal

nome = str(input('Digite seu nome: '))

def tem_vogal():
  if set('aeiou').intersection(nome.lower()):
    print('Seu nome contém vogais.')
  else:
    print('Seu nome não contém vogais.')

def imprime_letras():
  for letra in nome:
    print(letra)

def main():
  tem_vogal()
  imprime_letras()

if __name__ == '__main__':
  main()

print()
# DESAFIO





