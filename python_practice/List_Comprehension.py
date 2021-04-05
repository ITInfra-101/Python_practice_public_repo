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