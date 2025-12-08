numbers_list = []
keep_asking = "yes"

while keep_asking == "yes":
    new_number = float(input("Enter number: "))
    if new_number == 0:
        keep_asking = "no"
    else:
        numbers_list.append(new_number)

number_sum = 0
print("The sum is: ", end="")
for index in range(len(numbers_list)):
    number = numbers_list[index]
    number_sum += number
print(f"{number_sum:.0f}")

number_average = number_sum / len(numbers_list)
print(f"The average is: {number_average}")

largest_number = max(numbers_list)
print(f"The largest number is: {largest_number:.0f}")

for index in range(len(numbers_list)):
    number = numbers_list[index]
    if number > 0 and number < number_sum:
        smallest_number = number
print(f"The smallest number is: {smallest_number:.0f}")