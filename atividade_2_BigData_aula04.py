#  2) Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, largura e altura), calcular e escrever a quantidade de 
# caixas de azulejos para se colocar em todas as suas paredes (considere que não será descontada a área ocupada por portas e janelas). Cada caixa 
# de azulejos possui 1,5 m²;

comprimento=float(input("Digite o comprimento da cozinha:"))
largura=float(input('Digite a largura da cozinha:'))
altura=float(input('Digite a altura da cozinha: '))
azulejos=1.5

area_1=(comprimento*altura)*2
area_2=(largura*altura)*2
area_total=area_1+area_2

total_azulejos=area_total/azulejos

print('Serão necessárias :',total_azulejos,' caixas de azulejos')