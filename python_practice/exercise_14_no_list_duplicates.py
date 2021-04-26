#Write a program (function!) that takes a list and
#  returns a new list that contains all the 
# elements of the first list minus all the duplicates.
# Extras:
#Write two different functions to do this -
#  one using a loop and constructing a list, and another using sets.
def no_list_duplicate():
    L1=[]
    L2=[]
    User_number=int(input("Enter the number of elements you want in the list   "))
    if User_number <= 10:
        for _ in range(User_number):
            user_list_input=int(input("start entering the numbers :      "   ))
            L1.append(user_list_input)
        print("This is list number 1"+ str(L1)) 
        for Each_elements in L1:
            if Each_elements not in L2:
                L2.append(Each_elements)
        print("This is list number 2"+ str(L2))
        L3=set(L1)
        print("This is list number 3 using a set function"+ str(L3))
        return L2
    else:
        print(" Enter number under 10  please")

    

no_list_doubles= no_list_duplicate()



    
