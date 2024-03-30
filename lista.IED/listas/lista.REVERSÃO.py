# Reversão de Lista: 
'''Escreva uma função que receba uma lista e reverta a ordem de seus elementos, sem criar uma nova lista.'''

class Lista:
    def __init__(self):
        self.list = []

    def inserir(self, elemento):
        self.list.append(elemento)

    def remover(self, elemento):
        if elemento in self.list:
            self.list.remove(elemento)
            print(f'ELEMENTO {elemento} REMOVIDO DA LISTA')

        else:
            print('ELEMENTO NÃO ENCONTRADO.')

    def inverter(self):
        self.list.reverse()
        print(self.list)

main = Lista()
while True:
    esc = int(input('ESCOLHA:\n [1]Adicionar na lista\n [2]Remover da lista\n [3]Inverter\n [4]Sair\n'))

    if esc == 1:
        elemento = input('QUAL ITEM DESEJA ADICIONAR?\n')
        main.inserir(elemento)
        print(f'ELEMENTO {elemento} ADICIONADO A LISTA')

    elif esc == 2:
        elemento = input('QUAL ITEM DESEJA REMOVER?\n')
        main.remover(elemento)

    elif esc == 3:
        main.inverter()

    elif esc == 4:
        print('ENCERRANDO O PROGRAMA...')
        break

    else:
        print('OPÇÃO INVÁLIDA')
