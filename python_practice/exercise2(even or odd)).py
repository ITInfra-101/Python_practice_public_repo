number = float(input("Enter a number :    "))
if number%4 == 0:
    print("The number is a multiple 4") 
elif number%2 == 0:
    print("The number is an even number")    
else:
    print("The number is an odd number") 

check = float(input("Enter a number to be divided by :    "))

if number%check == 0:
    print(" The number got divided evenly!! spliced it up real good !!")
else:
    print("The number didnt get divided evenly !!")    