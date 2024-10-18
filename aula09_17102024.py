import random

def somar(num1,num2): 
    return f'Resultado da soma : {num1+num2}.'

def subtrair(num1,num2):
      return f'Resultado da subtração: {num1-num2}.'

def multiplicar(num1,num2):
    return f'Resultado da multiplicação: {num1*num2}.'

# def dividir(num1,num2):
#     if num2!=0:
#       return f'Resultado da divisão: {num1/num2:.2f}'
#     else:
#         return 'Divisões por 0 não são permitidas!'

# def doisnum_aleatorios(qtd,numero_minimo,numero_maximo):
#     for i in range(qtd):
#         return random.randint(numero_minimo,numero_maximo)
#TRATAMENTO DE EXCEÇÕES (TRY e EXCEPT)

#Reformulando a função de divisão:
def dividir(num1,num2):
    try:
        resultado=num1/num2
    except ZeroDivisionError:
        print("Erro: não é possível dividir por zero!")
    else:
        print(f"O resultado da divisão é {resultado}.")
    finally:
        print("Operação finalizada.")

#Testando a função reformulada:
dividir(20,2)
dividir(20,0)
dividir(2,5)    

def doisnum_aleatorios(qtd,numero_minimo,numero_maximo):
    return[random.randint(numero_minimo,numero_maximo)for i in range(qtd)]

numeros= doisnum_aleatorios(2,1,1000)
numero1,numero2=numeros[0],numeros[1]
print(f'Numero gerados :{numero1,numero2}')


print(somar(numero1,numero2))
print(subtrair(numero1,numero2))
print(multiplicar(numero1,numero2))
print(dividir(numero1,numero2))

