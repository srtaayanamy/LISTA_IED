# Reverso de Fila: 
'''Utilizando apenas operações de fila (enfileirar e desenfileirar), escreva uma função que inverta a ordem dos elementos de uma fila.'''

class Ordem_Fila:
    def __init__(self):
        self.fila = []

    def enqueue (self, item):
        self.fila.append(item)

    def desenfileirar (self):
        stack = []
        while self.fila:
            stack.append(self.fila.pop(0))
        while stack:
            self.fila.append(stack.pop())
        return self.fila
        
    def mostrar(self):
        if self.fila:
            print('\nFILA ATUAL:')
            print(self.fila)
        else:
            print('A FILA NÃO EXISTE.')
        
main = Ordem_Fila()
while True:

    print('\nESCOLHA O QUE DESEJA FAZER:\n [1]Adicionar itens na fila\n [2]Inverter fila\n [3]Mostrar fila\n [4]Sair')
    esc = int(input())

    if esc == 1:
        item = input('QUAL O ITEM QUE DESEJA ADICIONAR? ')
        main.enqueue(item)
        print('ITEM ADICIONADO À FILA.')

    elif esc == 2:
        retorno = main.desenfileirar()
        print('\nFILA INVERSA:')
        print(retorno)

    elif esc == 3:
        main.mostrar()

    elif esc == 4:
        print('ENCERRANDO PROGRAMA...')
        break
    
    else:
        print('OPÇÃO INVÁLIDA, por favor escolha dentre as opções listadas.')
