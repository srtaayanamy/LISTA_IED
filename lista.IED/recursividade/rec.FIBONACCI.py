# Implemente uma função recursiva que retorne o N-ésimo termo da sequência de Fibonacci. Teste a função com valores de N pequenos e grandes e observe a performance.


def f(n):

    if n == 1:
        return (0)
    if n == 2:
        return (1)
    if n > 2:
        return (f(n-1) + f(n-2))
    
n = int(input('Quantos elementos? '))

for i in range(1, n):
        print(f(i))