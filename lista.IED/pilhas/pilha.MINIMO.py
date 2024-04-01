# Mínimo na Pilha:
'''Modifique a estrutura de Pilha para que ela suporte uma operação adicional min(), que retorna o menor elemento presente na pilha em tempo constante.'''

class StackMinimo:
    def __init__(self):
        self.itens = []
        self.minimos = []

    def push(self, item):
        self.itens.append(item)
        if not self.minimos or item <= self.minimos[-1]:
            self.minimos.append(item)

    def vazia(self):
        return self.itens == []

    def min(self):
        if self.vazia():
            return None
        return self.minimos[-1]

pilha = StackMinimo()

while True:
    print('\nESCOLHA O QUE DESEJA FAZER:\n [1]Empilhar\n [2]Menor elemento\n [3]Sair\n')
    esc = int(input())

    if esc == 1:
        item = int(input('DIGITE O NÚMERO QUE DESEJA EMPILHAR: '))
        pilha.push(item)
    
    elif esc == 2:
        menor_elemento = pilha.min()
        if menor_elemento is not None:
            print("O MENOR ELEMENTO NA PILHA É:", menor_elemento)
        else:
            print("A PILHA ESTÁ VAZIA.")
    
    elif esc == 3:
        print('ENCERRANDO PROGRAMA...')
        break

    else:
        print('OPÇÃO INVÁLIDA, por favor, escolha dentre as opções listadas.')
