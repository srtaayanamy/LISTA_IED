# mostra item por item

thislist = [1, 2, 3]
for x in thislist:
  print(x)

# imprime todos os itens, usando um loop while para percorrer todos os números de índice

lista02 = ["apple", "banana", "cherry"]
i = 0
while i < len(lista02):
  print(lista02[i])
  i = i + 1

# sort = coloca em ordem alfabética

list = ["orange", "mango", "kiwi", "pineapple", "banana"]
list.sort()
print(list)

# [ for x in range(inicio, fim, passo): ]

'''
print('impares\n')
for y in range(1, 100, 2):
  print (y)

print('pares\n')
for y in range(0, 101, 2):
  print (y)

'''

# zip = liga duas listas pelo indice / facilita na hora de usar o range(len())

nomes = ['anna', 'joao', 'caio', 'luiz']
idades = ['12', '13', '14', '15']
for nome, idade in zip (nomes, idades):
    print(f'{nome} tem {idade} anos')