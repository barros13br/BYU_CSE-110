#Prompt user age
print()
user_age = int(input("How old are you? "))
#Show user age next birthday
print(f"On your next birthday, you will be {user_age + 1}.")
print()
print("---------------------------------------------------------")
#prompt user number of eggs
eggs_quantity = int(input("How many egg cartoms do you have? "))
#Show quantity of eggs
print(f"You have {eggs_quantity * 12} eggs.")
print()
print("---------------------------------------------------------")
#Prompt user number of cookies
cookies_quantity = int(input("How many cookies do you have? "))
#Prompt user number of people
people = int(input("how many people are there? "))
#Dividing cookies per people
cookies_per_person = cookies_quantity/people
print(f"Each person may have {cookies_per_person:.1f} cookies.")
print()