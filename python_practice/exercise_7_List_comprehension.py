#Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
# Write one line of Python that takes this list a and 
# makes a new list that has only the even elements of this list in it.
#Logic 2 list comprehension
a1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# User_input_number=int(input("Enter a number till which the list should be displayed  :      "))
# a12=a1[0:User_input_number]
# length_of_a1=len(a1)
b1 = [each_element for each_element in a1 if (each_element%2)==0]
c1 =[each_element for each_element in a1 if (each_element%2)!=0]
print("The whole big list is {}    ".format(a1))
print("The list is made of even numbers of big list  {}    ".format(b1))
print("The list is made of odd numbers of big list  {}    ".format(c1))
