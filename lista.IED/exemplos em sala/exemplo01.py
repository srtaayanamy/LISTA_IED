class Fila:
    def __init__(self):
        self.lista = []

    def enqueue(self, elemento):
        self.lista.append(elemento)

    def dequeue(self):
        self.lista.pop(0)

    def front(self):
        return self.lista[0]

    def is_empty(self):
        if not self.lista:
            return True
        else:
            return False

def processar_chamadas(fila_chamada, fila_atendente):
    if fila_atendente.is_empty():
        print('\nNão existe atendentes...')
    elif fila_chamada.is_empty():
        print('\nNão existe chamadas...')
    else:
        print(f'\nA chamada {fila_chamada.front()} está sendo atendida/processada por {fila_atendente.front()}')
        fila_atendente.dequeue()
        fila_chamada.dequeue()

fila_chamadas = Fila()
fila_atendentes = Fila()

fila_chamadas.enqueue(1)
fila_chamadas.enqueue(2)
fila_chamadas.enqueue(3)

fila_atendentes.enqueue('Gustavo')
fila_atendentes.enqueue('Natan')
fila_atendentes.enqueue('ikes')

processar_chamadas(fila_chamadas, fila_atendentes)
processar_chamadas(fila_chamadas, fila_atendentes)
processar_chamadas(fila_chamadas, fila_atendentes)
