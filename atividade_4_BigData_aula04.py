# 4) Escreva um programa que leia o código de origem de um produto e imprima na tela a região de sua procedência, conforme a tabela que foi passada:

codigo=int(input('Por favor informe o código de origem do produto: '))

if codigo==1:
 print('Região Sul')
elif codigo==2: 
 print('Região Norte')
elif codigo==3:
 print('Região Leste')
elif codigo==4: 
 print('Região Oeste')
elif codigo==5: 
 print('Região Nordeste')
elif codigo==6: 
 print('Região Nordeste')
elif codigo==7: 
 print('Região Sudeste')
elif codigo==8:  
 print('Região Sudeste')
elif codigo==9: 
 print('Região Sudeste')
elif codigo==10: 
 print('Região Centro-oeste')
elif codigo==11: 
 print('Região Noroeste')
else:
 print('Por favor infome um código de 1 ao 11; ') 
 codigo=int(input('Por favor informe o código de origem do produto: '))