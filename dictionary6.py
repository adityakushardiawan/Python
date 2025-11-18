import datetime
import string
import random

transaction_template ={
    'book' : 'book',
    'category' : 'category',
    'member' : 'member',
    'total' : 'total',
    'borrow_date' : datetime.datetime(1999,1,11)
}

data_transaction ={}
while True: 
    
  
    print(f"{'Transaksi Library SCS':^20}")
    print("-"*20)

    trans = dict.fromkeys(transaction_template.keys())
    trans['book'] = input("Book Name :")
    trans['category'] = input("Category :")
    trans['member'] = input("Member Name :")
    trans['total'] = int(input("Total :"))
    year = int(input("Year(YYYY):"))
    month = int(input("Month(1-12):"))
    date = int(input("Date(1-31):"))
    trans['borrow_date'] = datetime.datetime(year,month,date)
    
    KEY = ''.join((random.choice(string.ascii_uppercase)for i in range(6)))
    
    data_transaction.update({KEY:trans})
    print("========================== Output Data Peminjaman Library SCS ========================")
    print(f"{'KEY':<6} {'book':<18} {'category':<10} {'member':<18} {'total':<10} {'borrow_date':<10}")
    print("="*80)
    
    for b in data_transaction:
        KEY = b
        prod = data_transaction[KEY]['book']
        harga = data_transaction[KEY]['category']
        cust = data_transaction[KEY]['member']
        diskon = data_transaction[KEY]['total']
        lahir = data_transaction[KEY]['borrow_date'].strftime("%x")
        print(f"{KEY:<6} {prod:<18} {harga:<10} {cust:<18} {diskon:<10} {lahir:<10}") 
    
    print("\n")
    is_done = input("Continue (y/n)?")
    if is_done =="n":
        break
print("\Finish")   
    