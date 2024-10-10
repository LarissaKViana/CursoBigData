# 3) Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do combustível é de R$ 4,87, escreva um 
# programa para ler: a marcação do odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de combustível gasto e o 
# valor total (R$) recebido dos passageiros. Calcular e escrever: a média do consumo em km/L e o lucro (líquido) do dia;

preco_combustivel=4.87

inicio_dia=float(input('Informe o número  odômetro (km) do inicio do dia: '))
fim_dia=float(input('Infoeme o número  odômetro (km) do fim do dia: '))
combustivel=float(input('informe o total de combustível gasto (litros): '))
total_bruto=float(input('Informe o total arrecadado(r$): '))

total_combustivel=combustivel*preco_combustivel
total_km=fim_dia-inicio_dia
media=combustivel/total_km
total_liquido=total_bruto-total_combustivel

print('A média de consumo por km/l: ',media)
print('O lucro líquido do dia: R$',total_liquido)