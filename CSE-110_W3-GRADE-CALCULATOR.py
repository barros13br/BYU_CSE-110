
grade = int(input("Put your grade here: "))

print()

if grade >= 90:
    print("You scored: A")
elif grade >= 80:
    print("You scored: B")
elif grade >= 70:
    print("You scored: C")
elif grade >= 60:
    print("You scored: D")
elif grade < 60:
    print("You scored: F")

print()
if grade >= 70:
    print("Congratulations you passed the class.")
else:
    print("Sorry you didn't pass the class, keeping working.")

print()
grade2 = int(input("Reenter your grade percentage: "))

if grade2 >= 90:
    letter = "A"
elif grade2 >= 80:
    letter = "B"
elif grade2 >= 70:
    letter = "C"
elif grade2 >= 60:
    letter = "D"
elif grade2 < 60:
    letter = "F"

sign = ""
 
if grade2 >= 97:
    sign = "+"
elif grade2 <= 93:
    sign = "-"
elif grade2 >= 87:
    sign = "+"
elif grade2 <= 83:
    sign = "-"
elif grade2 >= 77:
    sign = "+"
elif grade2 <= 73:
    sign = "-"
elif grade2 >= 60:
    sign = "+"
elif grade2 <= 63:
    sign = "-"

if letter == "F":
    sign = ""

print()
print(f"You scored: {letter}{sign}.")
