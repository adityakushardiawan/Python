#funtion untuk view data
print("===Aplikasi Restaurant===")
#book = [] # judul buku
#resto = []
food=[] # nama menu
price = [] # harga
drink =[]
priceminum2 =[]

def showdata():
    if len(food)<= 0:
        print("empty")
    else:
        for f in range(len(food)) :
            print("==Food List==")
            print ("[",f,"]",food[f],",",price[f])
def showdatadrink():
    if len(drink)<= 0:
        print("empty")
    else:
        for d in range(len(drink)) :
            print("==Drink List==")
            print ("[",d,"]",drink[d],",",priceminum2[d])

def insertdata():
    food2 = input("Food Name:")
    price2 = input("price:")
    food.append(food2) 
    price.append(price2)
    
def insertdatadrink():
    drink2 = input("Drink Name:")
    pricedrink2 = input("price:")
    drink.append(drink2) 
    priceminum2.append(pricedrink2)
    
def editdata():
    showdata()
    f = int(input("Id Food:"))
    if (f > len(food)):
        print("False Id")
    else:
        food3 = input("New Food Name:")
        price3 =  int(input("New Food Price: "))
    food[f] = food3 
    price[f] =price3

def editdatadrink():
    showdata()
    d = int(input("Id Drink:"))
    if (d > len(drink)):
        print("False Id")
    else:
        drink3 = input("New Drink Name:")
        pricedrink3 =  int(input("New Drink Price: "))
    drink[d] = drink3 
    priceminum2[d] =pricedrink3
    
def deletedata():
    showdata()
    f = int(input("Id Food:"))
    if (f > len(food)):
        print("False Id")
    else:
        food.remove(food[f])
        price.remove(price[f])

def deletedatadrink():
    showdatadrink()
    d = int(input("Id Drink:"))
    if (d > len(drink)):
        print("False Id")
    else:
        drink.remove(drink[d])
        priceminum2.remove(priceminum2[d])
        
def optiondrink():
    print("\n") #Memberikan space (enter)
    print("Menu Drink [Option menu food choose number 1]")
    print("Select Option?")
    print("[1] Menu Food")
    print("[2] Show data drink")
    print("[3] Insert Drink")
    print("[4] Edit Drink")
    print("[5] Data Drink")
    print("[6] Exit")
    
    drink = input("Select Option?") 
    print("\n")
    if drink =="1":
        showdata()
    elif drink =="2":
        showdatadrink()
    elif drink =="3":
        insertdatadrink()
    elif drink =="4":
        editdatadrink()
    elif drink =="5":
        deletedatadrink()  
    elif drink =="6":
        exit()
    else :
        print ("False Option !!")  

def optfood():
    print("\n") #Memberikan space (enter)
    print("Menu Food [Option menu Drink choose number 6]")
    print("Select Option Data Food?")
    print("[1] Show Data Food")
    print("[2] Insert Food")
    print("[3] Edit Food")
    print("[4] Delete Food")
    print("[5] Exit")
    print("[6] Option Data Drink")
    
    food = input("Select Option?") 
    print("\n")
    if food =="1":
        showdata()
    elif food =="2":
        insertdata()
    elif food =="3":
        editdata()
    elif food =="4":
        deletedata()  
    elif food =="5":
        exit()
    elif food=="6":
        optfood()
    else :
        print ("False Option !!")
          
while (True) :
    optfood() 
    