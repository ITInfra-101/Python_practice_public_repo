# Write a password generator in Python. 
# Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, 
# uppercase letters, numbers, and symbols. The passwords should be random, 
# generating a new password every time the user asks for a new password. 
# Include your run-time code in a main method.
# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

def pass_gen_basic():
    import random
    List_of_special_symbols=['|', '^', '&', '+', '-', '%', '*', '/', '=', '!', '>']
    List_of_alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ns=(input("Enter the number of random symbols you want in the generated password from 3 to 5    "))
    nl=(input("Enter the number of alphabets you want in the generated password from 5 to 10         "))
    nn=(input("Enter the number of numbers user wants in the generated password  from 4 to 8         "))
    try:
        ns=int(ns)
        nl=int(nl)
        nn=int(nn) 
        if((ns>=3 and ns<=5) and (nl>=5 and nl<=10) and (nn>=4 and nn<=8)):
            List_of_password_special_chars=[]
            for _ in range(0,ns):
                rand_symbol=random.choice(List_of_special_symbols)
                List_of_password_special_chars.append(rand_symbol)
            List_of_password_alphabets=[]
            for _ in range(0,nl):
                rand_letters=random.choice(List_of_alphabets)
                List_of_password_alphabets.append(rand_letters)
            List_of_numbers=[]
            for _ in range(0,nn):
                n1= random.randrange(0,100)
                List_of_numbers.append(n1)
            User_password=[List_of_password_special_chars,List_of_password_alphabets,List_of_numbers]
            str_special=str(User_password[0])
            str_char=str(User_password[1])
            str_num=str(User_password[2])
            str_special_x=str_special.strip("[]',")
            str_char_x=str_char.strip("[]',")
            str_num_x=str_num.strip("[]',")
            super_password=str_char_x+" "+str_num_x+" "+str_special_x
            super_password_1=super_password.replace(','," ")
            super_password_2=super_password_1.replace("'","")
            super_password_final=super_password_2.replace(" ","")
            print("The generated password is  :" + super_password_final)
            while True:
                pass_gen_basic()
                return super_password_final
    except:
        print("**********************************INVALID INPUT*******************************************")

generate_password=pass_gen_basic()

