# Distribuição de Chamadas:
'''Imagine um sistema de distribuição de chamadas para atendentes. Implemente uma função que, dadas duas filas (uma de chamadas e outra de atendentes), distribua as chamadas de forma equitativa, retornando a fila de chamadas não atendidas (se houver).'''

class DistribuicaoChamadas:
    def __init__(self):
        self.fila_chamadas = []
        self.fila_atendentes = []

    def enqueue_chamadas(self, chamada):
        self.fila_chamadas.append(chamada)

    def enqueue_atendentes(self, atendente):
        self.fila_atendentes.append(atendente)

    def distribuir(self):
        chamadas_nao_atendidas = []
        while self.fila_chamadas and self.fila_atendentes:
            chamada = self.fila_chamadas.pop(0)
            atendente = self.fila_atendentes.pop(0)
            print(f"Atendendo chamada {chamada} com atendente {atendente}")
            chamadas_nao_atendidas = self.fila_chamadas
        return chamadas_nao_atendidas
    
fila = DistribuicaoChamadas()
while True:
    print('\nESCOLHA O QUE DESEJA FAZER:\n [1]Adicionar chamadas\n [2]Adicionar atendentes\n [3]Distribuir\n [4]Sair')
    esc = int(input())

    if esc == 1:
        chamada = input('QUAL A CHAMADA? ')
        fila.enqueue_chamadas(chamada)
    
    elif esc == 2:
        atendente = input('QUAL O(a) ATENDENTE? ')
        fila.enqueue_atendentes(atendente)

    elif esc == 3:  
        chamadas_nao_atendidas = fila.distribuir()
        print('Chamadas não atendidas:', chamadas_nao_atendidas)

    elif esc == 4:
        print('ENCERRANDO PROGRAMA...')
        break
    
    else:
        print('OPÇÃO INVÁLIDA, por favor escolha dentre as opções listadas.')
