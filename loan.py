decision = ""
# job = input("Do you have a job? (yes/no): ")
# job = job.lower()

# if job == "yes":
#     job_time = input("How long have you worked there? ")
#     job_payment = float(input("How much money do you make in there? $"))

# loan_collateral = input("Is There any good collateral for the loan?  (yes/no): ")

# credit = input("Do you have a good credit score or paying back loans? (yes/no): ")

# debt_amount = float(input("How much is the debt amount? $"))

# money_amount = float(input("How much money do you have saved? $"))

# down_payment = input("Will you have a donwned payment? (yes/no):")
# down_payment = down_payment.lower()

# if down_payment == "yes":
#     percentage_loan = float(input("What percentage of the loan does it amount to? "))

print("In a rating from 1 (really bad) to 10 (super good), answer the following:")
loan_size = int(input("How large is the loan? "))
credit_history = int(input("How good is you credit history? "))
income_height = int(input("How high is you income? "))
their_down_payment = int(input("How large is your down payment? "))

if loan_size >= 5:
    if credit_history >=7 and income_height >=7:
        decision = "yes"
    elif loan_size >= 7 or income_height >=7:
        if their_down_payment >= 5:
            decision = "yes"
        else:
            decision = "no"
    else:
        decision = "no"
elif loan_size < 5:
    if credit_history < 4:
        decision = "no"
    elif credit_history >= 4:
        if income_height >= 7 or their_down_payment >= 7:
            decision = "yes"
        elif income_height >= 4 and their_down_payment >=4: 
            decision = "yes"
        else:
            decision = "no"

print()
if decision == "yes":
    print(f"The decision for your loan is: {decision.capitalize()}! Congratulations!")
else:
    print(f"The decision for your loan is: {decision.capitalize()}. I'm sorry...")