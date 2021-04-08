# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order. 
# For example, say I type the string:

def Reverse_word_order():
    User_input_string=input(" enter a sentence please    :    ")
    result=User_input_string.split(" ")
    return print(result[::-1])



rever_str=Reverse_word_order()