# Take two lists, say for example these two:
# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists
#  (without duplicates). Make sure your program works on two lists of different sizes. 
# Write this in one line of Python using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).
import random
Random_list_1 = []
Random_list_2 = []

for e1 in range(0,7):
    e1 = random.randrange(1,888)
    Random_list_1.append(e1)
print("This is randomly genrated list 1 "+ str(Random_list_1))


Random_list_2 = []
for e2 in range(0,7):
    e2 = random.randrange(1,888)
    Random_list_2.append(e2)
print("This is randomly genrated list 2 "+ str(Random_list_2))

Random_list_3=[]
for x in Random_list_1:
    if x in Random_list_2:
        Random_list_3.append(x)
print("This is randomly genrated list 3 "+ str(Random_list_3))
        
Random_list_4=list(set(Random_list_1) & set(Random_list_2))
print(Random_list_4)