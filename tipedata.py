#Jenis tipe data di python
# Integer / int = number (bilangan bulat)
# Float = Decimal number
# String / str = text,huruf,number
# Boolean = option true / False
calculator = float (input("Input Number :"))
height = float (input("Input height :"))
age = int (input("Input Age:"))
address = input("Input Address:")
full_name = str(input("Input Full name:"))
print("Height:",height)
print("Age",age)
print("Address:",address)
print("Full Name:",full_name)

print ("="*30)
print ("=== Operator Matematika ===")
print ("="*30)
print ("Area Rectangle")
#formula area : panjang * lebar 
panjang = float (input("Input Panjang :"))  
lebar = float (input("Input Lebar:"))
area = float(panjang) * float(lebar)
#output jawaban
print(f"Area Rectangle {area} cm") 
#f = untuk memanggil/konversi number 