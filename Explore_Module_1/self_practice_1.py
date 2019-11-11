


nama = 'Andi'; print(nama)
usia = 22
usia += 10
print(usia)
jomblo = True; print(jomblo)

import math
print(math.pi)
print(math.fabs(-4.7))
print(math.fabs(-33))

text = "I'm Arian, nice to meet you"
print(text[1])
print(text[2:])
print(text[:4])
print(text[2:5])
print(text[:])
print(text)
print(len(text))
print(len(text.replace(" ", "")))

import math

x = 4
y = 3
z = 2
w = ((x + y * z) / (x * y)) **z
print(w)
print(math.ceil(w))
print(math.floor(w))

total = 485
tahun = total / 360 ; print(round(tahun, 2))
bulan = total / 30 ; print(bulan)
minggu = total / 360 ; print(minggu)
hari = total / 1 ; print(hari)

facebook = 'facebook\'s rating is'
fb_rating = 3.5
fb_rating_str = str(fb_rating)
print("i've known the rating of fb.", facebook, fb_rating)

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_1, row_2, row_3, row_4, row_5]
ratings_1 = row_1[3]
ratings_2 = row_2[3]
ratings_3 = row_3[3]

total = 

ratings = []
for row in app_data_set:
    rating = row[1]
    ratings.append(rating)
    sum(ratings)

total = sum(ratings) ; print(total)
average = total / len(app_data_set) ; print(average)
print(round(average, 2))

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

x = 3
x **= 2
print(x)

print('hello world')
name = 'Arian Rasyid'
number = 81294950683
height = 172.5
print('Hi, My name is %s. My number is %d. i\'m %f feet. How about you?' % (name, number, height))

name = "Gandalf"
extendedName = "the Grey"
age = 84
IQ = 149.9
print('type(name):', type(name)) #type(name): <class 'str'>
print('type(age):', type(age))   #type(age): <class 'int'>   
print('type(IQ):', type(IQ))     #type(IQ): <class 'float'>   

print('%s %s\'s age is %d with incredible IQ of %f ' %(name, extendedName, age, IQ)) #Gandalf the Grey's age is 84 with incredible IQ of 149.900000 

#Same output can be printed in following ways:


print ('{0} {1}\'s age is {2} with incredible IQ of {3} '.format(name, extendedName, age, IQ))          # with help of older method
print ('{} {}\'s age is {} with incredible IQ of {} '.format(name, extendedName, age, IQ))          # with help of older method

print("Multiplication of %d and %f is %f" %(age, IQ, age*IQ)) #Multiplication of 84 and 149.900000 is 12591.600000          


file = input("file apa yang mau dibuka? : ")
opened_file = input(open(file))

import pandas as pd
import numpy as np 

df=pd.read_csv(r"D:\M Arian Rasyid S\File Organization\Learning\Data Science\AppleStore.csv")
opened_file = open('D:\M Arian Rasyid S\File Organization\Learning\Data Science\AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

print(len(df))
print(df[0])
print(df[1:3])



while 


name = "not_aneta"

while name != "aneta":
    name = input("What is my name? ")

if name == "aneta":
    print("You guessed my name!")
print("hello")

onee = 3.43323232
one_decimal = format(3.4434333, '.1f') ; print(one_decimal)
import math
one = format(math.pi, '.2f') ; print(one)

def nama_hari(a, b, translate=True):
    a = [Senin, Selasa, Rabu, Kamis, Jumat, Sabtu, Minggu]
    b = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]
    if translate:
        return a.index(b)
    else:
        return b.index(a)

c = nama_hari(1, 1, translate= False) ; print(c)

def a_sum(a, b):
    tambahan = a + b
    # difference = a - b
    return tambahan

x = input('maen tebak2an nyok? :')
a = int(input('a itu breapa? : '))
b = int(input('b itu breapa? : '))
y = input("hasil penjumlahan dan pengurangannye berape tuh? : ")

if y == a_sum(a, b):
    print("pinter juge lu!")
else:
    print("yelah masa kaga tau?")
print(sum_and_difference(a, b))

a_list = [3, 4]
first_element, second_element = a_list
print(first_element)
print(second_element)
