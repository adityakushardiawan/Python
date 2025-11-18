#import library 
import datetime
import string
import random
#Dictionary
student = {
    'name' : 'name',
    'address' : 'address',
    'grade' : 'grade',
    'birthdate' : datetime.datetime(1999,1,11)
}
data_student = {}
while True :
    print(f"=== Student Surabaya Cambridge School ===")
    print("="*30)
    #panggil data
    #variabel = dict.fromkeys(student.keys())
    std = dict.fromkeys(student.keys()) #untuk memanggil template
    #formula input dictionary 
    #variabel ['data'] = input("..........")
    std ['name'] = input("Input Full name:")
    std['address'] = input("Input Address:")
    std['grade'] =  int(input("Input grade:"))
    year = int(input("Input Year:"))
    month = int(input("Input Month:"))
    date = int(input("Input Date:"))
    std['birthdate'] = datetime.datetime(year,month,date)
    #untuk membuat id student
    KEY = ''.join((random.choice(string.ascii_uppercase)for i in range(6)))
    #menampilkan output tampilan 
    data_student.update({KEY:std})
    print(f"{'KEY':<6} {'name':<18} {'address':<50} {'grade':<20} {'birthdate':<10}")
    print("="*30)
    
    for b in data_student:
        KEY = b
        nama = data_student [KEY]['name']
        alamat = data_student [KEY]['address']
        kelas = data_student [KEY]['grade']
        tanggal_lahir = data_student [KEY] ['birthdate'].strftime("%x")
        print(f"{KEY:<6} {nama:<18} {alamat:<50} {kelas:20} {tanggal_lahir:<10}")
        
    print("\n")
    option = input("Continue ? (y/n)")
    if option == "n":
        break
print("Finish")