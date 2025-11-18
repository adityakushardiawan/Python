print ("== Aplikasi Penerimaan Pramugari Pesawat")
print("Requirement:")
print("1. Age : Minimum Age 17 Years ")
print("2. Height : Minimum Height 160 cm ")
print("3. Toefl Score : Minimum 500 ")
print("4. Myopia / Mata Minus : Maximum 3 ")
print("5. Weight : Maximum 70Kg ")
print("==================================")
name = input ("Input Full Name :")
age = int (input("Input Age:"))
height = int (input("Input Height:"))
fs = int (input("Input Toefl Score:"))
e = int (input("Input Myopia / Mata minus :"))
c = int (input("Input Weight:"))
#Persyaratan 1
if age >=17:
    if height >=160: #persyaratan 3
        if fs >=500:
            if e <=3:
                if c<=70:
                    print("Congrats",name,"Anda Diterima Jadi Pramugari")
                else:
                    print("Sorry",name,"Chinese Score belum memenuhi kriteria")
            else:
                print("Sorry",name,"Englsih Score belum memenuhi kriteria")
        else:
            print("Sorry",name,"Final Score belum memenuhi kriteria")
    else:
        print("Sorry",name,"Tinggi belum memenuhi kriteria")
else : 
    print("Sorry",name,"Coba di tahun depan")
