# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
# Take this opportunity to think about how you can use functions. 
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. 
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fibonacchi_seq():
    User_input=int(input("Enter the number of numbers you want in fibonacci sequence : ?"))
    Fibonnaci_List=[]
    n1=0
    n2=1
    for _ in range(User_input):
        new_num=n1+n2
        n1=n2
        n2=new_num
        Fibonnaci_List.append(float(n1))

    return print(Fibonnaci_List)

fib = fibonacchi_seq()


# As Pylint states, you aren't using the i variable.
# If you really plan on not using it, change it to _ and Pylint should ignore it.