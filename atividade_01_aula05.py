# 5) Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação optativa dos estudantes de uma turma. Caso o estudante 
#não tenha feito a optativa, deve ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa substitui a 
# nota mais baixa entre as duas primeiras avaliações. Escrever a média e mensagens que indiquem se o estudante foi aprovado, reprovado ou se 
# está em exame, de acordo com as informações abaixo: 
# Aprovado: média >= 6.0, Reprovado: média < 3.0, Exame: média >= 3.0 e < 6.0;

N_alunos=int(input('Informe o número de alunos da sua turma :'))

i=0

while i <N_alunos:
 avaliacao_1=float(input('Informe a nota da primeira avaliação: '))
 avaliacao_2=float(input('Informe a nota da segunda avaliação: '))
 avaliacao_optativa=float(input('Informe a nota da avaliação optativa :'))


 if avaliacao_optativa!=-1:
  menor_nota=min(avaliacao_1,avaliacao_2)
 if avaliacao_optativa>menor_nota:
    if avaliacao_1==menor_nota:
       avaliacao_1=avaliacao_optativa
    else:
      avaliacao_2=avaliacao_optativa

 media=(avaliacao_1+avaliacao_2)/2


 if media>=6.0:
   print('A média: ',media,'Aprovado!')
 elif media<3.0:
  print('A média: ',media,'Reprovado')
 else :
  print('A média: ',media,'Exame') 
 
 i=i+1

  
  