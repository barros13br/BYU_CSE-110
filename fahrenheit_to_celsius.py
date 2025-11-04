#prompt user fahrenheit
print("-----------------------------------------------------------------")
fahrenheit = float(input("What is the temperature in Fahrenheit? "))
#doing the convertion (math)
convertion_to_celsius = (fahrenheit - 32) * (5 / 9)
#printing the result
print()
print(f"The temperature in Celsius is {convertion_to_celsius:.1f} degrees.")
print("-----------------------------------------------------------------")