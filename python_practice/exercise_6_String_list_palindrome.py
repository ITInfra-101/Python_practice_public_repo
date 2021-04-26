#Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)
User_String = input("Enter a sentence or name     :")
length_of_string = len(User_String)
print(length_of_string)
# print(User_String[::-1]) This means start at the end of the string by 1 character
if (User_String[0:length_of_string]) == (User_String[::-1]):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
    