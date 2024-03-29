# Implementação de Lista: 
'''Crie uma classe Lista que implemente as seguintes operações básicas: inserção, remoção e busca de um elemento. Além disso, adicione um método para imprimir todos os elementos da lista.'''

class Lista:
    def __init__(self):
        self.list = []

    def inserir (self, item):
        self.list.append(item)
        print('ITEM ADICIONADO.')

    def remover (self, item):
        if item in self.list:
            self.list.remove(item)
            print('ITEM REMOVIDO.')
        else:
            print('O ITEM NÃO FOI LOCALIZADO.') 

    def busca (self, item):
        if item in self.list:
            return True
        else:
            return False
        
    def mostrar(self):
        if self.list:
            print(self.list)

main = Lista()
while True:

    print('\nLISTA DE ITENS:\n Faça uma escolha:\n [1]Adicionar\n [2]Remover\n [3]Buscar elemento\n [4]Mostrar lista\n [5]Sair')
    esc = int(input())
    if esc == 1:
        item = input('QUAL ITEM DESEJA ADICIONAR?\n')
        main.inserir(item)
    elif esc == 2:
        item = input('QUAL ITEM DESEJA REMOVER?\n')
        main.remover(item)
    elif esc == 3:
        item = input('QUAL ITEM DESEJA BUSCAR?\n')
        res = main.busca(item)
        if res == True:
            print(f'O ITEM {item} ESTÁ NA LISTA.')
        else:
            print(f'O ITEM {item} NÂO ESTÁ NA LISTA.')
    elif esc == 4:
        print('LISTA:')
        main.mostrar()
    elif esc == 5:
        print('ENCERRANDO O PROGRAMA...')
        break
    else: 
        print('OPÇÃO INVÁLIDA.')
        
