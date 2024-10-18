num_cadidatos=[]
contador=1
while contador<=num_cadidatos:
 nome=input('Digite seu nome completo:')
 idade=int(input('Informe sua idade: '))

 if idade<18:
   print('Para se candidatar a uma vaga é necessário ter no mínimo 18 anos!')
 else:
  print(f'Candidato número: {contador}')
  dt_nasc=input('Informe sua data de nascimento: ')
  telefone=(input("digite seu telefone: "))
  e_mail=input('Informe eu endereço de E-mail: ')
  formacao=input('Qual sua formação acadêmica: ')
  experiencia=input('Informe sobre suas últimas experiências profissionais: ')

  num_cadidatos.append({
        'nome':nome,
        'idade':idade,
        'dt_nasc':dt_nasc,
        'telefone':telefone,
        'email':e_mail,
        'formacao':formacao,
        'experiencia':experiencia
  })
  contador=contador+1  
  