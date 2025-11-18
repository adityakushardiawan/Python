age = input("Berapa Umur Anda :")

if age<='25':
    
    if age<='17':
        print ("Anda Masih Sekolah") #1-17 tahun
    else:
        print ("Anda Masih Mahasiswa") #18-25tahun

elif age>='25':
    
    if age>='50':    
        print ("Anda Sudah Lanjut Usia") #50 Tahun keatas
    else:
        print ("Anda Sudah Orang Tua/Parents") #26-50 Tahun
else :
    print ("Error")