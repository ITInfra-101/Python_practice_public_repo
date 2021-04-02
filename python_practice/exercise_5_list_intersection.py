import random
L1=[2,3,5,6,7,8,9,0,"JRE"]
L2=[1,3,5,6,7.99,4.4,9,0,"LFP"]
L3=list(set(L1) & set(L2))
print("Values from List 1  :{}".format(L1))
print("Values from List 2  :{}".format(L2))
print("Values from List 3 : {}".format(L3))
#Generating list based on comman elelents in ONE LINE
L_One_1=[2,3,5,6,7,8,9,0,"JRE"]
L_One_2=[1,3,5,6,7.99,4.4,9,0,"JRE"]
L_One_3 = [each_element for each_element in L_One_1 if each_element in L_One_2]
print("Common elements from One line logic generated list {}".format(L_One_3))
#Generating random lists and displaying their common elements 
RL1 = []
for e1 in range(0,7):
    e1 = random.randrange(1,888)
    RL1.append(e1)
print(RL1)

RL2 = []
for e2 in range(0,7):
    e2 = random.randrange(1,888)
    RL2.append(e2)
print(RL2)

RL3 = list(set(RL1) & set(RL2))
print("The value the intersection of RL3    {}".format(RL3))