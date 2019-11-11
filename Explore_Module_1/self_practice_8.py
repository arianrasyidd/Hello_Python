#* Palindrome
def palindrome(kalimat):
    x = ''
    kata = kalimat.split()
    for i in kata:
        z = i[::-1] + ' '
        x += z
    return x

print(palindrome("Hai aku Lintang"))

#**Morse Code
morse_code = {
'A' : '. _',           
'B' : '_ . . .',       
'C' : '. .   .',       
'D' : '_ . .',         
'E' : '.',             
'F' : '. - .',         
'G' : '_ _ .',         
'H' : '. . . .',       
'I' : '. .',           
'J' : '_ . _ .',       
'K' : '_ . _',         
'L' : '____',          
'M' : '_ _',           
'N' : '_ .',
'O' : '.   .',         
'P' : '. . . . .',
'Q' : '. . _ .',
'R' : '.   . .',
'S' : '. . .',
'T' : '_',
'U' : '. . _',
'V' : '. . . _',
'W' : '. _ _',
'X' : '. _ . .',
'Y' : '. .   . .',
'Z' : '.   . . .',
'1' : '. _ _ .',       
'2' : '. . _ . .',     
'3' : '. . . _ .',     
'4' : '. . . . _',
'5' : ' _ _ _',
'6' : '. . . . . .',
'7' : '- - . .',
'8' : '_ . . . .',
'9' : '_ . . _',
'0' : '_______'
}

i = {}
a = input('Nama kamu siapa? ')
b = keys(nama)
def morse():
    for key in morse_code:
        i.values(nama)
    return i

#** ChaesarChiper

"-----------------------------------------------------------------------------------------------------------------------------"

'''
# bikin half pyramid
def bintang(x):
    star = ''
    for i in range(x):
        star += ' * '
        print(star)

bintang(5)

# bikin inverted half pyramid
def rStar(x):
    star = ''
    for i in range(x):
        star = ' * ' * (x - i)
        print(star)

rStar(5)

# bikin half pyramid tapi angka
def pirAng (x):
    angka = ''
    for i in range(x):
        angka += str(i+1) + ' '
        print(angka)

pirAng(5)
'''
# bikin inverted half pyramid angka
def rPirAng(x):
    k = x
    angka = ''
    for i in range(x):
        for j in range(k):
            angka += str(j+1)
        print(angka)

rPirAng(5)
'''
# bikin half pyramid angka berulang
def pirAngUl (x):
    angka = ''
    for i in range(x):
        angka = str(i+1) * (i+1)
        print(angka)

pirAngUl(5)

# bikin inverted half pyramid angka berulang
def rPirAngUl (x):
    angka = ''
    for i in range(x):
        angka = str(i+1) * (x - i)
        print(angka)

rPirAngUl(5)

# bikin half pyramid inverted angka
def PirRAng (x):
    angka = ''
    for i in range(x):
        angka += str(x - i) + ' '
        print(angka)

PirRAng(5)
'''
# bikin inverted half pyramid inverted angka