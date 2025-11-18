 # Function =  Sekumpulan code yang digabungkan menjadi 1 lalu
 # dipanggil kembali
 # Penulisan Function = def
 # Parameter = variabel yang memiliki nilai di function
 
 # Formula / Rumus function tanpa parameter
 #def variabel():
 #print("text 1")
 #variabel()
 
# Formula / Rumus function parameter
# def variabel(variabel parameter):
#print (variabel parameter)
#variabel("text 2")

#function tanpa parameter
def c(): #variabel untuk function
    print("Hello Grade 10 D")
c() #pemanggilan variabel

#function parameter
def n(ucapan): #ucapan = parameter
    print(ucapan)
n("Happy New Year 2025") #n = pemanggilan variabel

#function & operator
def luas_segitiga(base,height):
    area = (base*height) / 2
    print("Luas Segitiga : %f" %area) # %f = untuk format decimal
luas_segitiga(5,10) # 5 = base , 10 = height

def circle(radius):
    area = 3.14 * radius**2
    perimeter = 2 * 3.14 * radius
    print("Luas Lingkaran : %f" %area)
    print("Keliling Lingkaran : %f" %perimeter)
circle(7) #7 adalah nilai radius