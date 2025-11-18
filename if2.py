print("=== Odd & Even Number ===")
#Input Manual
number = int (input("Input Number:"))
if number == 1:
    print(number,"Odd Number")
elif number == 3:
    print(number,"Odd Number")
else:
    print(number,"Even Number")
#Input Otomatis
print("==================")
print("Input otomatis")
number2 = int(input("Input Number :"))
if (number2 % 2) == 0: # %2 = : 2
    print("{0} even number".format(number2))
else:
    print("{0} odd number".format(number2))
print("="*30)
print("Aplikasi Kategori Umur")
age = input("Input Age:")
if age <='25': # kurang dari 25 tahun
    if age <='17': #nested if (if di dalam if)
        print ("Anda masih sekolah")
    else: # usia 18-25
      print("Anda sudah di university")
elif age >='25': # lebih dari 25 tahun
    if age >='50': #nested if (if di dalam if)
        print ("Anda sudah lansia ") #diatas 50 tahun
    else: # usia 26 - 50 tahun
        print("Anda sudah menjadi orang tua / parents")  
else :
    print("Error")  
