#introductory message
print("Please anter the following information:")
print()
#input area
first_name = input("First name: ")
last_name = input("last name: ")
email = input("E-mail address: ")
phone = input("Phone number: ")
job = input("Job title: ")
indentification_number = input("ID number: ")

#ending declaration
print()
print("The ID Card is: ")
print("-------------------------------------------------------")
print(f"{last_name.upper()}, {first_name.capitalize()}")
print(job.capitalize())
print(f"ID: {indentification_number}")
print()
print(email.lower())
print(phone)
print("-------------------------------------------------------")