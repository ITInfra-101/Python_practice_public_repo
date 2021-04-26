# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
# and makes a new list of only the first and last elements of the given list. 
# For practice, write this code inside a function.

def list_ends():
    import random
    user_number=int(input("Enter the number of items you want in a list     :"))
    User_list=[]
    for each_element in range(0, user_number):
        each_element=random.randrange(0,999)
        User_list.append(float(each_element))
    print("The user generated list is :     "+str(User_list))

    New_list=[User_list[0],User_list[-1]]
    print("The lists made of first and last element of the list is :" + str(New_list))
    return New_list


List_created=list_ends()


