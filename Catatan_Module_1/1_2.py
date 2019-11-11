#Aritmethical Operation

#* Aritmethical Methode
x = 18                  #variable_1
y = 2                   #variable_2
print(x + y)            #penjumlahan
print(x - y)            #pengurangan
print(x * y)            #perkalian
print(x / y)            #hasil pembagian akan selalu float
print(x // y)           #hasil pembagian akan menjadi integer
print(y ** 2)           #bisa juga pake print(pow(x, y))
print( 10 % 3)          #modulus = hasil dari pembagian
print(abs(x))           #angka absolut, gapeduli positif negatifnya

#* akar pangkat
print(4 ** (1/2))       #atau bisa juga pake bilangan desimal, contohnya 4 ** (0.5)
print(27 ** (1/3))      #karena 4 akar 2 = 2, karena 27 akar 3 = 3

#* max and min funtion
print(max(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))       #mensortir angka terbesar untuk dijadikan sebagai output
print(min(1, 2, 3, 4 ,5, 6, 7, 8, .2))          #mensortir angka terkecil untuk dijadikan sebagai output

#* pembulatan
print(round(3.67856))           #membulatkan menjadi integer
print(round(3.67856, 1))        #float dengan 1 angka dibelakang koma
print(round(3.67856, 2))        #float dengan 2 angka dibelakang koma
print(0.1 + 0.2)                #angka menjadi integer
print(round((0.1 + 0.2), 1))    #float dengan 1 angka dibelakang koma

#* math library
import math                     #memasukan math libraries
print(math.pi)                  #pi dari lingkaran
print(math.floor(3.9))          #dibulatkan keatas
print(math.ceil(3.9))           #dibulatkan kebawah
print(math.sqrt(196))           #akar pangkat 2
print(math.factorial(6))        #6! = 6 * 5 * 4 * 3 * 2 * 1 = ???

#TODO Practice -1
#? cara 1
x = 13                      #jumlah total ekor ayam dan kambing (k + a = 13)
y = 32                      #jumlah total kaki ayam dan kambing (4k + 2a = 32)
KK = 4
KA = 2
k = (y-2*x) / KA
print('Jumlah kambing adalah', int(k))
a = x-k
print('Jumlah ayam adalah', int(a))
Ayam = (jumlah_Kaki - (kaki_kambing * jumlah_Total)) / (kaki_ayam - kaki_kambing)
Kambing = (Jumlah_Kaki - (kaki_ayam * jumlah_Total)) / (kaki_kambing - kaki_ayam)

#? cara 2
Jmlhewan = 13
Jmlkaki = 32
kakikambing = 4
kakiayam = 2
ayam = int((((Jmlhewan*kakikambing) - Jmlkaki) / kakiayam))
kambing = Jmlhewan - ayam
print(kambing)
print(ayam)

#? cara 3
jumlah_hewan = int(input("total jumlah hewan? : "))
jumlah_kaki = int(input("total jumlah kaki? : "))
kaki_ayam = int(input("kaki ayam ada? : "))
kaki_kambing = int(input("kaki kambing ada? : "))
ayam = int(input(((jumlah_hewan * kaki_kambing) - jumlah_kaki) / kaki_ayam == x))
kambing = int(input(jumlah_hewan - ayam))
print(ayam)
print(kambing)
