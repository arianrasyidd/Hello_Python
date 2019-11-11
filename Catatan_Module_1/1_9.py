#Lambda, Map, Filter dan Reduce
Note = '''
Lambda Function adalah function yang gapunya nama (anonymous function)
kita juga bisa menggunakan beberapa parameter ketika menggunakan lambda function
map digunakan untuk mengubah setiap nilai pada list
filter untuk menyaring isi list.
reduce mengubah list menjadi suatu nilai tunggal
'''

#Lambda
# Contoh singkat lambda function ke - 1
x = lambda a : a + 10
# print(type(x))
# print(x(2))

#* kapan kita menggunakan lambda function? ketika kita membutuhkan function 
#* tetapi tidak ingin memanggilnya untuk kedua kali

#contoh ke - 2
y = lambda a, b, c : a + b + c
# print(y(2, 4, 5))


#* bermanfaat untuk membuat function didalam function (menggunakan custom function dengan template function yang sudah ada)

#Contoh penggunaan lambda function di dalam function
def myFunction(x):
    return lambda a : a ** x            #?penggunaan parameternya adalah X
pangkat2 = myFunction(2)
pangkat3 = myFunction(3)
pangkat5 = myFunction(5)

print(type(pangkat2))
print(pangkat2(12))
print(pangkat3(4))
print(pangkat5(2))

#* lambda harus 1 expresion (1 line)
#penggunaan Lambda Function di if / else
x = lambda a : True if a % 2 == 0 else False
print(x(4))

#penggunaan string di lambda
y = lambda a : 'Angka Genap' if a % 2 == 0 else 'Angka Ganjil'
print(y(4))

#penjelasan lambda
z = lambda a : print(a)
z('Hello')
print(z('Arian'))

#Map

#* Contoh singkat
def y(a) :
    return len(a)
a = ['Andilala', 'Budiman', 'Caca']
x = map(y, a)
print(x)
print(list(x))

#Contoh 2 parameter
a = ['Cokelat', 'Kiwi', 'Melon']
b = ['Apel', 'Jeruk', 'Nanas']
def combi (a, b):
    return a + ' ' + b
x = map(combi, a, b)                #?fungsinya, sama object yang mau diolahnya
print(list(x))

#* penggunaan function dengan map dan lambda
# contoh ke - 1
x = [2, 4, 6, 8, 10]
a_result = map(lambda a:a ** 2, x)
print(list(a_result))

#cara ke - 2 cari contoh ke - 1
b = []
for i in x:
    b.append(i ** 2)
print(b)

# cara ke - 3 dari contoh ke - 1
def pangkat2(a):
    return a ** 2
y = map(pangkat2, x)
print(tuple(y))                     #? bisa berbeda2 juga ternyata, ga harus list

# Filter

#* Contoh penggunaan
x = range(11)
def KurangLima(x):
    if x < 5:
        return False
    else:
        return True

y = filter(KurangLima, x)           #? returnnya harus boolean
print(y)
print(list(y))

z = filter(lambda a : True if a >= 5 else False, x)
print(list(z))

m = lambda z : a ** 2, z            #? experiment
print(m)

x = [1, 2, 3, 4, 5]
y = [1, 2, 6, 7, 8]
z = list(filter(lambda a : a in x, y))
print(z)

m = list(filter(lambda x : True if x < 3 else False, x))
n = list(filter(lambda x : x < 3, x))                       # n adalah versi singkat dari m



# map advance level

#* Contoh singkat
z = list(map(pow, [2, 3], [2, 3]))
print(z)


#Reduce
from functools import reduce
angka = [1, 2, 3, 4]
w = reduce(lambda x, y : x * y, angka)
print(w)
 z = red
kata = ['ini', 'ibu', 'budi']
print(''.join(kata))

from functools import reduce
z = reduce(lambda x, y: x + y, kata)
print(z)

test1 = list(map(lambda x : x * 2, filter(lambda x : x > 3, angka))) #? 8 karena dia memfilter dulu sebelum di mapping
print(test1)
test2 = list(filter(lambda x : x > 3, map(lambda x : x * 2, angka))) #? 4, 6, 8 karena dia mapping dulu baru memfilter
print(test2)

nomor = list(range(1, 101))
print(nomor)

step_1 = list(filter(lambda x : True if x % 2 == 0 else False, nomor))
print(step_1)

step_2 = list(map(lambda a : a * 2, step_1))
print(step_2)

from functools import reduce
step_3 = reduce(lambda x, y : x + y, step_2)
print(step_3)

#? bilangan prima dari 0 - 100?
prima = list(range(1, 101))
for i in prima:
    filter(lambda x : True if x == i or x % i else False, prima)
    print(i, prima)

def prima(x):
    a = False
    if x > 1:
        if x == 2: a = True
        else:
            for i in range(2, x):
                if x % i == 0:
                    a = False
                    break
                else:
                    a = True
    else:
        a = False
    return a

print(prima(81))
z = list(filter(prima, range(101)))
print(z)
print(len(z))
