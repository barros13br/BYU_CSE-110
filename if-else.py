number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the sencond number: "))

# verifing if the first number is grather than the second one
if number_1 > number_2:
    print ("The first number is greater")
else:
    print ("The first number is not greater")

# verifing if numbers are equal
if number_1 == number_2:
    print ("The numbers are equal")
else:
    print ("The numbers are not equal")

# verifing if se second number is greater than the first
if number_1 < number_2:
    print ("The second number is greater")
else:
    print ("The second number is not greater")
print()

animal = input("What is your favorite animal? ")
animal = animal.lower()

if animal == "bear":
    print ("That's my favorite animal too!")
else:
    print ("That is a good one, but it is not my favorite.")