# CRIANDO
criaturas_maritimas = ['tubarão', 'peixe', 'lula', 'camarão', 'anêmona']
print(criaturas_maritimas)
print()

# ACESSAR UM DOS ITENS
print(criaturas_maritimas[1])
print()

# ACESSAR UM DOS ITENS COM NÚMEROS NEGATIVOS
print(criaturas_maritimas[-1])
print()

# Nessa lista:
# Números positivos: 0 a 4.
# Números negativos: -1 a -5.

# CONCATENAR LISTAS
print (criaturas_maritimas + ['polvo'])
print()

# MODIFICAR ITENS NA LISTA
criaturas_maritimas[1] = 'polvo'
print(criaturas_maritimas)
print()

criaturas_maritimas[-3] = 'baiacu'
print(criaturas_maritimas)
print()

# FATIAMENTO
# O índice final não entra na lista, 'anêmona'
criaturas_maritimas = ['tubarão', 'peixe', 'lula', 'camarão', 'anêmona']
print (criaturas_maritimas[1:4])
# Primeiro número (1): inclusive
# Segundo número (4): exclusive

# 0 ao 2
print (criaturas_maritimas[:3])

# 3 até o final
print (criaturas_maritimas[3:])

# Negativo
print (criaturas_maritimas[-4:-2])

print (criaturas_maritimas[-3:])
print()

# PASSO
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Do 1 até o 11, de 2 em 2
print(numeros[1:11:2])

# De 3 em 3 do total
print(numeros[::3])


