# Utilizando apenas operações de fila (enfileirar e desenfileirar), escreva uma função que inverta a ordem dos elementos de uma fila.

class Fila:
    def __init__(self):
        self.filinha = []
    
    def enfilheirar (self, item):
        self.filinha.append(item)
    
    def desenfileirar (self):
        if self.filinha:
            self.filinha.reverse()
            return self.filinha
        else:
            return False
        
filinha = Fila()
while True:

    print('Deseja fazer o quê?\n 1-Adicionar na lista;\n 2-Inverter a lista')
    esc = int(input())

    if esc == 1:
        item = input('Digite o item: ')
        filinha.enfilheirar(item)
        print('Item enfileirado')

    elif esc == 2:
        inverso = filinha.desenfileirar()
        if inverso != False:
            print(inverso)
        else:
            print('Não tem fila')
    else:
        break