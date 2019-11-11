# #Class,
# #* class = cetakan object
# class Mobil:
#     warna = 'merah'
#     tahun = 2010

# #* create object mobil
# # mobil1 = Mobil()
# # print(Mobil)
# # print(mobil1)
# # print(mobil1.warna)
# # print(mobil1.tahun)

# # mobil2 = Mobil()
# # print(mobil2.warna)
# # print(mobil2.tahun)

# #* membuat fungsi didalam kelas
# # class MobilCustom():
# #     def __init__(self,  warna, tahun, model):
# #         self.color = warna
# #         self.year = tahun
# #         self.model = model
# #     #method
# #     def jadul(self):
# #         if self.year < 2010:
# #             return True
# #         else : return False
# #     def tes(self):
# #         print(self.color, self.year, self.model, self.jadul())


# # mobilA = MobilCustom('pink', 1998, 'X')              #syntatic sugar
# # mobilB = MobilCustom('blue', 2018, 'Z')

# # mobilA.tes()
# # print(mobilA.jadul())

# # #* menambah variabel ke dalam kelas
# # class MobilCustom():
# #     def __init__(self,  warna, tahun):
# #         self.color = warna
# #         self.year = tahun

# # class Car(MobilCustom):                   #inheritance
# #     gps = True

# # mobil1 = MobilCustom('pink', 2004)
# # car1 = Car('black', 2008)
# # print(mobil1.color, mobil1.year, mobil1.gps)
# # print(car1.color, car1.year, car1.gps)

# #* menambah variabel ke dalam kelas
# # class MobilCustom():
# #     def __init__(self,  warna, tahun):
# #         self.color = warna
# #         self.year = tahun

# # class Car(MobilCustom):
# #     def __init__(self, soundSys):
# #         self.soundSys = soundSys

# # mobil1 = MobilCustom(['pink', 'red'], 2004)
# # car1 = Car('black', 2008)
# # print(mobil1.color, mobil1.year, mobil1.gps)
# # print(car1.color, car1.year, car1.gps)

# #* menambah object baru di inherite
# # class X:
# #     def __init__(self, nama, gelar):
# #         self.nama = nama
# #         self.gelar = gelar

# # class Y(X):
# #     def __init__(self, nama, gelar, univ):
# #         super().__init__(nama, gelar)
# #         self.kampus = univ

# # objX = X('Andi', 'M.Sc')
# # objY = Y('Budi', 'Dr.', 'UNPAD')
# # print(objY.kampus)

# #* Cara menampilkan seluruh hasil di output 
# # class X:
# #     def __init__(self, nama, gelar):
# #         self.nama = nama
# #         self.gelar = gelar

# # class Y(X):
# #     def __init__(self, nama, gelar, univ):
# #         super().__init__(nama, gelar)
# #         self.kampus = univ

# # class Z(Y):
# #     pass

# # objX = X('Andi', 'M.Sc')
# # objY = Y('Budi', 'Dr.', 'UNPAD')
# # objZ = Z('Caca', 'S.E.', 'UI')
# # print(objY.kampus, objY.gelar, objY.nama)       #cara 1

# # from pprint import pprint
# # pprint(vars(objY))                              #cara 2

# # print(vars(objY))                               #cara 3

# #* memanggil object ke output
# # print(objY.nama)
# # print(getattr(objY, 'nama'))

# #* memastikan atribut yang ada
# # print(hasattr(objY, 'warna'))                   #hanya mengeluarkan False and True
# # print(hasattr(objY, 'nama'))

# #* menambah properti ke object
# # objY.warna = 'merah'
# # objZ.usia = 23
# # setattr(objZ, 'alamat', 'BSD')
# # print(vars(objY))
# # print(vars(objZ))

# # #* menghapus properti di object
# # delattr(objZ, 'alamat')
# # print(vars(objZ))

# class student:
#     def __init__(self, nama, usia):
#         self.nama = nama
#         self.usia = usia

# data = [
#     {'nama' : 'Andi', 'usia' : 21},
#     {'nama' : 'Budi', 'usia' : 22},
#     {'nama' : 'Caca', 'usia' : 23},
#     {'nama' : 'Deni', 'usia' : 24}
# ]

# def createObj(x):
#     nama = x['nama']
#     vars()[nama] = student(x['nama'], x['usia'])
# return vars()[nama]
# def  createObj(x):
#     return student (x['nama', x['usia']])

# dataNew = list(map(
#     lambda x : student(x['nama'], x['usia']), data
# ))
# print(dataNew[0].nama)

print('ok')
print('yes')

print(123)

print(890)

