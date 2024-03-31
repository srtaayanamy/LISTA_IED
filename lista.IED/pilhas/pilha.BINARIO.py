# Conversão de Decimal para Binário:
'''Utilize uma pilha para converter um número inteiro decimal para binário. Apresente o resultado como uma string.'''

class DecimalParaBinario:
    def __init__(self):
        self.pilha = []
    
    def isEmpty(self):
        return self.pilha == []
    
    def converter(self, numero):
        if numero == 0:
            return "0"
        while numero > 0:
            resto = numero % 2
            numero //= 2
            self.pilha.append(str(resto))

        num_binario = ""
        for digito in reversed(self.pilha):
            num_binario  += digito
        return num_binario

main = DecimalParaBinario()
while True:
    numero = int(input('QUE NUMERO DESEJA CONVERTER PARA BINÁRIO? (Apenas números inteiros)\n'))
    if numero >= 0:
        num_binario = main.converter(numero)
        print("{} EM DECIMAL É IGUAL A {} EM BINÁRIO." .format(numero, num_binario))
    else:
        print("POR FAVOR, INSIRA UM NÚMERO INTEIRO NÃO NEGATIVO.")
