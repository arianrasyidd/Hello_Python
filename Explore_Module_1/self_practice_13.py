# data = open('data_penjualan_motor_honda_2014_2018.csv', 'r')
# print(data.readable())
# files = data.readlines()
# pre_header = (files[0].split(','))
# pre_header[-1] = pre_header[-1][ :-1]
# print(pre_header)
# header = pre_header.index(::)

# print(header)
# print(header[1])
# for title in files[0]:
#     dict(row)

# import csv

# with open(data_penjualan_motor_honda_2014_2018.csv 'r') as x:
#     baca = csv.reader(x)
#     print(list(baca))

# x = ['Tahun', Periode, Jenis, Jumlah]
# y = [2014, 'Januari', Honda, 191921932]
# print(dict(zip(x, y)))

# import csv

# with open('data_penjualan_motor_honda_2014_2018.csv', 'r') as x:
#     baca = csv.DictReader(x)
#     for i in baca:
#         print(dict(i))

# import csv

# data = [{'Nama' : 'Andi', 'Usia': 22, 'Kota': 'Jakarta'},
#         {'Nama' : 'Budi', 'Usia': 22, 'Kota': 'Bandung'},
#         {'Nama' : 'Caca', 'Usia': 23, 'Kota': 'Jakarta'},
# ]

# with open('0.csv', 'w', newline='') as x:
#     kolom = ['Nama', 'Usia', 'Kota']
#     a = csv.DictWriter(x, fieldnames=kolom, delimiter='!')
#     a.writeheader()
#     a.writerows(data)


# import json

# with open('tes.json', 'r') as x:
#     out = json.load(x)

# print(type(out))
# print(type(out[0]))
# print(out)

# import json

# with open('tes.json', 'r') as x:
#     out = json.load(x)

# with open('haha.json', 'w') as y:
#     json.dump(out, y)


#TODO manual / pakai package csv json:
# 1. csv => json
# 2. json => csv