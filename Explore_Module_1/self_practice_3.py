Pembagian mini kelompok belajar JCDS

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

Pembagian nomor absen

import random
absen = set(range(1, 22))
while len(absen) > 0:
    if len(absen) >= 0:
        anggota = set(random.sample(absen, 1))
    absen = (absen ^ anggota)
    a = input('nama? : ')
    print(anggota)
    print(absen)

'''
# for nama in absen

# import random 

# absen = list(range(28))
# a = input('siapa tutornya? : ')
# print(a, random.choices(absen, k=4))

# absen = list(range(1, 28))
# random.shuffle(absen)
# print(absen)

# def pembagian_kelompok(nama, absen):
#     absen = range(1, 27)
'''


