# nama = 'arian'
# print(len(nama) + 10)
# print(nama[1:len(nama)])
# print(nama[len(nama) - 1])
# print(nama.replace('a', 'e'))

# print(max(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))       #mensortir angka terbesar untuk dijadikan sebagai output
# print(min(1, 2, 3, 4 ,5, 6, 7, 8, .2))  

# print(round(3.6501, 1))
# print(round((0.1 + 0.2), 1))
# print(0.1 + 0.2)

# kalimat = 'Hari ini Andi tidak kuliah'
# cari = 'h'
# x = cari.lower()
# print(cari.lower() in kalimat.lower())          #biar lebih terstuktur
# print(kalimat.lower().count(x))

# kalimat = 'Hari ini Andi tidak kuliah'
# cari = 'h'                                      
# print(cari.lower() in kalimat.lower())          #biar lebih terstuktur
# print(kalimat.lower().count(cari.lower()))

# "Sekarang hari Rabu, hari apakah 100 hari lagi?"
question = '''
1.kenapa kalo index_brpHarinya dijadiin sama dengan 7 atau kelipatannya, hasilnya index out of range?
'''
# hari = [
#     'senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu'
# ]
# now = 'Rabu' ; brpHari = 100
# index_now  = hari[2]
# index_brpHari = 7 % 7
# a_result = hari[len(hari) - index_brpHari]
# print(a_result)

# print(index_brpHari)
# var_2 = 100 % 7
# print(type(var_2))

# a = [
#     'senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu'
# ]
# b = 7
# c = 100
# d = "rabu"
# d = ((c % b)a.index('rabu')) #? bisa gasih ini?
# print(d)
# hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
# now = 'rabu'; brpHari = 3
# iNow = hari.index(now)
# sisaHari = brpHari % len(hari)
# hariYgDicari = hari[(iNow + sisaHari) % 7]
# print(hariYgDicari)


# hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
# now = 'rabu'; brpHari = 3
# iNow = hari.index(now)
# sisaHari = brpHari % len(hari)
# hariYgDicari = hari[abs(iNow - sisaHari)] % 7
# print(hariYgDicari)

# hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
# now = 'rabu'; brpHari = -3
# iNow = hari.index(now)
# sisaHari = brpHari % len(hari)
# hariYgDicari = hari[(iNow + sisaHari) % 7]
# print(hariYgDicari)

# x = {1 : True, 2 : False}
# print(x.items())

#bikin angka f, cara 1
# x = 'x'
# a = ''
# numbers = [5, 2, 5, 2, 2]
# for number in numbers:
#     for y in range(0,number):
#        a += x
#     print(a)
#     a = ''

#cara 2
# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     print('x' * x_count)