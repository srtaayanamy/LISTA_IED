# Sistema de Gerenciamento de Tarefas de Impressão

class Fila:
    def __init__(self):
        self.fila = []

    def enqueue(self, tarefa):
        self.fila.append(tarefa)

    def dequeue(self):
        if not self.is_empty():
            return self.fila.pop(0)

    def is_empty(self):
        return not self.fila

    def mostrar(self):
        return self.fila

class Pilha:
    def __init__(self):
        self.tarefas = []

    def is_empty(self):
        return not self.tarefas

    def push(self, tarefa):
        self.tarefas.append(tarefa)

    def pop(self):
        if not self.is_empty():
            return self.tarefas.pop()

    def peek(self):
        if not self.is_empty():
            return self.tarefas[-1]

    def size(self):
        return len(self.tarefas)

fila_alta = Fila()
fila_media = Fila()
fila_baixa = Fila()
fila_processo = Fila()
pilha_cancelamento = Pilha()

def adicionar_tarefa(tarefa, prioridade):
    if prioridade == 1:
        fila_alta.enqueue(tarefa)
    elif prioridade == 2:
        fila_media.enqueue(tarefa)
    elif prioridade == 3:
        fila_baixa.enqueue(tarefa)

def cancelar_tarefa(fila, item):
    if item in fila.mostrar():
        fila.fila.remove(item)
        pilha_cancelamento.push(item)
        print("Tarefa cancelada:", item)
    else:
        print("Tarefa não encontrada na fila")

def processar_tarefa():
    if not fila_alta.is_empty():
        tarefa = fila_alta.dequeue()
        print("Processando tarefa de alta prioridade:", tarefa)
    elif not fila_media.is_empty():
        tarefa = fila_media.dequeue()
        print("Processando tarefa de média prioridade:", tarefa)
    elif not fila_baixa.is_empty():
        tarefa = fila_baixa.dequeue()
        print("Processando tarefa de baixa prioridade:", tarefa)
    else:
        print("Nenhuma tarefa na fila para processar")

while True:
    print('ESCOLHA:\n [1]Adicionar tarefa\n [2]Remover tarefa\n [3]Processar tarefa\n [4]Sair\n')
    opc = int(input("Escolha uma opção: "))

    if opc == 1:
        tarefa = input("Informe a tarefa: ")
        prioridade = int(input("Defina a prioridade da tarefa (1-Alta, 2-Média, 3-Baixa): "))
        adicionar_tarefa(tarefa, prioridade)
    
    elif opc == 2:
        prioridade = int(input("Qual a prioridade da tarefa que deseja cancelar? (1-Alta, 2-Média, 3-Baixa): "))
        item = input("Informe a tarefa que deseja cancelar: ")
        if prioridade == 1:
            cancelar_tarefa(fila_alta, item)
        elif prioridade == 2:
            cancelar_tarefa(fila_media, item)
        elif prioridade == 3:
            cancelar_tarefa(fila_baixa, item)
    
    elif opc == 3:
        processar_tarefa()
    
    elif opc == 4:
        print('ENCERRANDO PROGRAMA...')
        break

    else:
        print('OPÇÃO INVÁLIDA, escolha dentre as opções listadas.')
