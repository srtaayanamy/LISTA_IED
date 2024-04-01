# Torres de Hanói:
'''Escreva uma função recursiva que resolva o problema das Torres de Hanói. A função deve imprimir os movimentos necessários para mover N discos do pino A para o pino C, usando o pino B como auxiliar.'''

def hanoi(n, a, c, b):
    if n == 1:
        print(f"MOVE 1 DE {a} PRA {c}")
        return
    hanoi(n-1, a, b, c)
    print(f"MOVE {n} DE {a} PRA {c}")
    hanoi(n-1, b, c, a)

while True:
    a = 'A'
    b = 'B'
    c = 'C'
    n = int(input('DIGITE O NÚMERO DE DISCOS: '))
    hanoi(n, a, c, b)
    break
