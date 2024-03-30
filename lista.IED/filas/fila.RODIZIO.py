# Rodízio de Pessoas: 
'''Dada uma fila inicial de pessoas, crie uma função que simule um número n de operações de "passar a pessoa da frente para o final da fila". Ao final, mostre a nova configuração da fila.'''

class Rodizio:
    def __init__(self):
        self.fila = []

    def enqueue (self, pessoa):
        self.fila.append(pessoa)
        print('PESSOA ADICIONADA À FILA.')

    def mover (self, n):
        if self.fila:
            for pessoa in range(n):
                temp = self.fila.pop(0)
                self.fila.append(temp)
            return self.fila
        else:
            return False
        
    def mostrar(self):
        print('\nFILA ATUAL:')
        print(self.fila)
        
main = Rodizio()
while True:

    print('\nESCOLHA O QUE DESEJA FAZER:\n [1]Adicionar pessoas na fila\n [2]Mover a primeira pessoa da fila\n [3]Mostrar Lista\n [4]Sair')
    esc = int(input())

    if esc == 1:
        pessoa = input('QUAL A PESSOA QUE DESEJA ADICIONAR? ')
        main.enqueue(pessoa)

    elif esc == 2:
        main.mostrar()
        n = int(input('QUANTAS VEZES DESEJA MOVER A PESSOA? '))
        print('\nFILA:')
        retorno = main.mover(n)
        if retorno != False:
            print(retorno)
        else:
            print('A FILA NÃO EXISTE.')

    elif esc == 3: 
        main.mostrar()

    elif esc == 4:
        print('ENCERRANDO PROGRAMA...')
        break

    else:
        print('OPÇÃO INVÁLIDA, por favor escolha entre as opções listadas.')
