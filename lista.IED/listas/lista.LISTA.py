# Crie uma classe Lista que implemente as seguintes operações básicas: inserção, remoção e busca de um elemento. Além disso, adicione um método para imprimir todos os elementos da lista.

class Lista():
    def __init__(self):
        self.elementos = []

    def inserir(self, elemento):
        self.elementos.append(elemento)
        print('Item adicionado')

    def remover(self, elemento):
        if elemento in self.elementos:
          self.elementos.remove(elemento)
        print('Item removido')

    def busca(self, elemento):
        if elemento in self.elementos:
            return True
        else:
            return False

    def mostrar(self):
        for elemento in self.elementos:
          print('-', elemento)

Lista = Lista()
while True:
  escolha = input('Digite a opção que prefere:\n 1-adicionar;\n 2-remover;\n 3-buscar;\n 4-mostrar;\n 5-sair;\n ')
  if escolha == '1':
      elemento = input('Qual item deseja adicionar? ')
      Lista.inserir(elemento)
  elif escolha == '2':
      elemento = input('Que elemento deseja excluir? ')
      Lista.remover(elemento)
  elif escolha == '3':
      elemento = input('Que elemento deseja buscar? ')
      res = Lista.busca(elemento)
      if res == True:
          print('O elemento está na lista')
      else:
          print ('O elemento não foi encontrado')
  elif escolha == '4':
      Lista.mostrar()
  elif escolha == '5':
      break
  else:
      print('Opção inválida')