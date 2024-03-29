# Escreva uma função que receba duas listas e as intercale em uma única lista. Não utilize métodos prontos da linguagem e faça a intercalação elemento a elemento.

lista1 = []
lista2 = []
lis_intercalada = []

def intercalar (lista1, lista2):
  i = 0
  j = 0

  while i < len(lista1) and j < len(lista2):
    lis_intercalada.append(lista1[i])
    lis_intercalada.append(lista2[j])
    i += 1
    j += 1

  lis_intercalada.extend(lista1[i:])
  lis_intercalada.extend(lista2[j:])
  return lis_intercalada

def adicionar01 (item):
   lista1.append(item)
   print('Item adicionado á lista 1!')

def adicionar02 (item):
   lista2.append(item)
   print('Item adicionado á lista 2!')

while True:
    esc = input('Escolha a opção:\n 1-Adicionar item ás listas.\n 2-Intercalar listas.\n')
    if esc == '1':
       qlista = input('deseja adicionar itens á lista 1 ou 2?\n')
       if qlista == '1':
          item = input('Que item deseja adicionar?\n')
          lista1.append(item)
       else: 
          item = input('Que item deseja adicionar?\n')
          lista2.append(item)

    elif esc == '2':
       lis_intercalada = intercalar(lista1, lista2)
       print(lis_intercalada)
       break

#oh my im so happy i just do it this amazing algoritimo uauu