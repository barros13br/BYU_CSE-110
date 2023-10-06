#here is goes the input.
children = float(input("What is the price of a child's meal? "))
adult = float(input("What is the price of a adult's meal? "))
q_children = int(input("How many children are there? "))
q_adults = int(input("How many adults are there? "))

#Sub total math
sub_total = (children * q_children) + (adult * q_adults)
print()
print(f"Subtotal: ${sub_total:.2f}")

#sale tax input and math.
print()
tax = float(input("What is the sales tax rate? "))
sale_tax = sub_total * tax / 100 
total = sale_tax + sub_total
print(f"Sales Tax: ${sale_tax:.2f}")
print(f"Total: ${total:.2f}")

#calculating paymant
print()
pay = float(input("What is the payment amount? "))
change = pay - total 
print(f"Change: ${change:.2f}")