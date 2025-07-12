# Slot Machine Gaming App
# window key + semicolon = emoji

# A function for the output of the slot machine spin
def spin_result():
    pass
# A function to display the output of slot machine
def slot_result():
    pass
# A function to determine if the user has won the spin
def lottery():
    pass

# Main method to encapsulate all the code
def main():
    print("Welcome to the PySlot! ")
    credit = 100
    print("Symbols: 💰 🐉 🐍 ❌")

    while credit > 0:
        print(f"Present credit: ${credit}")
        bet = input("Enter the betting amount: $")
        if not bet.isdigit():
            print("Please enter a valid number!")
            continue
        bet = int(bet)
        if bet > credit:
            print("Not enough balance!")
            continue
        if bet <= 0 :
            print("Please enter a valid amount!")


        bet -= credit


# Dunder main for individual/ separate module
if __name__ == '__main__':
    main()
