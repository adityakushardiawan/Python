print("=== Aplikasi Cinema XXI ===")
print("\n") #untuk merapikan / space kosong
movie = []
actor = []
category = []
year = []
#Function Show Data
def showdata():
    if len(movie) <=0: #len = jumlah data
        print("empty, please input data")
    else:
        for index in range(len(movie)):
            print("[", index, "]", movie[index],actor[index])
    # %d = untuk Id movie, %s = untuk nama movie, data lain

#Function Input Data
def input_data():
    movie2 = input("Input movie:")
    #Formula Insert = variabel awal.append(variabel input)
    movie.append(movie2)
#Function Edit Data 
def edit_data():
    showdata()
    index = int(input("Input ID movie:"))
    if (index > len(movie)):
        print("False ID")
    else:
        movie3 = input("Input New movie")
    movie[index] = movie3 #FORMULA edit
#Function Delete
def delete_data():
    showdata()
    index = int(input("Input ID movie:"))
    if (index > len(movie)):
        print("False ID")
    else:
        #formula delete = variabel.remove(variabel[index])
        movie.remove(movie[index])
#Function Option
def option():
    print("=== Select Option ===")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")
    
    movie = input("Select Option:")
    print("\n")
    if movie == "1":
        showdata()
    elif movie =="2":
        input_data()
    elif movie =="3":
        edit_data()
    elif movie =="4":
        delete_data()
    elif movie =="5":
        exit()
    else:
        print("False")
        
#Close untuk function 
if __name__ == "__main__":
    while(True):
        option()