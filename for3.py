print ("== For / Nested For Python")
print("="*20)
print("== Segitiga 1 ==")
row = int(input("Input Row:"))
for i in range(1, row+1):
    print(i *"*")
print("="*20)
print("== Segitiga 2 ==")
# *****   1 ->   5
# ****    2->    4  = formula = row-i + 1
# ***     3->    3
# **      4->    2
# *       5->    1
for j in range(1,row+1):
    print((row-j+1) * "*")
    
print("="*20)
print("===  Segitiga 3 ===")
#    *      # 1 ->1 
#   ***     # 2 ->3 formula = 2*k-i
#  *****    # 3-> 5 
#*********  # 5-> 7
for k in range(1,row+1):
    print((row-k)* " "+(2*k-1)*"*")
        #untuk space     #untuk star
print("="*20)
# *******   #1 -> 5
#  *****    #2 -> 4
#   ***     #3 -> 3
#    *      #4 -> 1
print("Segitiga 4")
a= 5
s= 0
for m in range(0,a):
    for n in range(0,s):
        print(" ",end="") #untuk space kosong
    s +=1
    for o in range(0,a):
        print("*",end="") #untuk star
    a -=1
    print("")    