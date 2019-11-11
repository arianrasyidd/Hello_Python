'''
Tugas
1. bikin Fibonnaci
2. bikin fungsi yang ngerubah huruf besar jadi kecil dan huruf kecil jadi besar
3. fungsi cek sudut antara 2 sisi
4. membalik 90 derajat sebuah list
'''

#* Soal No.1
'''
cara no 2
pake for loops
pake if else
pake while loops
'''
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946
def fibo(urutan):
    if urutan < 2:
        return urutan
    else:
        return fibo(urutan - 1) + fibo(urutan - 2)

# print(fibo(6))
class Fibo:
    def fibo(self, urutan):
        if urutan < 2:
            return urutan
        else:
            return self.fibo(urutan - 1) + self.fibo(urutan - 2)

Fibo = Fibo()
print(Fibo.fibo(1))
print(Fibo.fibo(6))
print(Fibo.fibo(10))



# fibonn = int(input("Berapa angka Fibonnaci? "))
# x = list(range(0, fibonn + 1))
# def fiboNumbers(x):
#     for a in x:
#         a = (x.index(a - 2) + x.index(a - 1))
#     return a

# print(fiboNumbers())



#* Soal nomor 2
"""
cara pertama pake for, if, else
cara kedua pake irisan
cara ketiga pake map, filter, lambda
"""
# x = 'AbcdEFgHizZSeqU4321'
# y = []
# w = ''
# def balik():
#     for a in list(x):
#         if a == a.upper():
#             z = a.lower()
#             y.append(z)
#             continue
#         else:
#             c = a.upper()
#             y.append(c)
#     return w.join(y)

# print(balik())

#! percobaan kedua
# y = set(x)
# z = y.copy()
# print(z & y)
# def balik():

#! Percobaan pertama
# def balik():
#     for a in list(x):
#         if a == :
#             y.append(a)
#         else:
#             z.append(a)
#     return y,z


# print(balik())


#* Soal No.3
pass

#* Soal No.4
