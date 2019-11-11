#* cara 1
for i in range(2, 10):
    print(i)
    if i == 7:
        break
else:
    print('OK')

#* cara ke 2
for i in range(2, 10):
    if i == 7:
        break
    print(i)
else:
    print('OK')

#* cara ke 3
for i in range(2, 10):
    if i == 7:
        continue
    print(i)
else:
    print('OK')


for i in range(2, 10):
    print(i)
    if i == 7:
        continue
else:
    print('OK')


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
# print(morse_code)
i = {}
a = input('Nama kamu siapa? ')
b = keys(nama)
def morse():
    for key in morse_code:
        i.values(nama)
    return i



        



print()
print(morse_code['A'], morse_code['R'], morse_code['I'], morse_code['A'], morse_code['N'])