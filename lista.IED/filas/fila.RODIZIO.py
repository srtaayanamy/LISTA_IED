# Dada uma fila inicial de pessoas, crie uma função que simule um número n de operações de "passar a pessoa da frente para o final da fila". Ao final, mostre a nova configuração da fila.

class Rodizio:

    def __init__(self):
        self.fila = []
    def inserir(self, pessoa):
        self.fila.append(pessoa)
    def mover(self, n):
        if self.fila:
            for pessoa in range(n):
                temp = self.fila.pop(0)
                self.fila.append(temp)
            return self.fila
        else:
            return False

fila = Rodizio()
while True:

    print('O que deseja fazer?\n1-Inserir pessoa;\n2-Passar pessoa para o final;\n3-Sair\n')
    esc = int(input())

    if esc == 1:
        pessoa = input('Digite a pessoa: ')
        fila.inserir(pessoa)
        print('O cliente foi adicionado na fila.')
    elif esc == 2:
        n = int(input('Quantas vezes?'))
        retorno = fila.mover(n)
        if retorno != False:
            print(retorno)
        else:
            print('Não tem fila')  
    elif esc == 3:
        break
    else: 
        print('Essa opção não existe')


