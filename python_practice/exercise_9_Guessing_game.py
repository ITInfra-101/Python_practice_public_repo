# Python does not have a random() function to make a random number, 
# but Python has a built-in module called random that can be used to make random numbers:

# Extras:
#     Keep the game going until the user types “exit”
#     Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
User_Guess_count = 0
while True:
    random_num = float(random.randrange(1,10))
    User_Answer= input("Please enter a number between 1 to 9 :    ")
    if ((User_Answer=="exit") or (User_Answer=="")):
        print("The number of user guess is  {}".format(User_Guess_count))
        break
    else:
        User_Answer_Float=float(User_Answer)
        User_Guess_count+=1
        if (random_num==User_Answer_Float):
            print("The random number guessed by user is right")
        elif(random_num<User_Answer_Float):
            print("The random number guessed by user is greater than geenrated random number")
        elif(random_num>User_Answer_Float):  
            print("The random number guessed by user is less than genrated random number")
        else:
            print(User_Guess_count)   
    
        

        
        
    

