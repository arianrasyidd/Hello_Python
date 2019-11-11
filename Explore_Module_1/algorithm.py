#PRACTICES ALGORITHM

#TODO mencari jumlah huruf
#? cara 1
kalimat = 'Hari ini Hari tidak masuk sekolah'
cari = 'a'
x = kalimat.upper().replace(cari.upper(), '')
print(x)
JmlCari = len(kalimat) - len(x)
print(f"Jumlah huruf '{cari}' ada = {JmlCari}")

#? cara 2
nama = ("Halo Dunia")
cari = 'h'
x = nama.upper().replace(cari.upper(), '')
print(x)
JmlCari = len(nama) - len(x)
print(f"Jumlah huruf '{cari}' ada = {JmlCari}")

#TODO Jumlah kata 'hari'?
kalimat = 'Hari ini Hari tidak masuk sekolah'
cari = 'tidak'
x = kalimat.lower(). replace(cari.lower(), '')
jmlCari = int((len(kalimat) - len(x)) / len(cari))
print(len(kalimat))
print(len(x))
print(f'Jumlah kata \'{cari}\' ada = {jmlCari}')

#TODO membuat algoritma dari soal persamaan linear
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

#? cara 4 (menggunakan input)
# Jika digunakan input
totalHewan  = int(input('Ketik total hewan : '))
totalKaki   = int(input('Ketik total kaki hewan : '))
kakiAyam    = int(input('Ketik jumlah kaki hewan A : '))
kakiKambing = int(input('Ketik jumlah kaki hewan B : '))

divisor = abs(kakiAyam - kakiKambing)

Kambing = abs((totalKaki - totalHewan*kakiAyam) / divisor)
#print("Kambing:", Kambing)

Ayam = abs((totalKaki - totalHewan*kakiKambing) / divisor)
#print("Ayam:", Ayam)

print(f'hewan A = {int(Ayam)}, hewan B = {int(Kambing)}')

#TODO Membuat algoritma untuk prediksi hari kedepan atau kebelakang
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

#TODO Latihan soal perbandingan
#soal ibu dan anak
agediff_i = 1/7
diff_i    = 19
agediff_a = 1/4
diff_a    = 1/2

equation_1 = (diff_i * agediff_a) + diff_a
equation_2 = (agediff_a - agediff_i)
age_ibu    = round(equation_1 / equation_2)

equation_3 = (((agediff_a / agediff_i) * diff_i) + ((diff_i * agediff_a) + diff_a) - diff_i)
equation_4 = (agediff_a / agediff_i) - 1
age_anak   = int(equation_3 / equation_4)

melahirkan = age_ibu - age_anak

print(f'Umur ibu {age_ibu}, Umur anak {age_anak}')
print(f'Maka umur ibu saat melahirkan anak adalah {melahirkan}')

#TODO Self Practice membuat algoritma untuk pembagian kelompok dan absen
#*Pembagian mini kelompok belajar JCDS

import random
absen = set(range(1, 22))
while len(absen) > 0:
    if len(absen) >= 12:
        anggota = set(random.sample(absen, 4))
    else:
        anggota = set(random.sample(absen, 3))
    absen = (absen ^ anggota)
    a = input('nama tutor : ')
    print(anggota)
    print(absen)

#*Pembagian nomor absen
import random
absen = set(range(1, 22))
while len(absen) > 0:
    if len(absen) >= 0:
        anggota = set(random.sample(absen, 1))
    absen = (absen ^ anggota)
    a = input('nama? : ')
    print(anggota)
    print(absen)


#TODO Menghitung hari di akan yang akan datang dari hari sekarang
#100 hari kedepan
hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
now = 'rabu'; brpHari = 100

iNow = hari.index(now)
sisaHari = brpHari % len(hari)
hariYgDicari = hari[(iNow + sisaHari) % 7]

print(hariYgDicari)

# 100 hari kebelakang
hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
now = 'rabu'; brpHari = -100

iNow = hari.index(now)
sisaHari = brpHari % len(hari)
hariYgDicari = hari[(iNow + sisaHari) % 7]

print(hariYgDicari)


#TODO Membuat fungsi membedakan angka ganjil genap manual
def gangen(x):
    if x % 2 == 0:
        print(x, 'tergolong GENAP')
    else:
        print(x, 'tergolong GANJIL')

#TODO Membuat fungsi membedakan angka ganjil genap manual (menggunakan return)
def gangen(angka):
    if angka % 2 == 0:
        return 'GENAP'
    else:
        return 'GANJIL'

