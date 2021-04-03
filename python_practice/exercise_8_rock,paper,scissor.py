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
    