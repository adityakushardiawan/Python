 #Rumus For Loop
#For Var In Iterable
#while Var In Iterable

#var = Variabel Contoh nya I,E,Char & Tipe Data
#in = tempat variabel Var Contohnya Len,Range
#iterable = Objek Data Contoh Array,list dll

#Contoh
# while i<len(citylist):
#urutan 1 = while/for
#urutan 2 = variabel I
#urutan 3 = in / Len
#urutan 4 = iterable / citylist
#char/string = 
# character/string tipe data untuk teks/kalimat
#lower = Merubah huruf kapital ke kecil
#upper = Merubah huruf kecil ke Kapital
#ganjil ='1,3,5,7,9,'
#genap ='2,4,6,8,10'
nilai_awal = int(input(' nilai awal: '))
nilai_akhir = int(input(' nilai akhir: '))
jumlah_ganjil= 0
jumlah_genap=0

for x in range(nilai_awal,nilai_akhir +1 ):
    if (x % 2)== 0:
    #if int.lower() in ganjil:
        jumlah_genap += 1

    else:
        #if int.lower() in genap:
        jumlah_ganjil += 1
print ('Jumlah Bilangan Genap :',jumlah_ganjil)
print ('Jumlah Bilangan Ganjil :',jumlah_genap)
#Classwork 6/11
#Menampilkan Jumlah Huruf Konsonan Contoh B,C,D Dan Seterusnya
#Menampilkan Flowchart
#Menampilkan Jumlah Huruf Vokal & Jumlah Konsonan (+ Point)
#nama file : classwork2.py