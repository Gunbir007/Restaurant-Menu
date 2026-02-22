menu={"Pizza": 12.00,
      "Burger": 6.00,
      "Chips": 2.00,
      "Fries": 2.50,
      "Soda": 3.00}

cart = []
total = 0

print("========MENU========")
for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("====================\n")

while True:
    food = input("Select an item(Enter to order): ").capitalize()
    print()
    if not food:
        break
    elif food in menu:
        cart.append(food)
    else:
        print("Choose only from the MENU")

if not cart:
    print("You have not ordered anything!")
else:
    print("\n=======Your Cart=======")
    for item in cart:
        print(f"{item:10}: ${menu[item]:.2f}")
        total+=menu[item]
    print("=======================")
    print(f"Your total is ${total:.2f}")
    print("=======================")