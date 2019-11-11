# #Open Data
# #? Berlaku untuk hampir semua format file, termasuk file python itu sendiri (py) atau txt., dll.

#* Practice Opening data -1
# data = open('./practice/note.txt', 'r') #untuk masuk ke folder
# data = open('./../note.txt', 'r') #untuk keluar ke folder
# data = open('note.txt', 'r') #r untuk read
# data = open('note.txt', 'a') #a untuk append alias menambah konten di file tersebut
# data = open('note.txt', 'w') #w untuk write dan langsung membuat file
# # data.write('test 123') #tetapi kalo kita write di file yang sudah ada, isi sebelumnya akan hilang
# # data.write('\nCoding Python') #2 kali write tanpa menghapus isi file sebelumnya
# # print(data.readable()) #untuk memastikan data bisa dibaca atau tidak
# # print(data.read()) #untuk membaca filenya
# # print(data.readlines()) #untuk dijadikan list
# # print(data.readline()) #untuk membaca per-index

#* Practice copying data -2
# file = open("tes.txt", "r")
# x = file.read()
# data = open("tes.py", "w")
# data.write(x)

# print(data.readable()) #! terlalu ribet
# reading = data.readlines()
# fungsi = reading.copy()
# print(fungsi)

#* Practice moving data and reverse it -3 
# data = open('tes.txt', 'w') #! belum beres

# data.write()
# data.write("\n\n\n'Andi', 'Budi', 'Caca'")


data = open('data.txt', 'r')
x = data.read().split(', ')[::-1]
print(x)

output = open('x.txt', 'a')
for i in x:
    output.write(i + '\n')