# Implemente uma classe FilaDeBanco que simule a chegada e o atendimento de clientes. Utilize métodos para inserir clientes na fila, atender clientes e mostrar o estado atual da fila.

class FilaDeBanco():
    def __init__(self):
        self.clientes = []
    
    def inserir(self, pessoa):
        self.clientes.append(pessoa)
        print('O cliente foi adicionado na fila.')

    def atender(self):
        if self.clientes:
            pessoa = self.clientes.pop(0)
            print(f'O(a) cliente {pessoa} foi atendido(a).')
        else:
            print('A fila está vazia.')

    def mostrar(self, pessoa):
        if self.clientes:
            for pessoa in self.clientes:
                print('-', pessoa)
        else:
            print('A fila está vazia.')
    
clientes = FilaDeBanco()
while True:
    esc = input('O que deseja fazer?\n1-Inserir cliente;\n2-Atender Cliente;\n3-Mostrar a fila.\n4-Sair\n')
    if esc == '1':
        pessoa = input('Digite o cliente que deseja adicionar: ')
        clientes.inserir(pessoa)
    elif esc == '2':
        clientes.atender()
    elif esc == '3':
        clientes.mostrar(pessoa)
    elif esc == '4':
        print('Encerrando a fila.')
        break
    else:
        print('Essa opção não existe')

# isso aqui foi de um terror, de um desespero sem precedentes 
