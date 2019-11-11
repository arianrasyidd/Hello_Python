#bikin fungsi yang tugasnya remove duplicate huruf
inputUser = input('Masukan nama : ')
name = set(inputUser)
print(name)
nameList = sorted(list(name))
print(nameList)

newString = ''
for i in inputUser:
    if i in nameList:
        i = '*'
        newString += i
    else:
        newString += i

print(newString, 'abc')

