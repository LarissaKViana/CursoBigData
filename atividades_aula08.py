#1) Um pescador precisa pagar uma multa caso o peso dos peixes exceda 100 quilos. Crie uma função para calcular a multa, se aplicável.

def multa():
   valor=(peso+(peso* 0.1))/2
   return valor


peso=float(input('Digite o valor do peso: '))

if peso>100 :
   print(f'O valor da multa é:R$ {multa()}.')
else:
   print('O valor do peso atende a norma estabelecida!')   