# print('Arian')
# x = [1, 2, 3, 4, 5]
# y = [1, 2, 6, 7, 8]
# z = list(filter(lambda a : a in x, y))
# x = [1, 2, 3, 4, 5]
# y = [1, 2, 6, 7, 8]
# z = list(filter(lambda a : a in x, y))
# print(z)
# c = list(set(x) & set(y))
# print(c)
# m = list(filter(lambda x : True if x < 3 else False, x))
# n = list(filter(lambda x : x < 3, x))                       # n adalah versi singkat dari m
# print(n)

# from functools import reduce
# angka = [1, 2, 3, 4]
# w = reduce(lambda x, y : x * y, angka)
# print(w)

# import functools

# command = ""
# started = False
# while True:
#     command = input('>>> ').lower()
#     if command == 'start':
#         if started:
#             print('Car is already started.')
#         else:
#             started = True
#             print('Car started...')
#     elif command == 'stop':
#         if not started == True:
#             print('Car is already stopped.')
#         else:
#             started = False
#             print('Car Stopped.')
#     elif command == 'help':
#         print('''
# start - to start the car
# stop - to stop the car
# exit - to quit the game
#         ''')
#     elif command == 'quit':
#         print('Thank you! see you soon!')
#         break
#     else:
#         print("I'm sorry, I don't understand")

# price = 0
# for item in [10, 20, 30, 40, 50]:
#     price += item

# print(price)

# numbers = [5, 2, 5, 2, 2]
# for x in numbers:
#     output = ''
#     for y in range(x):
#         output += '*'
#     print(output)

# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     print('x' * x_count)


# numbers = [1, 3, 5, 7, 9, 10, 12, 32, 23, 45, 21, 6, 5, 8]
# maxFunc = numbers[0]
# for number in numbers:
#     if number > maxFunc:
#         maxFunc = number
# print(maxFunc)

# #TODO Remove the duplicate algorithm
# numbers = [2, 2, 4, 6, 3, 4, 6, 1, 3, 2]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)


#TODO Make a max function manually
# numbers = [1, 3, 5, 7, 9, 10, 12, 32, 23, 45, 21, 6, 5, 8]
# maxFunc = numbers[0]
# for number in numbers:
#     if number > maxFunc:
#         maxFunc = number
# print(maxFunc)

# def emoji_converter(message):
#     words = message.split(' ')
#     emojis = {
#         ":)" : "😊"
#     }
#     output = ''
#     for word in words:
#         output += emojis.get(word, word) + ' '
#     return output


# message = input('>')
# print(emoji_converter(message))

# class Mammal:
#     def walk(self):
#         print

# class Mobil:
#     warna = 'merah'
#     tahun = 2010


# mobil1 = Mobil()
# print(Mobil)
# print(mobil1)
# print(mobil1.warna)
# print(mobil1.tahun)

# print(mobil1.warn


