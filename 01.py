'''Aula 12 Mundo 02 // Condições Aninhadas (if, elif, else; condições juntas)'''

'''
nome = str(input('Digite um nome: '))
if nome == 'Samuel':
    print(f'{nome} é um nome bonito.')
elif nome == 'Hériclys' or nome == 'Pericles':
    print(f'Esse nome é bastante incomum')
elif nome in 'Julia Isabella Maria': #todo nome que for 'julia', ou 'isabella', ou 'maria' cairá nessa condição
    print(f'Belo nome feminino')
print(f'Tenha um bom dia, {nome}!')
'''






'''
desafio 36
- Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai 
  perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor
  da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''
# housevalue = int(input('House value: '))
# salary = int(input('Salary: '))
# months = int(input('How many months: '))
# installment = housevalue / months
# if installment > salary * 0.3:
#     print(f'The installment value exced 30% of your salary.')
# elif installment <= salary * 0.3:
#     print(f'Congrats!! This house is available to buy.')



'''
desafio 37
- Ler um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
  1) para binário 2) para octal e 3) para hexadecimal.
'''
# import random
# number = random.randint(0, 99)
# bin = bin(number)
# oct = oct(number)
# hex = hex(number)
# print(f'Number drawned: {number}\n')
# print('Wich one do you wanna choose: \n'
#       '[1] for binary conversion\n'
#       '[2] for octal conversion\n'
#       '[3] for hexadecimal\n'
#       '[4] all options above\n')
# option = int(input('Inform your option: '))
# if option != 1 and option != 2 and option != 3 and option != 4:
#     print(f'This informed option [{option}] is not valid.')
# elif option == 1:
#     print(f'\nBinary: {bin[2:]}')
# elif option == 2:
#     print((f'\nOctal: {oct[2:]}'))
# elif option == 3:
#     print(f'\nHexadecimal: {hex[2:]}')
# elif option == 4:
#     print(f'\nBinary: {bin[2:]}')
#     print((f'Octal: {oct[2:]}'))
#     print(f'Hexadecimal: {hex[2:]}')



'''
desafio 38
- Ler 2 números inteiros e compare-os, mostrando na tela uma mensagem: 1) O 1º valor é maior 
  2) o 2º valor é maior 3) Não existe nenhum valor maior, os dois são iguais.
'''
# import random
# number1 = random.randint(0, 9)
# number2 = random.randint(0, 9)
# print(f'First number: {number1}')
# print(f'Second number: {number2}\n')
# if number1 > number2:
#     print(f'The first number [{number1}] is greater than the second [{number2}].')
# elif number2 > number1:
#     print(f'The second number [{number2}] is greater than the first [{number1}]')
# else:
#     print(f'The first and second numbers are the same.')


'''
desafio 39
- Ler o ano de nascimento de um jovem e informe, de acordo com sua idade: 1) Se ele vai se alistar ao
  serviço militar 2) Se é a hora de se alistar 3) Se já passou o tempo do alistamento. 
  O programa deverá mostrar também o tempo que falta ou que passou do prazo.
'''
# birthyear = int(input('Inform the year you were born: '))
# year = 2020
# age = year - birthyear
# exced = age - 18
# if birthyear >= year:
#     print('Are you kidding? ')
# elif birthyear < year:
#     if age == 18:
#         print('Congrats, you can enlist youserf to United States Armed Forces.')
#     elif age < 18:
#         print('You do not have to enlist yourself yet. You have to wait a few more years.')
#     else:
#         print(f'The enlist time exceeded {exced} years. Look for a military junta immediately!!')



'''
desafio 40
- Ler 2 notas de um aluno e calcule sua média, mostrando no final uma mensagem, de acordo com sua média
  final: 1) média abaixo de 5: reprovado 2) média igual a 5 e 6.9: recuperação 
  3) média 7 ou superior: aprovado.
'''
# score1 = float(input('Inform your first score: '))
# score2 = float(input('Inform your second score: '))
# average = (score1 + score2) / 2
# if average < 5:
#     print(f'Your average score was {average:.2f}. You failed.')
# elif average >= 5 and average <= 6.9:
#     print(f'Your average score was {average:.2f}. You have to do a substitute test.')
# elif average >= 7 and average <= 10:
#     print(f'Congrats!! You passed the exam.')



'''
desafio 41
- Ler a idade de uma nadador e mostrar sua categoria, de acordo com sua idade: 1) até 9 anos: mirim 
  2) até 14: infantil 3) até 19: junior 4) até 20: senior 5) acima: master
