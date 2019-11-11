# # def fungsi(x):
# #     return x ** 2
# # print(fungsi(2))

# # x = int(input("1: "))
# # y = int(input("2: "))

# # def pangkat(a, b):

# #     z = 1

# #     for i in range(b):
# #         z *= a

# #     return z

# # print(pangkat(x, y))

# a = [1, 2, 3, 4, 5, 6, 7, 8, 10]
# b = []
# c = []

# for i in range(len(a)):
#     i += 1
#     b.append(a[len(a)-i])

# print(b)

# i = 1

# while i <= len(a):
#     c.append(a[len(a)-i])
#     i += 1

# print(c)

# x = "abcdefghijklmnopqrstuvwxyzxyz"
# print(x.count('v'))

# a = (1, 3, 5, 7, 9)
# print(type(a))

# listItem = list(range(1, 11, 2)) ; print(listItem)
# listitem = list(range(1, 33, 3)) ; print(listitem)
# abcd = list(range(1, 32, 2)) ; print(abcd)

# y = 'Nama urut '
# for item in range(1, 11) :
#     print(y + str(item))

# x = {1 : True, 2 : False}
# print(x.items())

# x = ['andi', 'budi', 'caca']
# def tes():
#     print(x[0])
#     print('caca' in x)

# tes()

# def myFunction(x):
#     return lambda a : a ** x            #?penggunaan parameternya adalah X
# pangkat2 = myFunction(2)
# pangkat3 = myFunction(3)
# pangkat5 = myFunction(5)

# print(type(pangkat2))
# print(pangkat2(12))
# print(pangkat3(4))
# print(pangkat5(2))

# z = lambda a : print(a)
# z('Hello')
# print(z('Arian'))
# def y(a) :
#     return len(a)
# a = ['Andilala', 'Budiman', 'Caca']
# x = map(y, a)
# print(x)
# print(list(x))

# a = ['Cokelat', 'Kiwi', 'Melon']
# b = ['Apel', 'Jeruk', 'Nanas']
# def combi (a, b):
#     return a + ' ' + b
# x = map(combi, a, b)                #?fungsinya, sama object yang mau diolahnya
# print(list(x))

# x = range(11)
# def KurangLima(x):
#     if x < 5:
#         return False
#     else:
#         return True

# y = filter(KurangLima, x)           #? returnnya harus boolean
# print(y)
# print(list(y))

z = list(map(pow, [2, 3], [2, 3]))
print(z)

