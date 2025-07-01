# Shopping Cart Application

# User input with type casting, then the equation for the total
item = input("What item do you want to buy?: ")
price = float(input("How much is it? "))
quantity = int(input("How much of it do you want to purchase?: "))
total = price * quantity

# Print formatted statement that displays user inputs and the answer to the equation
print(f"You have bought {quantity} * {item}/s")
print(f"Your total amount due is ${total}")