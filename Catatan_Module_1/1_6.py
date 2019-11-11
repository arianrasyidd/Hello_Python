#Function
Note = '''
1.fungsinya membungkus program
2.membantu mempersingkat penulisan kode
3.kita bisa manggil variabel diluar function
4.kita tidak bisa manggil variable yang ada dalam function ke luar function
5.nama parameter bebas, walaupun memanggil variabel dari luar
# 6.mereturn suatu value
'''

#contoh function dengan 1 parameter
def kuadrat(angka):
    print(angka ** 2)
kuadrat(2)
kuadrat(3)

#contoh function dengan 2 parameter
def pangkat(angka1, angka2):
    print(angka1 ** angka2)
pangkat(2, 3)
pangkat(3, 5)
pangkat(
    float(input('Ketik angka 1 : ')),
    float(input('Ketik angka 2 : '))
)

x = ['andi', 'budi', 'caca']
def tes():
    print(x[0])
    print('caca' in x)

tes()

#Contoh singkat
def gangen(x):
    if x % 2 == 0:
        print(x, 'tergolong GENAP')
    else:
        print(x, 'tergolong GANJIL')

# practice_2
# def iCalculator(a, b):
#     a = int(input('masukan angka 1 : '))
#     x = input('masukan operator aritmatika (+-*/) : ')
#     b = int(input('masukan angka 2 : '))
#     if x == '+':
#         print(f'hasil dari {a} {x} {b} adalah {a + b')
#     elif x == '*':
#         print(f'hasil dari {a} {x} {b} adalah {a * b}')
#     elif x == '/':
#         print(f'hasil dari {a} {x} {b} adalah {a / b}')
#     elif x == '-':
#         print(f'hasil dari {a} {x} {b} adalah {a - b}')
#     else:
#         print('maaf operator tidak dikenali')

# iCalculator()


#practice_3
# def vocal(kalimat):
#     vokal = ['a', 'i', 'u', 'e', 'o']
#     if 'a' in kalimat:
#         print(kalimat.replace('a', 'o').replace('i', 'o').replace('u', '0').replace())
#     # elif 'i' in kalimat:
#     #     print(kalimat.replace('i', 'o'))
#     # elif 'u' in kalimat:
#     #     print(kalimat.replace('u', 'o'))
#     # elif 'e' in kalimat:
#     #     print(kalimat.replace('e', 'o'))
#     # else:
#     #     print('tidak ada kalimat vokal')

# vocal('muhammad arian rasyid')

#practice_3 (jawaban)
# def vocal(kalimat):
#     kalimat = kalimat.lower()
#     kalimat = kalimat.replace('a', 'o')
#     kalimat = kalimat.replace('i', 'o')
#     kalimat = kalimat.replace('u', 'o')
#     kalimat = kalimat.replace('e', 'o')
#     print(kalimat)

# vocal('muhammad arian rasyid')

#return
note = '''
1. Apabila menggunakan return, kita harus menggunakan print lagi ketika memanggilnya
2. Apabila didalam funsi sudah ada print, kita tidak perlu menggunakan print lagi ketika ingin memanggilnya
3. Ketika didalam fungsi sudah ada print, dan kita menggunakan print lagi, maka akan menghasilkan output 'none'
'''

#* Contoh
def gangen(angka):
    if angka % 2 == 0:
        return 'GENAP'
    else:
        return 'GANJIL'

print(gangen(46))


#while loops

#* Contoh penggunaan dan latihan logika
# i = 1
# while i < 20:
#     print(i)
#     i += 1

# i = 20
# while i >= 1:
#     print(i)
#     i -= 2

# students = ['Andi', 'Budi', 'Caca', 'Deni']
# index = 0
# while index <= len(students) -1:
#     print(students[index])
#     index += 1

# x = students.copy()
# print(x)

# x = list(range(1, 11))
# y = elemen ** 2
#     # [1, 4, 9, 16, 25 ... 100]
# while len(absen) <= 10

# print(x)

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = []
# index = 0
# while index <= len(x) - 1:
#     y.append(x[index] ** 2)
#     index += 1
# print(y)

# i = 1
# while i < 10:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# i = 0
# while i < 10:
#     i += 1
#     if i == 5:
#         continue
#     print(i)
    
# password = '12345'
# a = input('ketik password : ')
# while a != password :
#     b = input('Password salah! Ketik Password : ')
#     if a == password or b == password:
#         print('kamu berhasil')
#         break

# password = '12345'
# jumlah_tebakan = 0
# batas_nebak = 5
# inputuser = ''
# while jumlah_tebakan <= batas_nebak :
#     jumlah_tebakan += 1
#     inputuser = input('ketik password : ')
#     if inputuser == password:
#         print('kamu benar')
#     elif inputuser != password:
#         print('Password salah')
#     else:
#         print('kamu pintar!')


# password = '12345'
# jumlah_tebakan = 11
# batas_nebak = 5
# inputuser = input('ketik password : ')
# while jumlah_tebakan != batas_nebak :
#     if inputuser == password:
#         jumlah_tebakan += 5                           #PR!
#         print('kamu benar')
#         break
#     elif inputuser != password:
#         x = input('password salah, coba lagi: ')
#     jumlah_tebakan += 1
    
# password = '12345'
# inputuser = ''
# JumlahInput = 0
# BatasInput = 5
# lebih = False

# while inputuser != password and not lebih:
#     if JumlahInput < BatasInput:
#         inputuser = input(
#             f'input ke-{JumlahInput+1} ketik password : ')
#         JumlahInput += 1
#     else:
#         lebih = True

# if lebih:
#     print('kesempatan habis, tunggu 24 jam')
# else:
#     print('password benar!')