# Instruções IF Aninhadas
nota1 = 80
nota2 = 50
if nota1 > 60:
  if nota2 > 60:
    print('Passou nas duas fases')
  else:
    print('Só passou na primeira fase')
else:
  print('Não passou na primeira fase')
# Só passou na primeira fase
print()

# Combinando Condições
nota1 = 80
nota2 = 70
if nota1 > 60 and nota2 > 60:
  print('Passou nas duas fases')
elif nota1 > 60:
  print('Só passou na primeira fase')
else:
  print('Não passou na primeira fase')

# LOOP WHILE
senha = ''
while senha != 'admin':
  print('Digite a senha:')
  senha = input()

print('Senha correta!')

# EXEMPLO
import random
numero = random.randint(1, 25)
nr_tentativa = 0

while nr_tentativa < 5:
  print('Adivinhe um número entre 1 e 25:')
  chute = input()
  chute = int(chute)
  nr_tentativa += 1

  if chute < numero:
    print('Seu palpite é muito baixo')
  if chute > numero:
    print('Seu palpite é muito alto')
  if chute == numero:
    break
if chute == numero:
    print('Você adivinhou o número em ' + str(nr_tentativa) + ' tentativas!')
else:
    print('Você não adivinhou o número. Era ' + str(numero))

print()

# DESAFIO
# 1. Crie um programa que popula uma lista de 5 animais fornecidos pelo usuário e a imprime no final, porém não aceita a inserção de nomes de animais com menos de 3 letras;
animais = []
inseridos = 0

while inseridos <= 5:
  print('Digite o nome de um animal:')
  animal = input()
  if len(animal) < 3:
    print('Nome deve ter mais de 3 letras')
  else:
    animais.append(animal)
    inseridos += 1
print(animais)
