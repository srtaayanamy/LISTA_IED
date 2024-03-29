# Escreva uma função que receba uma lista e reverta a ordem de seus elementos, sem criar uma nova lista.

lista = []  
while True:
    
    print('1-Adicionar\n2-Reverter')   
    esc = int(input('\nEscolha: '))    

    if esc == 1:
        item = input('\nDigite o item que você quer adicionar: ')
        lista.append(item)
        print(f'\Item adicionado. ')

    elif esc == 2:
        lista.reverse()
        print(lista)
        break