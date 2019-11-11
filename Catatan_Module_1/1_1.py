# #Basic Fundamentals of Python

# #* variables & type dari variablenya
# nama = "andi"       #string
# usia = 12           #integer
# tinggi = 189.3      #float
# jomblo = False      #boolean


# # String

# #* penjelasan sederhana
# print("jum'at")                 #tanda kutip 1 dengan 2 beda
# print('jum\'at')                #pake backlash kalo mau cancel atau kalo mau pake 1
# print('Purwadhika\tSchool')     #untuk tab
# print('Purwadhika\nSchool')     #untuk enter

# #* menggabungkan string dengan variabel
# nama = 'arian'
# print(nama + ' school')         #Cara ke-1
# print(nama, 'school')           #Cara ke-2

# #* str() menjadikan selain string menjadi string
# print('saya ' + nama + ' usia ' + str(usia))    #Cara ke-1
# print('saya', nama, 'usia', usia)               #Cara ke-2

# #* %s reference to string yg di %, %d reference to digit yg di %
# print('Saya %s usia %d' % (nama, usia))

# #* {} reference to yg di dalem .format
# print('Saya {} usia {}'.format(nama, usia))

# #* print dengan metode singkat (f)
# print(f'Saya {nama} usia {usia}')

# #* variable string jadi berhuruf besar atau kecil
# print(nama.lower())
# print(nama.upper())

# #* ngecek sebuah variabel string hurufnya capital atau engga
# x = 'hahaha'
# print(x.islower())
# print(x.isupper())
# print(nama.lower().isupper())
# print(nama.upper().islower())

# #* len untuk ngecek jumlah karakter dalam variabel string sampe terakhir
# print(len(nama))
# print(len(nama) + 5)

# #* [diisi nomor urutan] untuk ngecek huruf di urutan itu dalam sebuah variabel string
# print(nama[0])
# print(nama[2])

# #* penggunaan titik dua (:) buat ngecek huruf dari urutan start sampe stop
# print(nama[0:2])
# print(nama[1:len(nama)])

# #* start : stop : step
# print(nama[1 : len(nama) : 2])

# #* kalau pake -(minus) ngitungnya mulai dari kata terakhir
# print(nama[-1])
# print(nama[len(nama) - 1])

# #* pake .index buat ngecek huruf tertentu ada diurutan berapa dalam sebuah variabel string
# print(nama.index('a'))

# #* pake .replace buat ganti karakter
# print(nama.replace('An', 'Un'))

# #* update variable
# x = 12
# x = 13
# print(x)
# x = 12
# x = x + 13
# x += 13
# print(x)


# #TODO practice

# #* Review materi di atas
# kampus = "Purwadhika Startup & Coding School"
# kelas = 'Data Science'
# print(f'Saya saat ini bersekolah di {kampus}, mengambil jurusan {kelas}')
# print(kampus.upper())
# print(kampus.isupper())
# print(nama)
# print(len(nama))
# print(len(nama.replace(" ","")))

# #! Percobaan. Mencoba mencari jumlah huruf dengan count
# print(kampus.lower().count("c"))
# print(kampus.lower().count("startup"))
# print(len(kampus[11:17]))


# #TODO Practice String -1
# x = "halo dunia"
# print(x.split(' '))
# print(x.capitalize())
# print(x.index('dunia'))
# print(x.lower())
# print(x.upper())
# print(len(x.replace(' ', '')))



# # Input methode

# #* Basic Input
# nama = input('Halo, namamu siapa? : ')
# print(f'Selamat datang {nama}')

# #* print(type(angka))
# angka = int(input('Masukkan angka : '))

# #TODO Practice Input -1
# total_hewan = input('ketik total hewan? : ')
# total_kaki = input('ketik total kaki hewan? : ')
# jumlahkakiayam = input('ketik jumlah kaki hewan A?: ')
# jumlahkakibsd = input('ketik jumlah kaki hewan B?: ')
# ayam = input('hewan = x: ')
# kambing = input('hewan B = y: ')

# #TODO Practice Input -2
# nama = (input("nama kamu? : "))
# umur = (input("umur kamu? : "))
# kelamin = (input("kelamin kamu? :"))
# pekerjaan = (input("pekerjaan kamu? : "))
# print("nama : ", nama)
# print("umur : ", umur)
# print("kelamin : ", kelamin)
# print("pekerjaan : ", pekerjaan)

# #TODO Practice Input -3
# a = input('Hello, what\'s your name? :')
# b = input('where do you come from?: ')
# c = input('could i get your number? : ')
# print('So, you are %s from %s, your number is %s, don\'t you?' %(a, b, c))

