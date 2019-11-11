# name = input('what\'s your name? ')
# fav_colour = input('what\'s your favorite colour? ')
# print(f'{name} likes {fav_colour}')

# birth_year = int(input('birth year: '))
# age = 2019 - birth_year ; print(age)

# absen = set(range(1, 28))
# while len(absen) > 0:
#     weight = float(input('what\'s your weight? '))
#     a_result = round(weight * .453592, 2) ; print(f'{a_result} kilograms')
#     break

# course = 'Pyhton\nfor\tBeginners'
# course = course.title().lower() ; print(course)
# print(course.find('n'))
# print(course[0:10:2])
# print(course.replace('o', 'e'))
# print(course.replace('\n',' ').replace('\t', ' ').replace('for', 'FOR').lower().upper())
# print(course)

# import math
# print(math.floor(2.5))
# print(math.factorial(9))    #factorial
# print(math.comb(9, 6))      #combination

# house_price = 1000000
# good_credit = True
# if good_credit:
#     down_payment = ((10 * house_price) // 100)
# else:
#     down_payment = ((20 * house_price) // 100)
# print(f'down payment : ${down_payment}')

# name = 'Muhammad Arian Rasyid Sidiq'
# if len(name) < 3:
#     print('name must be at least 3 characters')
# elif len(name) >= 50:
#     print('name can be maximum of 50 characters')
# else:
#     print(f'your name {name}, looks good!')

# absen = set(range(1, 28))
# while len(absen) > 0:
    # weight = float(input('What is your weight? '))
    # Kg = round(weight * .45359237, 2)
    # Lbs = round(weight * 2.2046226218, 2)
    # if weight > 100:
    #     print(f'Pounds to Kilo : {Kg}')
    # else:
    #     print(f'Kilo to Pounds : {Lbs}')
        # break

# weight = float(input('What is your weight? '))
# if weight > 100:
#     Kg = round(weight * .45359237, 2)
#     print(f'you are {Kg} kilos.')
# else:
#     Lbs = round(weight * 2.2046226218, 2)
#     print(f'you are {Lbs} pounds.')

# weight = float(input('weight : '))
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == 'L':
#     Kg = round(weight * .45, 2)
#     print(f'you are {Kg} kilos.')
# elif unit.upper() == 'K':
#     Lbs = round(weight / .45, 2)
#     print(f'you are {Lbs} pounds.')
# else:
#     print('wrong code! Just type L or K')

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# input("Wanna play some game? Click 1 to start or click 0 to refuse")

#INFINITE LOOPS

# while guess_count < guess_limit:
#     a = input('guess my secret number : ')
#     if a == 9:
#         guess_count += 1
#         print('You Win!')
#     elif guess_count == 1:
#         print('Wrong answer')
#     elif guess_count == 2:
#         print('still wrong')
#     elif guess_count == 3:
#         print('wrong again and you failed!')
#     break

# for x in range(4):
#     for y in range(3):
#         print(f'{x}, {y}')





