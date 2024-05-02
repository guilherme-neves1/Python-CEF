# CONCATENAR LISTAS
criaturas_maritimas = ['tubarão', 'peixe', 'lula', 'camarão', 'anêmona']
oceanos = ['Pacífico', 'Atlântico', 'Ártico', 'Índico','Antártico']
print(criaturas_maritimas + oceanos)
print()

print(criaturas_maritimas + ['hermitão'])
print()

# MULTIPLICAR
oceanos = ['Pacífico', 'Atlântico', 'Ártico', 'Índico','Antártico'] 
print(oceanos * 2)
print()

# ATRIBUIR
criaturas_maritimas = ['tubarão', 'peixe', 'lula', 'camarão']
criaturas_maritimas += ['anêmona']
print(criaturas_maritimas)
print()

criaturas_maritimas *= 2
print(criaturas_maritimas)
print()

# REMOVER ITENS
criaturas_maritimas = ['tubarão', 'peixe', 'lula', 'camarão']
del criaturas_maritimas[1]
print(criaturas_maritimas)
print()

criaturas_maritimas = ['tubarão', 'peixe', 'lula', 'camarão']
del criaturas_maritimas[1:4]
print(criaturas_maritimas)
print()

# LISTAS DE LISTAS
nomes_marinhos = [['tubarão', 'peixe', 'camarão'], ['Barbatana', 'Nemo', 'Cascudo']]

# Na primeira lista, o segundo item
print(nomes_marinhos[0][1]) # peixe

# Na segunda lista, o terceiro item
print(nomes_marinhos[1][2]) # Cascudo
print()

# DESAFIO

# 1. Crie uma lista com 5 linguagens de programação chamada de ‘linguagens’.
linguagens = ['Python', 'Javascript', 'Java', 'Cobol', 'Kotlin']
print(linguagens)

# 2. Imprima o 3º elemento desta lista.
print(linguagens[2])

# 3. Imprima o último elemento desta lista.
print(linguagens[-1])

# 4. Modifique o primeiro elemento da lista para 'C++'.
linguagens[0] = 'C++'
print(linguagens)

# 5. Concatene na lista a linguagem 'Prolog'.
linguagens += ['Prolog']
print(linguagens)
print()

# MÉTODOS DE LISTA

# list.append()
peixes = ['tilápia', 'bacalhau', 'sardinha', 'enguia']

peixes.append('salmao')
print(peixes)
print()

# O método list.append() é diferente do método de concatenação:
# Enquanto o método de concatenação gera uma nova lista, o método list.append altera a própria lista original.

# list.insert(i, x) 
# usa dois argumentos, sendo i a posição de índice na qual você deseja adicionar um item e x o próprio item:
peixes = ['tilápia', 'bacalhau', 'sardinha', 'enguia']
peixes.insert(0, 'anchova')
print(peixes)
print()

# list.extend(l)
# Combinar mais de uma lista 'l'
peixes = ['tilápia', 'bacalhau', 'sardinha', 'enguia']
outros_peixes = ['lambari', 'traíra']
peixes.extend(outros_peixes)
print(peixes)
print()

# list.remove()
peixes = ['tilápia', 'bacalhau', 'sardinha', 'enguia']
peixes.remove('tilápia')
print(peixes)
print()

# list.pop()
# O método list.pop() é muito comum em pilhas.
# O método list.pop() faz duas coisas ao mesmo tempo: retorna e remove.
peixes = ['tilápia', 'bacalhau', 'sardinha', 'enguia']

print(peixes.pop()) # enguia
print(peixes)

print(peixes.pop(1)) # bacalhau
print(peixes)
print()

# list.index()
peixes = ['tilápia', 'bacalhau', 'sardinha', 'enguia']
print(peixes.index('sardinha'))
