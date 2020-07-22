'''Aula 15 Mundo 02 // Interrompendo repetições while (break)'''






'''
desafio 66
- Ler vários números inteiros pelo teclado. O programa só vai parar quando o 
  usuário digitar '999', que é a condição de parada. No final, mostre quantos
  números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''
# sum = 0
# ct = 0
# while True:
#     num = int(input('Inform a number: '))
#     if num != 999:
#         ct += 1
#         sum += num
#     else:
#         print(f'\nTotal numbers: {ct}')
#         print(f'Sum: {sum}')
#         break



'''
desafio 67
- Elabore um programa que mostre a tabuada de vários números, um de cada vez, para
  cada valor digitado pelo usuário. O programa será interrompido quando o número
  solicitado for negativo.
'''
# while True:
#     num = int(input('Value: '))
#     print()
#     if num > 0:
#         for n in range(1, 11):
#             print(f'{n} X {num} = {num * n}')
#     else:
#         print('\n{:-^30}'.format('Finished Process'))
#         break
#     print('-=' * 30)



'''
desafio 68
- Elabore um programa que jogue 'par ou ímpar' com o usuário. O jogo será interrompido
  quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou
  até o final do jogo.
'''
# import random
# player = str(input('type [even] or [odd]:\t '))
# computer = str
#
# if player == 'even':
#     computer = 'odd'
# elif player == 'odd':
#     computer = 'even'
# ct = 0
# while True:
#     numplayer = random.randint(0, 10)
#     numcomputer = random.randint(0, 10)
#     print(f'\nPlayer number: {numplayer}')
#     print(f'Computer number: {numcomputer}')
#     if (numplayer + numcomputer) % 2 == 0 and player == 'even':
#         print('Player wins\n')
#         ct += 1
#     elif (numplayer + numcomputer) % 2 == 0 and computer == 'even':
#         print('Computer wins')
#         print('-='*15)
#         print(f'Player wins: {ct}')
#         break
#     elif (numplayer + numcomputer) % 2 != 0 and computer == 'odd':
#         print('Computer wins')
#         print('-='*15)
#         print(f'Total wins of the player: {ct}')
#         break
#     elif (numplayer + numcomputer) % 2 != 0 and player == 'odd':
#         print('Player wins\n')
#         ct += 1



'''
desafio 69
- Ler a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
  perguntar se o usuário quer ou não continuar. No final, mostre: 1) Quantos tem mais
  do que 18 anos 2) Quantos homens foram cadastrados 3) Quantas mulheres tem menos de
  20 anos.
'''
# ctage = 0
# ctmale = 0
# ctfemale = 0
# while True:
#     age = int(input('\nInform your age:\t'))
#     gender = str(input('Inform your gender → [M] or [F]:\t')).upper()
#     if age > 18:
#         ctage += 1
#     if gender == 'M':
#         ctmale += 1
#     if gender == 'F' and age < 20:
#         ctfemale += 1
#     option = str(input('\nDo you wanna continue? [Y] or [N]:\t')).upper()
#     if option == 'Y':
#         print()
#     elif option == 'N':
#         print('-='*25)
#         print(f'Above 18: {ctage}')
#         print(f'Mans: {ctmale}')
#         print(f'Women under 20: {ctfemale}')
#         break



'''
desafio 70
- Ler o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
  continuar. No final, mostre: 1) Qual o total gasto na compra 2) Quantos produtos custam
  mais do que R$1000 3) Qual é o nome do produto mais barato.
'''
# sum = productabove = ct = 0
# lowest = 99999
# namelowest = ''
# while True:
#     name = str(input('Name: '))
#     price = float(input(f'Price of {name}: '))
#     ct += 1
#     sum += price
#     if price > 1000:
#         productabove += 1
#     if price < lowest:
#         lowest = price
#         namelowest = name
#     option = ' '
#     while option not in 'YN':
#         option = str(input('\nDo you wanna continue? [Y] or [N]:\t')).strip().upper()[0] #pega somente a 1 letra
#     if option == 'N':
#         break
# print('-'*50)
# print(f'\nTotal: ${sum:.2f}')
# print(f'Products above $1000:\t{productabove:.2f}')
# print(f'Lowest product: {namelowest}, by costing ${lowest:.2f}\n')
# print('{:-^50}'.format('FINISHED PROCESS'))



'''
desafio 71
- Elabore um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte
  qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas
  de cada valor serão entregues. OBS: O caixa possui apenas cédulas de RS50, R$ 20, R$10 e R$1.
'''
# value = int(input('Value: '))
# total = value
# banknote = 50
# totalbanknote = 0
# while True:
#     if total >= banknote:
#         total -= banknote
#         totalbanknote += 1
#     else:
#         if totalbanknote > 0:
#             print(f'Total of bank notes {totalbanknote} of ${banknote}')
#         if banknote == 50:
#             banknote = 20
#         elif banknote == 20:
#             banknote = 10
#         elif banknote == 10:
#             banknote = 1
#
#         totalbanknote = 0
#
#         if total == 0:
#             break