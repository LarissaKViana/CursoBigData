###ATIVIDADE###
# Crie um código que seja capaz de ler e armazenar
# uma sequência de 20 números pares e 20 números ímpares.
# Obs: utilize estruturas de repetição para fechar esse conjunto
# de números.

num_pares=20
num_impar=20

lista_par=[]
lista_impar=[]
contador=0


while contador<num_pares:
  num_digitado=int(input('Informe um número par: '))
  if num_digitado%2==0:
    lista_par.insert(contador,num_digitado)
    contador=contador+1
  else:
    print("O número informado não é Par!")

contador=0

while contador <num_impar:
  num_digitado=int(input('Informe um número impar: '))
  if num_digitado%2!=0:
    lista_impar.insert(contador,num_digitado)
    contador=contador+1
  else:
    print("O número informado não é IMPAR!")          

lista_par.sort()
lista_impar.sort()
print(lista_par)
print(lista_impar)   