#TODO Membuat fungsi calculator sederhana
def iCalculator(a, b):
    a = int(input('masukan angka 1 : '))
    x = input('masukan operator aritmatika (+-*/) : ')
    b = int(input('masukan angka 2 : '))
    if x == '+':
        print(f'hasil dari {a} {x} {b} adalah {a + b')
    elif x == '*':
        print(f'hasil dari {a} {x} {b} adalah {a * b}')
    elif x == '/':
        print(f'hasil dari {a} {x} {b} adalah {a / b}')
    elif x == '-':
        print(f'hasil dari {a} {x} {b} adalah {a - b}')
    else:
        print('maaf operator tidak dikenali')

iCalculator()


#TODO Membuat fungsi replace tanpa menggunakan replace
def vocal(kalimat):
    kalimat = kalimat.lower()
    kalimat = kalimat.replace('a', 'o')
    kalimat = kalimat.replace('i', 'o')
    kalimat = kalimat.replace('u', 'o')
    kalimat = kalimat.replace('e', 'o')
    print(kalimat)

vocal('muhammad arian rasyid')

#TODO Latihan logika menggunakan while
i = 1
while i < 20:
    print(i)
    i += 1

i = 20
while i >= 1:
    print(i)
    i -= 2

students = ['Andi', 'Budi', 'Caca', 'Deni']
index = 0
while index <= len(students) -1:
    print(students[index])
    index += 1

x = students.copy()
print(x)

x = list(range(1, 11))
y = elemen ** 2
    # [1, 4, 9, 16, 25 ... 100]
while len(absen) <= 10

print(x)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = []
index = 0
while index <= len(x) - 1:
    y.append(x[index] ** 2)
    index += 1
print(y)

i = 1
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)
    
password = '12345'
a = input('ketik password : ')
while a != password :
    b = input('Password salah! Ketik Password : ')
    if a == password or b == password:
        print('kamu berhasil')
        break

password = '12345'
jumlah_tebakan = 0
batas_nebak = 5
inputuser = ''
while jumlah_tebakan <= batas_nebak :
    jumlah_tebakan += 1
    inputuser = input('ketik password : ')
    if inputuser == password:
        print('kamu benar')
    elif inputuser != password:
        print('Password salah')
    else:
        print('kamu pintar!')


password = '12345'
jumlah_tebakan = 11
batas_nebak = 5
inputuser = input('ketik password : ')
while jumlah_tebakan != batas_nebak :
    if inputuser == password:
        jumlah_tebakan += 5                           #PR!
        print('kamu benar')
        break
    elif inputuser != password:
        x = input('password salah, coba lagi: ')
    jumlah_tebakan += 1
    
password = '12345'
inputuser = ''
JumlahInput = 0
BatasInput = 5
lebih = False

while inputuser != password and not lebih:
    if JumlahInput < BatasInput:
        inputuser = input(
            f'input ke-{JumlahInput+1} ketik password : ')
        JumlahInput += 1
    else:
        lebih = True

if lebih:
    print('kesempatan habis, tunggu 24 jam')
else:
    print('password benar!')

#TODO Latihan Logika For Loops
for i in range(1, 11):
    if i % 2 == 0:
        print('WOW!')
    else:
        print(i)

