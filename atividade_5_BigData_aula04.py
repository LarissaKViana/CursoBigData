# 5) Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação optativa dos estudantes de uma turma. Caso o estudante 
#não tenha feito a optativa, deve ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa substitui a 
# nota mais baixa entre as duas primeiras avaliações. Escrever a média e mensagens que indiquem se o estudante foi aprovado, reprovado ou se 
# está em exame, de acordo com as informações abaixo: 
# Aprovado: média >= 6.0, Reprovado: média < 3.0, Exame: média >= 3.0 e < 6.0;

avaliacao_1=float(input('Informe a nota da primeira avaliação:'))
avaliacao_2=float(input('Informe a nota da segunda avaliação:'))
optativa=int(input('O aluno realizou a prova optativa? (Sim=1/Não=0)'))

if optativa==1:
 avaliacao_optativa=float(input('Informe a nota da avaliação optativa :'))
 if avaliacao_1<avaliacao_2:
   media=(avaliacao_optativa+avaliacao_2)/2
 else:
   media=(avaliacao_optativa+avaliacao_1)/2
elif optativa==0:
 avaliacao_optativa=-1
 media=(avaliacao_1+avaliacao_2)/2
else:
  print('Por favor,informe uma opção válida!')
 

if media>=6.0:
   print('A média: ',media,'Aprovado!')
elif media<3.0:
  print('A média: ',media,'Reprovado')
else :
  print('A média: ',media,'Exame') 