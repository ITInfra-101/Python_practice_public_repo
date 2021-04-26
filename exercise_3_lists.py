random_numbers = [100,165,3,4.98,66.77,2]
for each_number in random_numbers:
    if each_number<=5:
        print("These numbers are less than 5 :{}".format(each_number))

# #Instead of printing the elements one by one, 
# # make a new list that has all the elements less than 5 from this list in it and 
# # print out this new list.

random_numbers = [100,165,3,4.98,66.77,2]
less_than_the_number=[]
n=0
for each_number in random_numbers:
    if each_number<=5:
        less_than_the_number.append(each_number)
        
print(less_than_the_number)

# Write this in one line of Python.
print([num for num in random_numbers if num < 99])

# Ask the user for a number and return a list that contains only elements from the 
# original list a that are smaller than that number given by the user.
user_number=float(input("Please enter a number:    "))
user_list=[]
for each_number in random_numbers:
    if each_number<=user_number:
        user_list.append(each_number)

print(user_list)
        

