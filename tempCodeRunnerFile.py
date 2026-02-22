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
print("====================")

while True:
    food = input("Select an item(q to Quit): ").capitalize()
    if food == "Q":
        break
    else:
        cart.append(food)

for item in cart:
    print(f"{item}: ${menu[item]}")
    total+=menu[item]

print(f"Your total is {total}")