grade = float(input("Enter your course grade: "))
score = ""

if grade >= 70:
    if grade >= 90:
        score = "A"
    elif grade >= 87:
        score = "B+"
    elif grade >= 83:
        score = "B"
    elif grade >= 80:
        score = "B-"
    elif grade >= 77:
        score = "C+"
    elif grade >= 73:
        score = "C"
    else:
        score = "C-"
    print(f"Congratulations! You passed! Your Grade is: {score}!")
elif grade < 70:
    if grade >=67:
        score = "D+"
    elif grade >= 63:
        score = "D"
    elif grade >= 60:
        score = "D-"
    else:
        score = "F"
    print(f"Unfortunately you didn't pass the course. Your grade is {score}.")