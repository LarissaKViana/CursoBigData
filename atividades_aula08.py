#1) Um pescador precisa pagar uma multa caso o peso dos peixes exceda 100 quilos. Crie uma função para calcular a multa, se aplicável.
# 2) Crie um programa que faça a leitura da altura e do peso de N pessoas para o cálculo do IMC, mostrando ao final a classificação de acordo
# com a tabela de IMC.
#
# 3) Crie funções que mostrem um cardápio de um restaurante (pelo menos 4 itens) e que permitam realizar pedidos e fechar a conta.
#
#1)
# def multa():
#    valor=(peso+(peso* 0.1))/2
#    return valor


# peso=float(input('Digite o valor do peso: '))

# if peso>100 :
#    print(f'O valor da multa é:R$ {multa()}.')
# else:
#    print('O valor do peso atende a norma estabelecida!')   

# 2)

def classificação_IMC():
   
   if valor_imc<18.5:
      print('Magreza')
   elif valor_imc>=18.5 and valor_imc<25:
      print('Normal')
   elif valor_imc>=25 and valor_imc<30:
      print('Sobrepeso')
   elif valor_imc>=30 and valor_imc<40:
      print('Obesidade')
   elif valor_imc>=40:
      print('Obesidade Grave')

peso=float(input('Informe o seu peso kg: '))
altura=float(input('Informe sua altura (metros): '))

valor_imc=peso/(altura*altura)

classificação_IMC()