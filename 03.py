'''Aula 14 Mundo 02 // Estrutura de repetição while'''





'''
desafio 57
- Ler o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça
  a digitação novamente até o valor estar correto.
'''
# ct = 1
# while ct <= 5:
#     gender = str(input('Inform your gender: ')).upper()
#     if gender != 'M' and gender != 'F':
#         print('Inform your gender correctly, please!!!\n')
#     else:
#         print(f'\nThe {ct}º person is {gender}')
#         ct += 1



'''
desafio 58
- Melhore o programa do exercício 28 onde o computador vai pensar em um número de 0 a 10.
  Só que agora o jogador vai adivinhar até acertar, mostrando no final quantos palpites
  foram dados para vencer.
'''
# import random
# num = random.randint(0, 10)
# num1 = int(input('Inform a number between 0 and 10: '))
# while num != num1:
#     print('Not yet\n')
#     num1 = int(input('Inform a number between 0 and 10: '))
# print(f'Assorted number: {num}')
# print('Congrats, you guessed the number!')



'''
desafio 59
- Ler 2 números e mostre um menu na tela: 1) somar 2) multiplicar 3) maior 4) novos números
  5) sair do programa. O programa deverá realizar a operação solicitada em cada caso.
'''
# num = int(input('Inform the first number: '))
# num1 = int(input('Inform the second number: '))
# while num != -1 and num1 != -1:
#     print('Select an option: \n'
#           '[1] add numbers\n'
#           '[2] multiply numbers\n'
#           '[3] check which is the biggest number\n'
#           '[4] other numbers\n'
#           '[5] quit program\n')
#     option = int(input('Inform an option: '))
#     if option == 1:
#         sum = num + num1
#         print(f'{num} + {num1} = {sum}')
#     elif option == 2:
#         mult = num * num1
#         print(f'{num} X {num1} = {mult}')
#     elif option == 3:
#         if num > num1:
#             print(f'[{num} > {num1}]')
#         else:
#             print(f'[{num1} > {num}]')
#     elif option == 4:
#         num = int(input('Inform the another first number: '))
#         num1 = int(input('Inform the another second number: '))
#     elif option == 5:
#         num = -1
#         num1 = -1
#     else:
#         print('Select a correct option!!!')
# print('\nSee you')



'''
desafio 60 // ASSISTIR A VIDEO AULA DO EXERCICIO
- Ler um número e mostre seu fatorial.
'''
# from math import factorial
# num = int(input('Inform a number: '))
# print(f'The factorial of {num} is {factorial(num)}')



'''
desafio 61
- Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
  termos da progressão usando while.
'''
# import random
# a1 = int(input('Inform the first term: '))
# q = random.randint(2, 5)
# ct = 1
# while ct < 11:
#     print(f'{ct}º term: {a1}')
#     a1 += q
#     ct += 1



'''
desafio 62
- Melhore o desafio 61, perguntando pro usuário se ele quer mostrar mais alguns termos. O programa
  encerra quando ele disser que quer mostrar '0 termos'.
'''
# import random
# a1 = int(input('Inform the first term: '))
# q = random.randint(2, 5)
# ct = 1
# while ct < 11:
#     print(f'{ct}º term: {a1}')
#     a1 += q
#     ct += 1
# print()
# option = str(input('Do you wanna continue? [Y] / [N]\t')).upper()
# if option == 'Y' or option == 'N':
#     if option == 'Y':
#         ct1 = 11
#         option1 = int(input('Inform how many more terms do you wanna see: '))
#         print()
#         while ct1 < ct + option1:
#             print(f'{ct1}º term: {a1}')
#             a1 += q
#             ct1 += 1
#     elif option == 'N':
#         print('See you')



'''
desafio 63
- Ler um número 'n' inteiro qualquer e mostre na tela os 'n' primeiros elementos de uma sequencia de
  Fibonacci. ex: 0 → 1 → 1 → 2 → 3 → 5 → 8 → 13...
'''
# term1 = 0
# term2 = 1
# ct = 3
# terms = int(input('How many terms do you want? '))
# print(f'[{term1}] → [{term2}]', end='')
# while ct <= terms:
#     term3 = term1 + term2
#     term1 = term2
#     term2 = term3
#     ct += 1
#     print(f' → [{term3}]', end='')




'''
desafio 64
- Ler vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
  '999', que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a 
  soma entre eles (desconsiderando o flag).
'''
# num = int(input('Inform a number: '))
# sum = num + 0
# ct = 1
# if num != 999:
#     while num != 999:
#         num = int(input('Inform a number: '))
#         if num != 999:
#             sum += num
#             ct += 1
#         else:
#             print(f'\nSum: {sum}'
#                   f'\nTotal numbers: {ct}')
# else:
#     print('Finished process')



'''
desafio 65
- Ler vários números inteiros pelo teclado. No final da execução, mostre a média de todos os números,
  qual o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar
  a digitar valores.
'''
# import random
# sum = 0
# ct = 0
# hvalue = 0
# lvalue = 9999
# num = 0
# average = float
# while num != 999:
#     option = str(input('Inform an option to start/continue: [Y] / [N]\t')).upper()
#     if option == 'Y':
#         num = random.randint(0, 100)
#         print(f'Assorted number: {num}\n')
#         sum += num
#         ct += 1
#         average = sum / ct
#         if num > hvalue:
#             hvalue = num
#         if num < lvalue:
#             lvalue = num
#     elif option == 'N':
#         num = 999
#         print(f'Highest: {hvalue}')
#         print(f'Lowest: {lvalue}')
#         print(f'Average: {average:.2f}')
#         print(f'\nFinished process')