num_cadidatos=2
contador=1
while contador<=num_cadidatos:

 idade=int(input('Informe sua idade: '))

 if idade>=18:
  print(f'Candidato número: {contador}')
  nome=input('Digite seu nome completo:')
  dt_nasc=input('Informe sua data de nascimento: ')
  telefone=(input("digite seu telefone: "))
  e_mail=input('Informe eu endereço de E-mail: ')
  formacao=input('Qual sua formação acadêmica: ')
  experiencia=input('Informe sobre suas últimas experiências profissionais: ')
  contador=contador+1
 else:
  print('Para se candidatar a uma vaga é necessário ter no mínimo 18 anos!')
  