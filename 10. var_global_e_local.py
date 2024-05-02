# Cria uma variável global, fora de uma função:
glb_var = "global"

# Define uma função:
def var_function (): 
  lcl_var = "local" # Cria uma variável local, dentro da função
  return lcl_var # Retorna a variável local

# Chama a função para imprimir a variável local
print(var_function())

# Imprime variável global fora da função
print(glb_var)
print()

# MESMO NOME PARA VARIÁVEL GLOBAL E LOCAL (FUNCIONA)

num1 = 5 # Variável global

def minha_function ():
  num1 = 10 # Usa o mesmo nome de variável num1
  num2 = 7 # Atribui a variável local
  print(num1) # Imprime a variável local num1
  print(num2) # Imprime a variável local num2

# Chama minha_function()
minha_function()
# Imprime a variável global num1
print(num1)

# FUNCIONA PORÉM O CÓDIGO FICA PROPENSO A BUGS

print()

# ATRIBUIR UMA VARIÁVEL GLOBAL DENTRO DE UMA FUNÇÃO

def nova_msg():
  global msg # Atribui a variável como global
  msg = "Olá Mundo!"

nova_msg() # Chama a função para poder imprimir a msg
print(msg)

# OBS.: Essa prática deve ser evitada, pois reduz a legibilidade do código.
print()

# FORMATAÇÃO DE STRINGS
print("Pedro tem {} laranjas.".format(5))

modelo = "Pedro tem {} laranjas."
print(modelo.format(5))
print(modelo.format(9))

# Pode ser reutilizado em vários locais do programa para exibir a mesma mensagem, trocando-se apenas o núcleo.

modelo = "Pedro tem {} laranjas e {} maçãs."
print(modelo.format("cinco", "dez"))

modelo = "Pedro tem {0} laranjas e {1} maçãs."
print(modelo.format("cinco", "dez"))
# Pedro tem cinco laranjas e dez maçãs.

modelo = "Pedro tem {1} laranjas e {0} maçãs."
print(modelo.format("cinco", "dez"))
# Pedro tem dez laranjas e cinco maçãs. 

modelo = "Pedro tem {1} laranjas e {0} maçãs e {of} outras frutas."
print(modelo.format("cinco", "dez", of = "três"))
# Pedro tem dez laranjas e cinco maçãs e três outras frutas.

# Tipo de conversão
# • “s” para string; 
# • “d” para exibir números inteiros decimais; e 
# • “f”, para exibir números de ponto flutuante.

modelo = "Pedro tem {0:s} laranjas e {1:3d} maçãs e {2:.3f} outras frutas."
# • O uso de “3d” indica que se trata de um número decimal de três posições. Por isso, o sistema complementará o número com espaços em branco.
# • O uso de “{2:.3f}” indica que o sistema deve apresentar depois do ponto apenas 3 posições, arredondando o número.

print(modelo.format("cinco", 10, 3.55477))
print()

# DESAFIO
# 1. Crie uma variável inteira com o valor 50.
# 2. Crie uma variável que represente a nota do aluno e atribua o valor de 8.5 utilizando as regras de estilo recomendadas.
# 3. Crie uma variável x e atribua ao valor 150, em seguida atribua x ao valor do dobro de x.
# 4. Crie uma função imprime_texto que imprime o valor de uma variável global chamada texto.
# 5. Imprima o número 357.756 com duas casas decimais utilizando o método format.

a = 50
nota_aluno = 8.5
x = 150
x = x * 2

texto = "Um texto"

def imprime_texto():
  print(texto)

imprime_texto()

print("{0:.2f}".format(357.756))
