# 1) Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um determinado cômodo de uma residência. 
# Dados de entrada: a potência da lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do cômodo. Considere que 
# a potência necessária é de 3 watts por metro quadrado e a cada 3 m² existe um bocal para uma lâmpada;

pot_lamp=int(input('Digite a potência de sua lampada em watts:')) #Potêcia da lampada
largura=float(input('Digite a largura do seu comodo:'))
comprimento=float(input("Digite o comprimento do comodo:"))
area=largura*comprimento

if(pot_lamp>=9):
 total_lamp=area/pot_lamp
 print('Será necessário: ', total_lamp,' Lâmpadas')
else:
 print('Potência da lampada insuficiente,potencia mínima de 9 watts')
