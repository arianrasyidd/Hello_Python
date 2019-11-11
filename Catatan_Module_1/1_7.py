#Looping in Python

#For Loops and While Loops
kota = ['Jakarta', 'Surabaya', "Bandung"]
#* memakai for loops
for item in kota:
    print(item)
#** memakai while loops
i = 0
while i < len(kota):
    i += 1

for i in range(1, 11):
    if i % 2 == 0:
        print('WOW!')
    else:
        print(i)

#*** FizzBuzz
# def FizzBuzz(x):
#     for i in range(1, x+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print('FizzBuzz')
#         elif i % 3 == 0:
#             print('Fizz')
#         elif i % 5 == 0:
#             print('Buzz')
#         else:
#             print(i)
    
# FizzBuzz(150)

#* Untuk membalik list
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#? jadi [7, 6, 5, 4, 3, 2, 1]

# # 1.pake reverse
# x.reverse()
# print(x)

# # 2. Indexing
# print(x[::-1])

# # 3. reversed()
# print(list(reversed(x)))

#* My Answer
# def reverseList(x):
#     r = []
#     for i in x:
#         r.insert(0, i)
#     return r
# print(reverseList([8, 7, 6, 3, 4, 5]))

#* The Answer
# def balikPosisi(myList):
#     hasil = []
#     for i in range(len(myList)):
#         hasil.insert(0, mylist[i])
#     return hasil
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# y = ['Andi', 'budi', 'caca', 'kevin']
# print(balikPosisi(x))
# print(balikPosisi(y))


# def replacez(word, char1):
#     newString = ""
#     for next_char in word:              # for each character in the word
#         if next_char == 'a' or next_char == 'i' or next_char == 'u' or next_char == 'e':          # if it is the character you want to replace
#             newString += char1          # add the new character to the new string
#         else:                           # otherwise
#             newString += next_char      # add the original character to the new string
#     return newString

# replacez('muhammad arian rasyid', 'o')


#* Jawaban mas Lintang
# def ubahVokal(kata):
#     output = ''
#     for huruf in kata:
#         if huruf in 'aiueo':
#             output = output + 'o'
#         else:
#             output += huruf
#     return output

# print(ubahVokal('lintang'))
# print(ubahVokal('kambing'))


#Palindrome
# def palindrome(kata):
#     if kata == kata[::-1]:
#         return True
#     else:
#         return False
# print(palindrome('sore'))

# def palindrome2(kata):
#     for i in range(round(len(kata)/2)):
#         palindromekah = False
#         if kata[i] == kata[len(kata)-1-i]:
#             palindromekah = True
#         else:
#             palindromekah = False
#             break
#     return palindromekah
# palindrome2('malam')

kalimat = 'Hai aku Lintang'

def palindrome(kalimat):
    x = ''
    kata = kalimat.split()
    for i in kata:
        z = i[::-1] + ' '
        x += z
    return x

print(palindrome("Hai aku Lintang"))

