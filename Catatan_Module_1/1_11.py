#Class
#* Inheritance
class Manusia:
    def __init__(self, nama):
        self.nama = nama

class Pria(Manusia):
    def __init__(self, nama):
        Manusia.__init__(self, nama)
        self.gender = 'Laki - laki'

objA = Manusia('Andi')
objB = Pria('Andi')
print(vars(objA))
print(vars(objB))

#* Multilevel Inherite
class X:
    def __init__(self, x):
        self.x = x

class Y(X):
    def __init__(self, x, y):
        X.__init__(self, x)
        self.y = y

class Z(Y):
    def __init__(self, x, y, z):
        Y.__init__(self, x, y)
        self.z = z

objA = Z('Andi', 'PNS', True)
objA = print(vars(objA))

#* Multiple Inheritance
class Karnivora:
    def __init__(self):
        self.daging = True
        self.nama = 'Karnivora'

class Herbivora:
    def __init__(self):
        self.tumbuhan = True
        self.nama = 'Herbivora'

class Omnivora(Karnivora, Herbivora):
    def __init__(self):
        Karnivora.__init__(self)
        Herbivora.__init__(self)                #Properti tergantung pada urutan
        self.mcD = True
        self.nama = 'Omnivora'

objA = Omnivora()
print(vars(objA))
print(Omnivora.__mro__)


# Penggunaan Modul dan Package

#* Datetime
import datetime as dt
x = dt.datetime.now()
print(x)
print(x.strftime('%d')) # tanggal
print(x.strftime('%A')) # nama hari
print(x.strftime('%m')) # bulan
print(x.strftime('%B')) # nama bulan
print(x.strftime('%Y')) # tahun

print(x.strftime('%H')) # 12 jam
print(x.strftime('%I')) # 24 jam
print(x.strftime('%p')) # am / pm
print(x.strftime('%M')) # minute
print(x.strftime('%S')) # sec

print(x.strftime('%c')) # lengkap
print(x.strftime('%x')) # tanggal / bulan / tahun
print(x.strftime('%X')) # jam : minute : second

import datetime as dt
x = dt.datetime.now()

class sekarang:
    def __init__(self, hari, tanggal, bulan, tahun, jam, menit, detik):
        self.hari = hari
        self.tanggal = tanggal
        self.bulan = bulan
        self.tahun = tahun
        self.jam = jam
        self.menit = menit
        self.detik = detik

waktuSkrng = sekarang()

#* Statistics
import statistics
x = [1, 3, 9, 2, 6, 4, 7, 8, 5, 5]
print(statistics.mean(x))
print(statistics.median(x))
print(statistics.mode(x))

from functools import reduce
class Statisik:
    def rataRata(self, x):
        total = reduce(lambda a,b: a + b, x)
        return total
    def nilaiTengah(slef, x):
        x.sort()
        if len(x) % 2 != 0:
            iTengah = [len(x) // 2]
        else:
            iTengah = [int(len(x) / 2)-1, int(len(x) / 2)]
        aTengah = list(map(lambda a: x[a], iTengah))
        total = reduce(lambda x, y : x + y, aTengah)
        return total / len(aTengah)

stat = Statisik()
print(stat.nilaiTengah([1, 2, 3, 4, 7, 9, 10, 12, 6, 6, 5, 3, 2, 1]))


















#!bikin Hariiiiii! Belajar!