'''
# import random
# age = random.randint(4, 30)
# print(f'Age: {age}\n')
# if age > 20:
#     print(f'Category: Master')
# elif age == 20:
#     print(f'Category: Senior')
# elif age > 14 and age <= 19:
#     print(f'Category: Junior')
# elif age > 9 and age <= 14:
#     print(f'Category: Childish')
# else:
#     print(f'Category: Little')



'''
desafio 42
- Enunciado do ex 35, porém agora mostrando se o triângulo formado é: 1) equilátero 2) isóceles 3) escaleno.
'''
# import random
# side1 = random.randint(1, 10)
# side2 = random.randint(1, 10)
# side3 = random.randint(1, 10)
# if abs(side2-side3) < side1 < side2 + side3 and abs(side1-side3) < side2 < side1 + side3 and abs(side1-side2) < side3 < side1 + side2:
#     print(f'The sides {side1}, {side2} and {side3} can form a triangle.')
#     if side1 == side2 and side1 == side3 or side2 == side1 and side2 == side3:
#         print('Equilateral triangle.')
#     elif side1 == side2 or side1 == side3 or side2 == side3:
#         print('Isosceles triangle.')
#     elif side1 != side2 and side1 != side3 and side2 != side3:
#         print('Scalene triangle.')
# else:
#     print(f'The sides {side1}, {side2} and {side3} can not form a triangle.')



'''
desafio 43
- Ler o peso e a altura de uma pessoa, calcule o seu IMC e mostre seu status: 
  1) abaixo de 18.5: abaixo do peso 2) entre 18.5 e 25: peso ideal 3) entre 25 e 30: sobrepeso 
  4) entre 30 e 40: obesidade 5) acima de 40: obesidade mórbida
'''
# height = float(input('Inform your height in meters: '))
# weight = float(input('Inform your weight in KG: '))
# imc = weight / height**2
# print(f'Your IMC: {imc:.2f}')
# if imc < 18.5:
#     print('underweight')
# elif imc >= 18.5 and imc < 24:
#     print('ideal weight')
# elif imc >= 24 and imc < 30:
#     print('overweight')
# elif imc >= 30 and imc < 40:
#     print('obesity')
# else:
#     print('morbid obesity')



'''
desafio 44
- Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
  condição de pagamento; 1) a vista dinheiro / cheque: 10% de desc 2) a vista cartão: 5% de desc 
  3) em até 2x: preço normal 4) 3x+ no cartao: 20% de juros
'''
# productvalue = float(input('Product value: '))

# print('Options: \n'
#       '[1] in cash or bank check\n'
#       '[2] cash card\n'
#       '[3] up to 2x\n'
#       '[4] up to 3x or more\n')
# paymentmethod = int(input('Inform a payment method: '))

# incash = productvalue * 0.9
# cashcard = productvalue * 0.95
# upto2 = productvalue
# upto3m = productvalue * 1.2

# if paymentmethod == 1:
#     print(f'Amount: {incash:.2f}')
# elif paymentmethod == 2:
#     print(f'Amount: {cashcard:.2f}')
# elif paymentmethod == 3:
#     print(f'Amount: {upto2:.2f}')
# elif paymentmethod == 4:
#     print(f'Amount: {upto3m:.2f}')
# else:
#     print('Invalid option!!')



'''
desafio 45
- Elabora um programa que jogue pedra, papel e tesoura com o usuário.
'''
# import random
# player = random.randint(1, 3)
# computer = random.randint(1, 3)
# if player == computer:
#     if player == 1 and computer == 1:
#         print(f'Tie in the game.\n'
#               f'Player: [Rock] // Computer: [Rock]')
#     elif player == 2 and computer == 2:
#         print(f'Tie in the game.\n'
#               f'Player: [Paper] // Computer: [Paper]')
#     elif player == 3 and computer == 3:
#         print(f'Tie in the game.\n'
#               f'Player: [Scissors] // Computer: [Scissors]')
# elif player == 1 and computer == 3:
#     print(f'Player wins.\n'
#           f'Player: [Rock] // Computer: [Scissors]')
# elif player == 2 and computer == 3:
#     print(f'Computer wins.\n'
#           f'Player: [Paper] // Computer: [Scissors]')
# elif player == 3 and computer == 2:
#     print(f'Player wins.\n'
#           f'Player: [Scissors] // Computer: [Paper]')
# elif player == 3 and computer == 1:
#     print(f'Computer wins.\n'
#           f'Player: [Scissors] // Computer: [Rock]')
# elif player == 2 and computer == 1:
#     print(f'Player wins.\n'
#           f'Player: [Paper] // Computer: [Rock]')
# elif player == 1 and computer == 2:
#     print(f'Computer wins.\n'
#           f'Player: [Rock] // Computer: [Paper]')