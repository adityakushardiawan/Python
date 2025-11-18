print("Function Return")
print("="*30)
#Return = mengambil nilai / rumus dari function
#Formula Function Return
# def variable1 (parameter):
# variable2 = body function : formula / rumus
# return variable2
# variable2 = variable1(value)
# print (variable2)
def math1(number): #math1 = variable 1
    math2 = number **2 #body, **kuadrat/pangkat
    return math2 #math2 = variable 2
m3 = math1(10) #m3 = variable 3
print(m3)
print("="*30)
print("Kalkulator Function")
def math4(number1,number2):
    addition = number1 + number2
    substraction = number2 - number1
    multiplication = number1 * number2
    division = number2 / number1
    return addition,substraction,multiplication,division
a,s,m,d = math4(5,10) #5 = number1, 10 = number2
print(f"Addition:{a}")
print(f"Substraction:{s}")
print(f"Multiplication:{m}")
print(f"Division:{d}")
#Classwork Function 
#Buat new file (nama file: cwfunction.py)
# buat aplikasi function untuk menghitung
# 1. Volume Cuboid (panjang * lebar * tinggi)
# 2. Volume Cube (sisi * sisi * sisi)
# 3. Area Circle (3.14 * radius * radius)
# 4. Area Square (sisi * sisi)
