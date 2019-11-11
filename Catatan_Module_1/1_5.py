#dictionary

#* Contoh penggunaan -1
andi = {
    'name' : 'Andi',
    'age' : 22,
    'is_married' :  False
}
print(andi['name'])
print(andi['age'])
print(andi['is_married'])
print(andi.get('name'))
print(andi.get('job', 'maaf Andi masih nganggur')) #bisa ditambahkan, tapi tidak menjadi key
print(andi['job'])
andi['name'] = 'Budi' #mengubah key, yang tadinya andi jadi budi
print(andi)

#* contoh penggunaan -2
andi = {
    'name' : 'Andi',
    'age' : 22,
    'is_married' :  False,
    'job' : 'pns',
    'cars' : ['Alphard', 'Xpander', 'Innova'],
    'address' : {
        'street' : 'mawar ungu',
        'RT' : 5, 'RW' : 121, 'kecamatan' : 'X',
        'zipcode' : 123456,
        'geo' : {
            'lat' : 111.11,
            'lng' : 65.86
        }
    }
}
print(andi['name'])
print(andi['age'])
print(andi['is_married'])
print(andi.get('name'))
print(andi['address']['geo'])
print(andi.get('home', 'tidak punya rumah'))
andi['salary'] = 25000000                  #buat nambahin key alias update property istilahnya
andi.update({'no_ktp' : 123456789123456})   #buat nambahin key juga
print(andi)

# Contoh penggunaan -3
#? kalo mengubah dict ke list, cuma keynya aja yang keluar
andi = {
    'name' : 'Andi',
    'age' : 22,
    'is_married' :  False,
    'job' : 'pns',
    'cars' : ['Alphard', 'Xpander', 'Innova'],
    'address' : {
        'street' : 'mawar ungu',
        'RT' : 5, 'RW' : 121, 'kecamatan' : 'X',
        'zipcode' : 123456,
        'geo' : {
            'lat' : 111.11,
            'lng' : 65.86
        }
    }
}
print(andi['name'])
print(andi['age'])
print(andi['is_married'])
print(andi.get('name'))
print(andi['address']['geo'])
print(andi.get('home', 'tidak punya rumah'))

andi ['salary'] = 25000000                   
andi.update({'no_ktp' : 123456789123456})   
print(list(andi))
print(list(andi.keys()))
print(andi.keys())
print(andi.values())
print(list.(andi.values()))


#practice 4
days = {
    'senin': 'monday',
    'selasa': 'tuesday',
    'rabu': 'wednesday',
    'kamis': 'thursday',
    'jumat': 'friday',
    'sabtu': 'saturday',
    'minggu': 'sunday'
}
input('ketik nama hari : ')
input('Bahasa Inggrisnya senin = Monday')
listhari = list(days.keys())
listhari2 = list(days.values())
hari = input('ketik nama hari : ')
indexHariFind = listhari2.index(hari)
hari_1 = listhari[indexHariFind]
print (f'bahasa indonesianya = {hari_1}')

# print(f'Bahasa inggrisnya {hari.upper()} = {days.get(hari.lower(), "Ga ada!")} ')
# input('ketik nama hari : ')
# input('bahasa inggrisnya : ')
# print(f'Bahasa inggrisnya {hari.upper()} = {days[hari.lower()].upper()}')