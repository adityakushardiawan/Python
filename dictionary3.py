import datetime
import string
import random

transaction_template ={
    'product' : 'product',
    'price' : 'price',
    'member' : 'member',
    'discount' : 'discount',
    'trans_date' : datetime.datetime(1999,1,11)
}

data_transaction ={}
while True: 
    
  
    print(f"{'Transaksi MC Donalds':^20}")
    print("-"*20)

    trans = dict.fromkeys(transaction_template.keys())
    trans['product'] = input("Product Name :")
    trans['price'] = int(input("Price :"))
    trans['member'] = input("Member Name :")
    trans['discount'] = int(input("Discount :"))
    year = int(input("Year(YYYY):"))
    month = int(input("Month(1-12):"))
    date = int(input("Date(1-31):"))
    trans['trans_date'] = datetime.datetime(year,month,date)
    
    KEY = ''.join((random.choice(string.ascii_uppercase)for i in range(6)))
    
    data_transaction.update({KEY:trans})
    print("========================== Output Data Transaksi MCD =========================")
    print(f"{'KEY':<6} {'product':<18} {'price':<10} {'member':<18} {'discount':<10} {'trans_date':<10}")
    print("="*80)
    
    for b in data_transaction:
        KEY = b
        prod = data_transaction[KEY]['pro duct']
        harga = data_transaction[KEY]['price']
        cust = data_transaction[KEY]['member']
        diskon = data_transaction[KEY]['discount']
        lahir = data_transaction[KEY]['trans_date'].strftime("%x")
        print(f"{KEY:<6} {prod:<18} {harga:<10} {cust:<18} {diskon:<10} {lahir:<10}") 
    
    print("\n")
    is_done = input("Continue (y/n)?")
    if is_done =="n":
        break
print("\Finish")   
    