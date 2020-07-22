'''Aula 13 Mundo 02 // Estrutura de repetição for'''






'''
desafio 46
- Elabore um programa que mostre na tela uma contagem regressiva para o estouro de fogos de 
  artifício, indo de 10 até 0 com uma pausa de 1 segundo entre eles.
'''
# import time
# for n in range (10, 0, -1):
#     print(n, end='...')
#     time.sleep(1)
# print('\nFeliz ano novo!!')



'''
desafio 47
- Elabore um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''
# for n in range(1, 50):
#     if n % 2 == 0:
#         print(n)



'''
desafio 48
- Elabora um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e 
  que se encontra no intervalor entre 1 e 500.
'''
# for n in range(1, 500):
#     if n % 3 == 0 and n % 2 != 0:
#         print(n)



'''
desafio 49
- Elabore um programa que mostre a tabuada do número digitado pelo usuário, porém agora 
  com a estrutura FOR.
'''
# num = int(input('Informe o número que deseja: '))
# ct = 0
# for n in range (0, 11):
#     print(f'{num} X {ct} = {num * ct}')
#     ct += 1



'''
desafio 50
- Ler 6 números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado 
  for ímpar, desconsidere-o.
'''
# import random
# import time
# ct = 1
# sum = 0
# ct1 = 0
# for n in range(0, 3):
#     ct1 = 0
#     sum = 0
#     for i in range(0, 6):
#         num = random.randint(0, 10)
#         ct1 += 1
#         if ct1 == 1:
#             print('')
#         print(f'{ct1}º valor do {ct}º sorteio: [{num}]\n')
#         if num % 2 == 0:
#             sum += num
#     ct += 1
#     time.sleep(1)
#
#     print(f'\nSum of the pair numbers drawned: {sum}\n')
#     print('=-'*20)
#     print('=-'*20)



'''
desafio 51
- Ler o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''
# import random
# q = random.randint(2, 5)
# first = random.randint(0, 100)
# print(f'[q] value: {q}\n')
# ct = 1
# for i in range(first, 150, q):
#     if ct <= 10:
#         print(f'{ct}º value: {i}')
#         ct += 1



'''
desafio 52
- Ler um número inteiro e diga se ele é ou não um número primo.
'''
# import random
# num = random.randint(0, 20)
# ct = 0
# for n in range(1, num +1):
#     if num % n == 0: #num / n
#         print('\033[33m', end=' ')
#         ct += 1
#     else:
#         print('\033[31m', end=' ')
#     print(f'{n}', end='')
# print(f'\n\033[mO número {num} foi divisível {ct} vezes.')
# if ct == 2:
#     print(f'\nO número {num} é primo.')
# else:
#     print(f'\nO número {num} não é primo.')



'''
desafio 53
- Ler uma frase qualquer e informe se essa frase é um palíndromo, desconsiderando os espaços
  ex: apos a sopa, a sacada da casa, a torre da derrota...
'''
# phrase = str(input('Inform a phrase: ')).strip().upper()
# words = phrase.split()
# together = ''.join(words)
# reverse = ''
# for letter in range(len(together) - 1, -1, -1):
#     reverse += together[letter]
#
# if reverse == together:
#     print(f'\nThis phrase: [{phrase}] is a palindrome\n')
# else:
#     print(f'\nThis phrase: [{phrase}] is not a palindrome\n')



'''
desafio 54
- Ler o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
  a maioridade e quantas já são maiores de idade.
'''
# ct = 0
# ct1 = 0
# for n in range(0, 6):
#     age = int(input('How old are you? '))
#     if age < 18:
#         ct += 1
#     elif age >= 18:
#         ct1 += 1
# print(f'Above 18: {ct1}')
# print(f'Below 18: {ct}')



'''
desafio 55
- Ler o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''
# highestweight = 0
# lowestweight = 99999
# for n in range(1, 6):
#     weight = float(input(f'Inform the weight of the {n}º person: '))
#     if weight > highestweight:
#         highestweight = weight
#     if weight < lowestweight:
#         lowestweight = weight
# print(f'\nHighest weight so far: {highestweight}Kg')
# print(f'Lowest weight so far: {lowestweight}Kg')



'''
desafio 56
- Ler o nome, idade e sexo de 4 pessoas. No final, mostre: 1) A média da idade do grupo 
  2) qual o homem mais velho 3) quantas mulheres tem menos que 20 anos
'''
# import math
# sumage = 0
# oldman = 0
# ct = 0
# for n in range(0, 4):
#     age = int(input('Inform your age: '))
#     sumage += age
#     gender = str(input('Inform your gender: [M] / [F]\t')).upper()
#     if gender != 'M' and gender != 'F':
#         gender = str(input('Inform your gender correctly, please: [M] / [F]')).upper()
#     elif gender == 'F':
#         if age < 20:
#             ct += 1
#     if gender == 'M':
#         if age > oldman:
#             oldman = age
# average = sumage / 4
# print(f'\n{ct} woman(s) are under 20.')
# print(f'The oldest man in the group is {oldman} years old.')
# print(f'The average age of this group is {math.trunc(average)} years old')