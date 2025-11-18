#program Logika Nested For
print('Segitiga 1')
rows = 5
#outer loop/outer for
for x in range(0, rows):
#prses iterasi Jumlah Rows
    for y in range(0, x + 1):#proses +1
        print("*", end='')#proses cetak *
    rows +=1
    print('')

print('Segitiga 2')
rows = 5
for x in range(0, rows):
    for y in range(0, rows - 1):
        print("*", end='')
    rows -= 1
    print('')
    
print('\n\n5')
a = 5
s = a - 1 # for spaces
for i in range(0, a):
    for j in range(0, s):
        print(' ', end='')
    s -= 1
    for j in range(0, i + 1):
        print('* ', end='')
 
    print('')
 
print('\n\n6')
a = 5
s = 0 # for spaces
for i in range(0, a):
    for j in range(0, s):
        print(' ',end='')
    s += 1
    for j in range(0, a):
        print('* ' , end='')
    a -= 1
    print('')