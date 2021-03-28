from datetime import datetime, timedelta 
Today = datetime.now()
name= input(" Please enter your name?")
age = float(input(" Please enter your age?"))
hundred_years_in_days= 365*(100-age)
years_to_turn_100 = timedelta(days=hundred_years_in_days)
Total_time_to_reach_100 = Today + years_to_turn_100
print("The name of the person is {} the current age is {} will turn 100 years of age in {} ".format(name,age,Total_time_to_reach_100))
message_copies=int(input("enter a number please  :    "))
message ="The name of the person is {} the current age is {} will turn 100 years of age in {} ".format(name,age,Total_time_to_reach_100)
print(message_copies * (message + "\n"))