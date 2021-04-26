#Displaying divisors for user input number of integer type
number=int(input("Please enter a number :   "))
list_of_numbers_till_specified_number = range(1,number)
list_of_divisors = []
for each_number in list_of_numbers_till_specified_number:
    if (number%each_number)==0:
        list_of_divisors.append(each_number)
    
print(list_of_divisors)


#Displaying divisors for user input number of float type
list_of_divisors_using_float =[]
number_float=float(input("Please enter a floating point number :   "))
x=1.0
while x!=number_float:
    if (float(number_float%x))==0:
        list_of_divisors_using_float.append(x)
    x+=1
print(list_of_divisors_using_float)

