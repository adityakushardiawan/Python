#Loop di Python
# For Loop = Jumlah loop sudah ditentukan
# While Loop = Jumlah loop belum ditentukan
# Formula :
# For : For Variable in iterable / location
# While : while variable condition 
print ("While Loop")
number = int(input("input start number:"))
#formula while 
while number <5: # <5 = condition
    number +=1  #untuk proses pindah ke next number 1,2,3,4,5
    print(f"Nomor saat ini -> {number}")
print("finish program")
print("="*30)


print("Aplikasi 2 Menghitung Average")
#list = sekumpulan data di aplikasi , list = [ ]
# [ ] = list, array menyimpan data
# { } = menampilkan hasil formula
# ( ) = untuk output
data = [4,8,12,16] # <- list
#urutan=0,1, 2, 3 
j = 0 # j = variabel u/ urutan id
sum = 0 #0 karena belum ada addition number
while j < len(data): #len = jumlah banyaknya data
    sum += data [j] #proses addition masing" data
    j +=1 #u/ perpindahan posisi data
avg = sum / len(data)
print("Nilai Average:",avg)


print ("="*3)
print ("Aplikasi 3 , Mencari nama kota")
data2 = ["Surabaya","Jakarta","Denpasar","Malang"]
city = input("Input City Name:")
c = 0 
while c <len(data2):
    if data2[c].lower() == city.lower():
    # cek sama nama input dengan nama kota di list database
        print("nama kota ada di urutan ->",c)
        break #untuk mengakhiri program
    print("False",data2[c])
    c+=1