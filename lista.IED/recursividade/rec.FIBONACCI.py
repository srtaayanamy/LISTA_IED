# Fibonacci:
'''Implemente uma função recursiva que retorne o N-ésimo termo da sequência de Fibonacci. Teste a função com valores de N pequenos e grandes e observe a performance.'''

def fibonacci (n):
    if n == 1:
        return (0)
    elif n == 2:
        return (1)
    if n > 2:
        return (fibonacci(n-1) + fibonacci(n-2))
    
print('QUAL O N-ÉSIMO TERMO? (Digite um número inteiro.)\n')
n = int(input())

print('O TERMO É {}!'.format(fibonacci(n)))
print('LISTA COMPLETA ATÉ O N-ÉSIMO TERMO:\n')
for i in range(1, n + 1):
     print(fibonacci(i))
