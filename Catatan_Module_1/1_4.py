#Data Type

#*perbedaan list, tuple dan set
a = (1, [
        'a', 'b', 'c'
    ], 3,
    {4, 5, 6}, [7, d])
List
x = [1, 2, 3, 4, 5, 6]
Tuple
y = (1, 2, 3, 4, 5, 6)
Set
z = {1, 2, 3, 4, 5, 6, 2, 5, 9}

#penjelasan dari set
'''
1. no indexing
2. duplicate elements not allowed 
3. set muttable, tp elemen2nya immutable atau gabisa dirubah
'''

#Set Function
z = {1, 2, 3, 4, 5, 6, 2, 5, 9}
print(len(z))
print(z)
print(set(x))
z.add([9, 8, 7])
print(z)

z.update('andi')
print(z)

z.update('Andi')
print(z)

z.update([6, 7, 8])
print(z)

z.update ({'z', 'budi'})
print(z)

z.remove('budi')
z.discard('deni')
print(z)

z.pop()
print(z)

#Diagram venn sign
sign = '''
buat cari irisan di set pake fungsi intersection atau pake tanda (&)
 buat cari gabungan di set pake fungsi union, atau pake tanda | (garis lurus)
buat cari selisih di set pake fungsi difference, atau pake tanda - (kurang)
buat cari selain irisan di set pake fungsi intersection atau pake tanda ^ (yaitulah pokonya)
'''

#* Contoh soal
p = {1, 2, 4, 7, 9, 19}
q = {7, 9, 8, 19, 6, 5, 12, 16, 17}
r = {3, 8, 6, 19}

print(p & q)
print(p & q & r)
print(p & q | r )
print(p - q | r)
print(p ^ q & r)

s = print(set(range(-9, 11)))
p = print(set(range(-4, 5)))
q = print(set(range(-7, 2)))
r = print(set(range(-1, 8)))
print(p|q, p|r, q|r)

mySet = {2, 3, 1, 8, 6}
mySet= list(mySet)
print(mySet)


x = set([1, 2, 3])
y = frozenset([1, 2, 3]) #frozenset adalah set yang immutable