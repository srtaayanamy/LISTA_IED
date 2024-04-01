# Fatorial:
'''Escreva uma função recursiva que calcule o fatorial de um número N.'''

def fat(n):
    if n == 0 or n == 1:
        return (1)
    else:
        return n*fat(n-1)

n = int(input('QUAL O NÚMERO QUE DESEJA CALCULAR O FATORIAL?\n'))
print('O FATORIAL É: ', fat(n))
