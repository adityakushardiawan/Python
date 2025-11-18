print("===  Aplikasi sisuca ===")
print("="*30)
print("Max Percobaan = 5")
#email &password 
list_username = ["scs","cambridge"]
list_password =["123","scs"]
#percobaan login
percobaan = 0
max_percobaan = 3
while percobaan < max_percobaan:#while 0 < 3:
    print("\n Percobaan ke =",percobaan+1)
    username = input("input username :")
    password = input("input password:")
    if username in list_username:
        index_user = list_username.index(username)        
        if password == list_password[index_user]:
            print("Login berhasil,selamat datang di sisuca")
            break #u/ keluar dari loop
        else:
            print("Password salah")
    else:
        print("username tidak ditemukan")
    percobaan +=1
else: 
    print("\n Kesempatan login sudah habis, akun diblokir")
print("Finish program")