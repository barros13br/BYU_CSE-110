large = int(input("How large is the loan? (1 to 10): "))
credit = int(input("How good is your credit history? (1 to 10): "))
income = int(input("How high is your income? (1 to 10): "))
down_payment = int(input("How large is your down payment? (1 to 10): "))
should_loan = False

if large >= 5:
    if credit >= 7 and income >= 7:
        should_loan = True
    elif credit >= 7 or income >=7 and down_payment >= 5:
        should_loan = True
    else:
        should_loan = False

if large < 5:
    if credit < 4:
        should_loan = False
    elif credit >= 4:
        if income >= 7 or down_payment >= 7:
            should_loan = True
        elif income >= 4 and down_payment >= 4:
            should_loan = True
        else:
            should_loan = False

print()
if should_loan == True:
    print("Decision: Yes.")
else:
    print("Decision: No.")