# Is vegetarian?

class Item:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price


is_vegetarian = input("Are you vegetarian? \"Yes\" or \"No\" ").lower() == "yes"

budget = float(input("Please enter your budget "))

not_vegetarian = not is_vegetarian

cart = []

if is_vegetarian:
    cart.append("Tofu")
    print("Added Tofu to your cart!")
else:
    cart.append("Chicken Breast")
    print("Added Chicken Breast to your cart!")

store_items = [
    Item("Banana", 5),
    Item("Carrots", 10),
    Item("Broccoli", 15),
]

if budget >= 5:
    cart.append(store_items[0].title)
    budget -= 5
if budget >= 10:
    cart.append(store_items[1].title)
    budget -= 10
if budget >= 15:
    cart.append(store_items[2].title)
    budget -= 15

print(f"Your cart has: {cart}")
print(f"Your wallet has: ${budget}")
