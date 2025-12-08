#I added a countin items cart at the top ooof each "round"

option_1 = "1. Add item"
option_2 = "2. Vew Cart"
option_3 = "3. Remove item"
option_4 = "4. Compute total"
option_5 = "5. Quit"
action = 0

cart_list = [] 
price_list = []

print("Welcome to the Shopping Cart Program!")
print()
print("Please select one of the following:")


while option_5 != "Quit":
    print()
    print(f"--You have {len(cart_list)} products in your cart.--")
    print("Please, select one of the following:")
    print(option_1)
    print(option_2)
    print(option_3)
    print(option_4)
    print(option_5)
    action = int(input("Please, enter an action: "))
    if action == 5:
        option_5 = "Quit"
        print("Thank you. Goodbye.")
    elif action == 1:
        new_item = input("What item would you like to add? ")
        price_new_item = float(input(f"What is the price of '{new_item}'? "))
        cart_list.append(new_item)
        price_list.append(price_new_item)
        print(f"'{new_item}' has been added to the cart!")
    elif action == 2:
        print("The contents of the shopping cart are:")
        for index in range(len(cart_list)):
            item = cart_list[index]
            print(f"{index + 1}. {item} - ${price_list[index]:.2f}")
    elif action == 3:
        print("The contents of the shopping cart are:")
        for index in range(len(cart_list)):
            item = cart_list[index]
            print(f"{index + 1}. {item} - ${price_list[index]}")
        change = int(input("Which item would you like to remove? "))
        cart_list.pop(change - 1)
        price_list.pop(change - 1)
        print("Item removed.")
    elif action == 4:
        total = 0
        for index in range(len(price_list)):
            price_item = price_list[index]
            total += price_item
        print(f"The total price of the item in the shopping cart is ${total:.2f}")
