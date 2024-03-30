# Simulação de Fila de Banco: 
'''Implemente uma classe FilaDeBanco que simule a chegada e o atendimento de clientes. Utilize métodos para inserir clientes na fila, atender clientes e mostrar o estado atual da fila.'''

class FilaDeBanco:
    def __init__(self):
        self.fila = []
    
    def enqueue (self, pessoa):
        self.fila.append(pessoa)
        print(f'A PESSOA {pessoa} FOI ADICIONADA À FILA.')

    def dequeue (self):
        if self.fila:
            pessoa = self.fila.pop(0)
            print(f'O(a) cliente {pessoa} foi atendido(a).')
        else:
            print('A FILA NÃO EXISTE.')
    
    def is_empty(self):
        if not self.fila:
            return True 
        else:
            return False 

    def mostrar (self):
            print('\nFILA DE PESSOAS:\n')
            print(self.fila)

fila_clientes = FilaDeBanco()
while True:

    print('\nESCOLHA O QUE DESEJA FAZER:\n [1]Adicionar pessoas na fila\n [2]Atender alguém na fila\n [3]Mostrar Lista\n [4]Sair')
    esc = int(input())

    if esc == 1:
        pessoa = input('DIGITE A PESSOA QUE DESEJA ADICIONAR À FILA: ')
        fila_clientes.enqueue(pessoa)
    
    elif esc == 2:
        fila_clientes.dequeue()

    elif esc == 3:
        fila_clientes.mostrar()
        res = fila_clientes.is_empty() 
        if res == True:
            print('A FILA ESTÁ VAZIA.')

    elif esc == 4:
        print('ENCERRANDO PROGRAMA...')
        break

    else:
        print('OPÇÃO INVÁLIDA, por favor escolha uma das opções listadas.')
        
