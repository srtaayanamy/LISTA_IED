# Remoção de Duplicatas: 
'''Implemente uma função que remova todos os elementos duplicados de uma lista.'''

class Lista_sem_duplicatas:
    def __init__(self):
        self.lista = []

    def inserir (self, item):
        self.lista.append(item)
        print('ITEM ADICIONADO.')

    def remover (self, item):
        if item in self.list:
            self.lista.remove(item)
            print('ITEM REMOVIDO.')
        else:
            print('O ITEM NÃO FOI LOCALIZADO.')

    def mostrar(self):
        if self.lista:
            print(self.lista)

    def duplicatas(self, lista):
        self.sem_dup = set(self.lista)
        print(list(set(self.lista)))

lista = Lista_sem_duplicatas()

while True:
    print('\nLISTA DE ITENS:\n Faça uma escolha:\n [1]Adicionar\n [2]Remover item único\n [3]Mostrar lista\n [4]Remover duplicatas\n [5]Sair')
    esc = int(input())
    if esc == 1:
        item = input('QUAL ITEM DESEJA ADICIONAR?\n')
        lista.inserir(item)
    elif esc == 2:
        item = input('QUAL ITEM DESEJA REMOVER?\n')
        lista.remover(item)
    elif esc == 3:
        lista.mostrar()
    elif esc == 4:
        lista.duplicatas(lista)
    elif esc == 5:
        print('ENCERRANDO PROGRAMA...')
        break 
    else: 
       print('OPÇÃO INVÁLIDA')
