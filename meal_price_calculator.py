#What I added: I added a if statement to verify if the payment amount is grader than the total value.

#Prompt prices of meals and number of adults and children
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of a adult's meal? "))
children_quantity = int(input("How many children are there? "))
adults_quantity = int(input("How many adults are there? "))
print()
#determining the subtotal before adding taxes
subtotal = (children_quantity * child_meal_price) + (adults_quantity * adult_meal_price)
print(f"Subtotal: ${subtotal:.2f}")
print()
#Prompt to user the sale tax rate
tax_rate = float(input("What is the sales tax rate? "))
sales_tax = (subtotal * tax_rate) / 100
print(f"Sales Tax: ${sales_tax:.2f}")
total = subtotal + sales_tax
print(f"Total: ${total:.2f}")
print()
#Prompt user payment amount 
payment_amount = float(input("What is the payment amount? $"))
change = payment_amount - total
if change < 0:
    print("The payment must be grather then the total amount.")
else:
    print(f"Change: ${change:.2f}")