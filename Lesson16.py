# Slot Machine Gaming App
# window key + semicolon = emoji

import random

# A function for the output of the slot machine spin using the icons and return
# the result in a random order with 4 iterables in a list comprehension
def spin_slot():
    emojis = ['💰', '🐉', '🐍', '❌']
    return [random.choice(emojis) for _ in range(4)]

# A function to display the output of slot machine with a separator between the slot result
def slot_result(display):
    print("------------------")
    print(" | ".join(display))
    print("------------------")

# A function to determine if the user has won the spin through if all the icons are the same
def lottery(display, bet):
    if display[0] == display[1] == display[2] == display[3]:
        if display[0] == '💰':
            return bet * 10
        elif display[0] == '🐉':
            return bet * 4
        elif display[0] == '❌':
            return bet / 2
    return 0

# Main method to encapsulate all the code beginning with a welcome screen and credits to start
def main():
    print("----------------------")
    print("Welcome to the PySlot!")
    credit = 100
    print("Symbols: 💰 🐉 🐍 ❌ ")
    print("----------------------")

# If the credit is greater than 0 then user input a betting amount which will subtract from the user credit
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

        credit -= bet

# The second function that displays the result on the screen
        display = spin_slot()
        print("Wait a second....\n")
        slot_result(display)

        winnings = lottery(display, bet)

        if winnings > 0:
            print(f"You won {winnings}.")
        else:
            print("Sorry, try again!")

        credit += winnings

        another_game = input("Do you want to try again?(Y/N): ").upper()
        if another_game != 'Y':
            break

    print(f"Game over! Total amount of credit is ${credit}")

# Dunder main for individual/ separate module
if __name__ == '__main__':
    main()
