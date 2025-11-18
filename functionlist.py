# Memasukkan data
def data (name,height,weight):
    print(f"{name} mempunyai tinggi {height} cm dan berat badan {weight} kg")
data2 = input("Input name:")
data3 = input("Input height:")
data4 = input("Input weight:")
data (data2,data3,data4)
#name = input("Input name")
#height = input("Input height")
#weight = input("Input weight")
def fungsi (data_list):
    data = data_list.copy()
    name = data [0]
    height = data [1]
    weight = data [2]
    print(f"{name} mempunyai tinggi {height} cm dan berat badan {weight} kg")
fungsi(["bryan",190,76]) 
#function *args
# *args = arguments / **kwargs = keyword arguments
# Function *args = variabel yang digunakan untuk membuat parameter menjadi tuple
# Kapan menggunakan args :
# 1. mendefinisikan suatu fungsi
# 2. memanggil suatu fungsi    
def fungsi2 (*args):
    name = args [0]
    height = args [1]
    weight = args [2]
    print(f"{name} mempunyai tinggi {height} cm dan berat badan {weight} kg")
fungsi2 ("dom",200,80)

def tambah(*data):
    output = 0
    for angka in data:
        output += angka
        
    return output
hasil = tambah(1,2,3,4,5)
print(f"Hasil = {hasil}" )

