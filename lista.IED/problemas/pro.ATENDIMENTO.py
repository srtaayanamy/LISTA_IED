# Gerenciador de Atendimento ao Cliente

class Fila:
    def __init__(self):
        self.fila = []

    def enqueue(self, item):
        self.fila.append(item)

    def dequeue(self):
        return self.fila.pop(0)

    def isEmpty(self):
        if not self.fila:
            return True
        else:
            return False

    def mostrar(self):
        if self.fila:
            return self.fila

    def front(self):
        return self.fila[0]

    def esvaziar(self):
        for i in range(len(self.fila)):
            self.fila.pop()

class Pilha:

    def __init__(self):
        self.pilha = []

    def push(self, item):
        self.pilha.append(item)

    def pop(self):
        self.pilha.pop()

    def is_empty(self):
        if not self.pilha:
            return True
        else:
            return False

    def base(self):
        return self.pilha[0]

    def processo(self):
        self.pop()

p_urgente = Pilha()
p_normal = Pilha()
fila_main = Fila()

def adicionar_solicitação(item, nivel_urgencia):
    if nivel_urgencia == 1:
        p_urgente.push(item)
    elif nivel_urgencia == 2:
        p_normal.push(item)
    else:
        print('OPÇÃO INVÁLIDA.')

def processar(p_urgente, p_normal):
    for n in range(len(p_urgente.pilha)):
        fila_main.enqueue(p_urgente.pilha[n])
    for n in range(len(p_normal.pilha)):
        fila_main.enqueue(p_normal.pilha[n])
    return fila_main.mostrar()

def remover(item, nivel):
    if nivel == 1:
        p_urgente.pilha.remove(item)
    elif nivel == 2:
        p_normal.pilha.remove(item)

while True:

    print('ESCOLHA O QUE DESEJA FAZER:\n [1]Adicionar solicitação\n [2]Atender solicitação\n [3]Cancelar solicitção\n [4]Consultar próxima solicitação\n [5]Sair\n')
    esc = int(input())

    if esc == 1:
        item = input('QUAL A SOLICITAÇÃO?\n')
        nivel_urgencia = int(input('QUAL O NÍVEL DE URGÊNCIA?\n [1]Urgente\n [2]Normal\n'))
        adicionar_solicitação(item, nivel_urgencia)

    elif esc == 2:
        print('FILA A SER PROCESSADA:\n')
        print(processar(p_urgente, p_normal))
        fila_main.esvaziar()
        print('FILA JÁ PROCESSADA:\n')
        if p_urgente.is_empty():
            p_normal.processo()
        else:
            p_urgente.processo()
        print(processar(p_urgente, p_normal))
        fila_main.esvaziar()

    elif esc == 3:
        print("QUAL SOLICITAÇÃO DESEJA REMOVER?\n")
        item = input()
        print("QUAL É A URGÊNCIA DESSA SOLICITAÇÃO?\n")
        print("[1]Urgente\n [2]Normal\n")
        nivel = int(input())
        remover(item, nivel)

    elif esc == 4:
        if p_urgente.is_empty():
            print("O PRÓXIMO ITEM QUE VAI SER PROCESSADO É: ")
            print(p_normal.base())
        else:
            print("O PRÓXIMO ITEM QUE VAI SER PROCESSADO É: ")
            print(p_urgente.base())

    elif esc == 5:
        print('ENCERRANDO PROGRAMA...')
        break

    else:
        print('OPÇÃO INVÁLIDA, escolha dentre as opções listadas.')
