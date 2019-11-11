#01 Nov 2019
#Logic Test
#! Bikin translator untuk kode morse

#* membuat bintang (segitiga siku2)
def star(x):
    star = ''
    for i in range(x):
        star += ' * '
        print(star)
    return star


star(5)



#bintang segitiga kebalik
# def rStar(x):
#     star = ''
#     for i in range(x):
#         star = ' * ' * (x-i)
#         print(star)    
        

# rStar(5)


# urutan angka menjadi setengah pyramid
# def nStar(x):
#     star = ''
#     for i in range(x):
#         star += str(i) + ' '
#         print(star)
#     return star

# nStar(20)

# urutan angka menjadi setengah pyramid terbalik
# def rStar(x):
#     star = ''
#     for i in range(x):
#         star = i * str(x-i) + ' '
#         print(star)    
        

# rStar(20)


#urutan angka pyramid dengan jajaran angka
# def aStar(x):
#     star = ''
#     for i in range(x):
#         star = str(i + 1) * (i + 1) + ' '
#         print(star)
#     print('\n')
#     return star

# aStar(9)


# def bStar(x):
#     star = ''
#     for i in range(x):
#         star = str(i + 1) * (x - i) + ' '
#         print(star)
#     print('\n')
#     return star

# bStar(9)

# def cStar(x):
#     star = ''
#     for i in range(x):
#         checkpoint = list(star + str(i + 1) + ' ')
#         type(checkpoint)
#         for y in checkpoint:
#              reversed(checkpoint)
#     return star

# cStar(20)

# Double For Loops
# x = [
#     [1, 2, 3], [4, 5, 6], [7, 8, 9]
# ]

# for i in x:
#     for j in i:
#         print()

# def pangkat(x, y):
#     while x != y:
#         x += 1
#         number = x * x
#     return number

# print(pangkat(3, 6))

# def pangkat(x, y):
#     out = 1
#     for i in range(y):
#         out *= x
#     print(out)

# pangkat(2, 3)

#Rekursif Function
# def pangkatB(x, y):               #? rekursif function adalah menggunakan fungsi (A) di fungsi (A)
#     if (y == 1):              
#         return x
#     else:
#         return x * pangkatB(x, y-1)
# print(pangkatB(2, 3))

'''
#** penjelasan
pangkatB(2, 1) = 2
pangkatB(2, 2) = 2 * pangkatB(2, 1)
pangkatB(2, 3) = 2 * pangkatB(2, 2)
'''

# def nStar(x):
#     star = ''
#     for i in range(x):
#         star += str(i + 1) + ' '
#         for y in star:
#             a = list(star)
#             b = 
#         print(star)
#     return star

# nStar(9)


#jawaban
def faktorial(x):
    angka = 1
    for i in range(1, x + 1):
        angka *= i
    return angka
    
print(faktorial(3))

"--------------------------------------------------------------------------------------------------------------------"

'''
# looping list di dalem list menggunakan
x = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in x:
    for j in i:
        print(j)

for i in range(5):
    for j in range(7,9):
        print(i, 'dan', j)

# bikin function pangkat
def pangkat(x, y):
    k = x
    for i in range(y-1):
        x *= k
    print(x)

pangkat(12, 2)

# bikin function factorial
def faktorial(x):
    angka = 1
    for i in range(1, x+1):
        angka *= i
    print(angka)

faktorial(3)



# REKURSIF FUNCTION
def faktorial2(x):
    if x <= 2:
        return x
    else:
        return x * faktorial2(x-1)      # fungsinya memanggil diri sendiri

print(faktorial2(4))
'''