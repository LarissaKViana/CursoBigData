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

#3) Crie funções que mostrem um cardápio de um restaurante (pelo menos 4 itens) e que permitam realizar pedidos e fechar a conta.
i=1
j=1
itens_pedido=[]
valor_itens=[]

def cardapio():
   lista_bebidas={'Suco':9,
                  'Refrigerante':10,
                  'Água':3,
                  'Garavita':3}
   
   lista_comidas={'Salgado frito':8,
                  'Salgado Assado':7,
                  'Pedaco de Torta':9,
                  'Misto Quente':7
                  }

   print(f'Lista de bebidas:{lista_bebidas}')
   print(f'Comidas: {lista_comidas}')
cardapio()

def pedido():
   op_bebidas={1:'Suco',
               2:'Refrigerante',
               3:'Água',
               4:'Garavita',
               5:'Sem bebida'}
   op_comidas={1:'Salgado frito',
               2:'Salgado Assado',
               3:'Pedaco de Torta',
               4:'Misto Quente',
               5: 'Sem comida'}
   
   num_bebidas=int(input(f'Informe a quantidade de bebidas que deseja: '))
  
   for i in range(num_bebidas):
     bebidas=int(input(f'Informe o número da bebida que deseja pedir : {op_bebidas}'))

     if bebidas==1:
       itens_pedido.append('Suco')
       valor_itens.append(9)
       
      
     elif bebidas==2:
       itens_pedido.append('Refrigerante')
       valor_itens.append(10)
       
     elif bebidas==3:
       itens_pedido.append('Água')
       valor_itens.append(3)
      
     elif bebidas==4:
       itens_pedido.append('Garavita')
       valor_itens.append(3)
       
     elif bebidas==5:
       print('Pedido sem bebida.')
     else:
       print('Infome uma opção válida!')
       i-=1

   num_comidas=int(input('Informe a quantidade de comida que deseja:'))
     
   for j in range(num_comidas):
      
     comida=int(input(f'Informe o número da bebida que deseja pedir :{op_comidas}'))

     if comida==1:
       itens_pedido.append('Salgado frito')
       valor_itens.append(8)
       
     elif comida==2:
       itens_pedido.append('Salgado Assado')
       valor_itens.append(7)
       
     elif comida==3:
       itens_pedido.append('Pedaço de Torta')
       valor_itens.append(9)
       
     elif comida==4:
       itens_pedido.append('Misto Quente')
       valor_itens.append(7)
       
     elif comida==5:
       print('Pedido sem Comida.')
            
     else:
       print('Infome uma opção válida!')
       j-=1
    
   return print(itens_pedido,valor_itens)
   
pedido()

def fechar_conta():
    valor_total_pedido= sum(valor_itens)
    print(f'Os itens do pedido:{itens_pedido}')
    print(f'Os Valores de cada item são respectivamente: {valor_itens}')
    print(f'O valor total da conta é : R${valor_total_pedido}')
  
fechar_conta()
