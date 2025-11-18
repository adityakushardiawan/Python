print(" ODD & EVEN Number ")
first_number = int(input("Input First number:"))
last_number = int(input("Input Last number:"))
jumlah_odd = 0
jumlah_even = 0
#formula for loop
# For variable in iterable 
for i in range(first_number,last_number +1):
    if (i % 2) == 0: 
        jumlah_even += 1
    else:
        jumlah_odd +=1
print("Jumlah Odd :",jumlah_odd)
print("Jumlah even:",jumlah_even)

#Note u/ flowchart diagram 
# Elips : untuk start & finish program
# Paralellogram : untuk input & output 
# Diamond : untuk if,else,nested if 
# Circle : loop, for loop,while loop
# rectangle : untuk process , formula, rumus 