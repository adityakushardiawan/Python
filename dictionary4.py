import string
import random
restaurant_template ={
    'name' : 'name',
    'address' : 'address',
    'category' : 'category',
}

data_restaurant ={}
while True: 
    
    print(f"{'Welcome':^20}")
    print(f"{'Restaurant In Surabaya':^20}")
    print("-"*20)

    restaurant = dict.fromkeys(restaurant_template.keys())
    restaurant['name'] = input("Restaurant Name :")
    restaurant['address]'] = input("Restaurant Address :")
    restaurant['category'] = input("Restaurant Category :") 
    
    #KEY = ''.join((random.choice(string.ascii_uppercase)for i in range(6)))
    KEY = ''.join((random.choice(string.ascii_uppercase)for i in range(6)))
    data_restaurant.update({KEY:restaurant})
    print(f"{'KEY':<6} {'name':<18} {'address':<10} {'category':<10}")
    print("="*50)
    
    
    for b in data_restaurant:
        KEY = b
        nama = data_restaurant[KEY]['name']
        alamat = data_restaurant[KEY]['address']
        #nomor = int=data_restaurant[KEY]['number']
        kategori = data_restaurant[KEY]['category']
        print(f"{KEY:<6} {nama:<18} {alamat:<10} {kategori:<10}")
        
        #print(f"{KEY:<6} {nama:<18} {alamat:<10} {nomor:<10} {kategori:<10}") 
    
    print("\n")
    is_done = input("Continue (y/n)?")
    if is_done =="n":
        break
print("\Finish")   
    