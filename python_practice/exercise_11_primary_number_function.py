# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors.). 
# You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.

def prime_number():
    User_input=float(input("Enter a number :        "))
    if (User_input%2==0):
        print("User has entered a composite number   "+ str(User_input))
    else:
        print("User has entered a prime number   "+ str(User_input))
    return User_input

number = prime_number()