#TODO Latihan logika FizzBuzz
def FizzBuzz(x):
    for i in range(1, x+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
    
FizzBuzz(150)

#TODO Membuat Fungsi reverse tanpa menggunakan reverse
#* Cara 1
def reverseList(x):
    r = []
    for i in x:
        r.insert(0, i)
    return r
print(reverseList([8, 7, 6, 3, 4, 5]))

#* Cara 2
def balikPosisi(myList):
    hasil = []
    for i in range(len(myList)):
        hasil.insert(0, mylist[i])
    return hasil
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = ['Andi', 'budi', 'caca', 'kevin']
print(balikPosisi(x))
print(balikPosisi(y))

#TODO Membuat Fungsi pangkat
#* cara 1
def pangkat(a, b):
    z = 1
    for i in range(b):
        z *= a

    return z


print(pangkat(a, b))

#** Cara 2
a = [1, 2, 3, 4, 5, 6, 7, 8, 10]
b = []
c = []

for i in range(len(a)):
    i += 1
    b.append(a[len(a)-i])

print(b)

i = 1
while i <= len(a):
    c.append(a[len(a)-i])
    i += 1

print(c)

#TODO Membuat fungsi replace huruf vokal
def ubahVokal(kata):
    output = ''
    for huruf in kata:
        if huruf in 'aiueo':
            output = output + 'o'
        else:
            output += huruf
    return output

print(ubahVokal('lintang'))
print(ubahVokal('kambing'))

#TODO Membuat fungsi palindrome
#* Cara 1
def palindrome(kata):
    if kata == kata[::-1]:
        return True
    else:
        return False


print(palindrome('sore'))

#** Cara 2
def palindrome2(kata):
    for i in range(round(len(kata)/2)):
        palindromekah = False
        if kata[i] == kata[len(kata)-1-i]:
            palindromekah = True
        else:
            palindromekah = False
            break

    return palindromekah


palindrome2('malam')

#*** Cara 3
kalimat = 'Hai aku Lintang'

def palindrome(kalimat):
    x = ''
    kata = kalimat.split()
    for i in kata:
        z = i[::-1] + ' '
        x += z
    
    return x


print(palindrome("Hai aku Lintang"))


#TODO Membuat algoritma bentuk segitiga siku - siku
membuat bintang (segitiga siku2)
def star(x):
    star = ''
    for i in range(x):
        star += ' * '
        print(star)
    return star


star(5)

#TODO Bintang segitiga kebalik
def rStar(x):
    star = ''
    for i in range(x):
        star = ' * ' * (x-i)
        print(star)    
        

rStar(5)

#TODO Algoritma membentuk shape
bintang segitiga kebalik
def rStar(x):
    star = ''
    for i in range(x):
        star = ' * ' * (x-i)
        print(star)    
        

rStar(5)


urutan angka menjadi setengah pyramid
def nStar(x):
    star = ''
    for i in range(x):
        star += str(i) + ' '
        print(star)
    return star

nStar(20)

urutan angka menjadi setengah pyramid terbalik
def rStar(x):
    star = ''
    for i in range(x):
        star = i * str(x-i) + ' '
        print(star)    
        

rStar(20)


urutan angka pyramid dengan jajaran angka
def aStar(x):
    star = ''
    for i in range(x):
        star = str(i + 1) * (i + 1) + ' '
        print(star)
    print('\n')
    return star

aStar(9)


def bStar(x):
    star = ''
    for i in range(x):
        star = str(i + 1) * (x - i) + ' '
        print(star)
    print('\n')
    return star

bStar(9)

def cStar(x):
    star = ''
    for i in range(x):
        checkpoint = list(star + str(i + 1) + ' ')
        type(checkpoint)
        for y in checkpoint:
             reversed(checkpoint)
    return star

cStar(20)

#TODO bikin function factorial
def faktorial(x):
    angka = 1
    for i in range(1, x+1):
        angka *= i
    print(angka)

faktorial(3)

#TODO Bikin function factorial menggunakan rekursif function (fungsi (a) didalam fungi (a))
def faktorial2(x):
    if x <= 2:
        return x
    else:
        return x * faktorial2(x-1)      # fungsinya memanggil diri sendiri

print(faktorial2(4))

#TODO Practice Map Function
a = ['Cokelat', 'Kiwi', 'Melon']
b = ['Apel', 'Jeruk', 'Nanas']
def combi (a, b):
    return a + ' ' + b
x = map(combi, a, b)                #?fungsinya, sama object yang mau diolahnya
print(list(x))

#TODO Practice Lambda Function
ef myFunction(x):
    return lambda a : a ** x            #?penggunaan parameternya adalah X
pangkat2 = myFunction(2)
pangkat3 = myFunction(3)
pangkat5 = myFunction(5)

print(type(pangkat2))
print(pangkat2(12))
print(pangkat3(4))
print(pangkat5(2))

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


#*TODO penggunaan function dengan map dan lambda
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


#TODO Membuat fungsi seperti irisan menggunakan filter dan lambda
x = [1, 2, 3, 4, 5]
y = [1, 2, 6, 7, 8]
z = list(filter(lambda a : a in x, y))
print(z)


#TODO Membuat algoritma untuk menentukan bilangan prima
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


#TODO Make a simple car game
command = ""
started = False
while True:
    command = input('>>> ').lower()
    if command == 'start':
        if started:
            print('Car has been started.')
        else:
            started = True
            print('Car started...')
    elif command == 'stop':
        if not started == True:
            print('Car has been stopped.')
        else:
            started = False
            print('Car Stopped.')
    elif command == 'help':
        print('''
start - to start the car
stop - to stop the car
exit - to quit the game
        ''')
    elif command == 'quit':
        print('Thank you! see you soon!')
        break
    else:
        print("I'm sorry, I don't understand")


#TODO Make make algorithm to print F in Terminal
numbers = [5, 2, 5, 2, 2]
for x in numbers:
    output = ''
    for y in range(x):
        output += '*'
    print(

#TODO Make a max function manually
numbers = [1, 3, 5, 7, 9, 10, 12, 32, 23, 45, 21, 6, 5, 8]
def find_max(numbers):
    maxFunc = numbers[0]
    for number in numbers:
        if number > maxFunc:
            maxFunc = number
    return maxFunc


#TODO Remove the duplicate algorithm
numbers = [2, 2, 4, 6, 3, 4, 6, 1, 3, 2]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


#TODO Emoji Converter function manually
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)" : "😊"
        ":(" : "😥"
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '
    return output


message = input('>')
print(emoji_converter())

