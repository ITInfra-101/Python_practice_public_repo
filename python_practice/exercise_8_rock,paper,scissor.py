# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, 
# and ask if the players want to start a new game)

# Remember the rules:

#     Rock beats scissors
#     Scissors beats paper
#     Paper beats rock

while True:
    User_input_1 = input("Enter Rock or Paper or Scissor for USER 1 : ")
    User_input_2 = input("Enter Rock or Paper or Scissor for USER 2 : ")
    User_input_1=User_input_1.lower()
    User_input_2=User_input_2.lower()
# print(User_input_1)
# print(User_input_2)
    if ((User_input_1=="rock") & (User_input_2=="rock")) or ((User_input_1=="scissor") & (User_input_2=="scissor")) or ((User_input_1=="paper") & (User_input_2=="paper")):
        print("Its both the same object cannot process")

    elif ((User_input_1=="rock") & (User_input_2=="scissor")) or ((User_input_1=="scissor") & (User_input_2=="paper")) or ((User_input_1=="paper") & (User_input_2=="rock")):
        print(" User 1 won")

    elif ((User_input_1=="scissor") & (User_input_2=="rock")) or ((User_input_1=="paper") & (User_input_2=="scissor")) or ((User_input_1=="rock") & (User_input_2=="paper")):
        print(" User 2 won")

    else:
        (User_input_1 == "") & (User_input_2 =="")
        break
