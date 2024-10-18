# FOR: sabemos a quantidade de vezes que o laço de repetição foi executado.

for i in range(5):
    numero=int(input('Digite um número:'))
    print(f'Dobro:{numero*2}')

# WHILE: queremos a repetição quando a condição for verdadeira.

contador=0
while True:
    numero=int(input('Digite um número:'))
    print(f'Triplo:{numero*3}')
    contador=contador+1

