#if, elif dan else
#* Contoh 1
nilai = 40
if nilai > 80:
    print(f'Nilai anda {nilai}, Anda Lulus!')
elif nilai < 40:
    print(f'nilai anda {nilai} tidak lulus!')
else:
    print(f'nilai anda {nilai}, anda remedial')

#* Contoh 2
massa = 50
tinggi = 1.78 
IMT = massa / tinggi
if IMT < 18.5:
    print("berat badan kurang")
elif 18.5 <= 24.9:
    print("berat badan ideal")
elif 25.0 <= 29.9:
    print("berat badan berlebih")
elif 30.0 - 39.9:
    print("berat badan sangat berlebih")
elif IMT > 39.9:
    print("obesitas")

#* Contoh 3
nilai = 30
if nilai >= 82:
    print('A')
elif nilai > 72 and nilai  < 81:
    print('B')
elif nilai > 62 and nilai < 71:
    print('C')
elif nilai > 52  and nilai < 61:
    print('D')
else:
    print('E')

#count function
x = "abcdefghijklmnopqrstuvwxyzxyz"         #memastikan ada berapa huruf tertentu di sebuah variable
print(x.count('g'))

#memanggil sebuah huruf dengan pola yang kita mau [start : stop : step]
x = "abcdefghijklmnopqrstuvwxyzxyz"
print(x[::2])
print(x[len(x) - 1]) #print(x[-1])

#memastikan sebuah angka atau huruf berada dalam sebuah data set (list, dict, set, tuple)
print('g in x')

#mencari jumlah sebuah huruf dalam kalimat
kalimat = 'Hari ini Andi tidak kuliah'
cari = 'h'                                      
print(cari.lower() in kalimat.lower())          #biar lebih terstuktur
print(kalimat.lower().count(cari.lower()))


#TODO Practice -1
#Sekarang hari Rabu, hari apakah 100 hari lagi?
hari = [
    'senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu'
]
#cara 1
now = 'Rabu' ; brpHari = 100
var_1  = hari[2]
var_2 = 100 % 7
var_3 = hari[len(hari) - hari[var_2]]
print(var_3)
result = (var_1 + hari[var_2])
print(result)

#cara 2 (evaluasi dari cara 2)
hari = [
    'senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu'
]
# "Sekarang hari Rabu, hari apakah 100 hari lagi?"
now = 'Rabu' ; brpHari = 100
var_1  = hari[2]
var_2 = 100 % 7
var_3 = hari[len(hari) - var_2]
print(var_3)

#undifined
a = [
    'senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu'
]
b = 7
c = 100
d = "rabu"
d = ((c % b).a.index('rabu'))

#100 hari kedepan
hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
now = 'rabu'; brpHari = 3
iNow = hari.index(now)
sisaHari = brpHari % len(hari)
hariYgDicari = hari[(iNow + sisaHari) % 7]
print(hariYgDicari)

#100 hari kebelakang (cara 1(butuh evaluasi)(bikin variable buat perhitungan absolutnya))
hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
now = 'rabu'; brpHari = 3
iNow = hari.index(now)
sisaHari = brpHari % len(hari)
hariYgDicari = abs(hari[iNow - sisaHari]) % 7
print(hariYgDicari)

# 100 hari kebelakang (cara 2)
hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
now = 'rabu'; brpHari = -3
iNow = hari.index(now)
sisaHari = brpHari % len(hari)
hariYgDicari = hari[(iNow + sisaHari) % 7]
print(hariYgDicari)

#List Function

#* Beberapa Fungsi untuk List
hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
hari.append('senin2')       #nambahin yang di paling belakang
print(hari)
hari.insert(4, 'senin3')    #selipin tambahan di dalam list
print(hari)
hari.remove('senin2')       #ngehapus elemen dalam list sesuai elemennya
print(hari)
hari.pop(2)                 #ngehapus elemen dalam list sesuai indexnya
print(hari)
hari.clear()                #ngehapus semua elemen dalam list
print(hari)

hari.sort()                   #ngurutin sesuai konten (dari alfabetis atau dari angka terkecil kebesar untuk angka, tapi gabisa digabung angka sama huruf)
print(hari)
hari.reverse()                   #ngurutin sesuai indexnya)
print(hari) 
x = [1,2,3,4,5,6,7,8,9]
y = x[::2].copy()
print(x)
print(y)
print(x + y)


#Tuple

#* Fungsinya sama dengan list, tetapi setiap elemen dari tuple tidak bisa dirubah
#* Penggunaannya adalah ketika kita memiliki code atau data yang tidak ingin dirubah siapapun didalam file utamanya
#* contoh tuple
a = (1, 3, 5, 7, 9)
print(type(a))


#Range

#* Contoh dari Range
listItem = list(range(1, 11, 2)) ; print(listItem)
listitem = list(range(1, 33, 3)) ; print(listitem)
abcd = list(range(1, 32, 2)) ; print(abcd)
a = [1, 2, 3, 4, 5, 6, 7, 8, 10]
for i in range(len(a)):
    i += 1
    b.append(a[len(a)-i])

print(b)


#TODO Latihan Logika dan range intermediate level

y = 'Nama urut '
for item in range(1, 11) :
    print(y + str(item))

x = ' Nama urut '
for item in range(0, 22, 2) :
    print(x + str(item))

z = ''
for item in range(0, 5): 
    z += ' * '
print(z)

a = ''
for item in range (0, 5):
    a += ' * \n'
# print(a)

b = ' \n'
for item in range (0, 5):
    b += ' * ' * 5
print(b)

b = ' \n'
for item in range (0, 5):
    b += ' * \n' * 5
print(b)

z = ''
for item in range(5):
    for item1 in range(5):
        z += ' * '
    z += '\n'

print(z)

z = ''
for item in range(1):
    for item1 in range(2):
        for item in range(3):
            z += '0'
        z += ' * '
    z += '\n'

print(z)