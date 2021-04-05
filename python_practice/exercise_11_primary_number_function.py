def prime_number():
    User_input=float(input("Enter a number :        "))
    if (User_input%2==0):
        print("User has entered a composite number   "+ str(User_input))
    else:
        print("User has entered a prime number   "+ str(User_input))
    return User_input

number = prime_number()
