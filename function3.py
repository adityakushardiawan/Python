#Function header
def header():
    '''function header'''
    print(f"{'Aplikasi Circle & Cone'}")
    print(f"{'='*40}")
#Function Input Number
def input_number():
    radius = float(input("Radius:"))
    height = float(input("Height:"))
    return radius,height
#Function Area
def area(radius):
    return 3.14*radius**2
#function perimeter
def perimeter(radius):
    return 2*3.14*radius
#function volume cone
def volume(radius,height):
    return 1/3*height*3.14*radius**2

while True:
    header()
    r,h = input_number() #untuk function input number
    luas = area(r)
    keliling = perimeter(r)
    volum = volume(r,h)
    print(f"Area Circle : {luas}")
    print(f"Perimeter Circle : {keliling}")
    print(f"Volume Cone : {volum}")
    
    option = input("Optin Y or N for Continue?")
    if option =="N":
        break
print("Thank You")