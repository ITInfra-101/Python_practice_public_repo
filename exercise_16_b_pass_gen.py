# Write a password generator in Python. 
# Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, 
# uppercase letters, numbers, and symbols. The passwords should be random, 
# generating a new password every time the user asks for a new password. 
# Include your run-time code in a main method.
# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
def pass_gen_basic_v_2():
    import random
    List_of_password_components=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '|', '^', '&', '+', '-', '%', '*', '/', '=', '!', '>',0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
        22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 
        55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88,
        89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    user_num=input("Please enter the number of characters you want in a password ")
    try:
        user_num=int(user_num)
        if(user_num<=26):
            Password_list=[]
            for _ in range(0,user_num):
                Pass_elements=random.choice(List_of_password_components)
                Password_list.append(Pass_elements)
        new_password=str(Password_list)
        password_1=new_password.replace(','," ")
        password_2=password_1.replace(" ","")
        password_3=password_2.replace("'","")
        password_4=password_3.strip("[]")
        print("The generated user password is:     "+ password_4)
        return password_4
    except:
        print("**********************************INVALID INPUT*******************************************")

new_password=pass_gen_basic_v_2()
