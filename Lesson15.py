# Positional, default, keyword, arbitrary. * unpacking operator.
# *args allow multiple non-keyword arguments. **kwargs allows for multiple keyword arguments
# membership operator (in/not in)
# list comprehension = [expression / in (value) / in (iterables) / if (condition)]
# match case = switch case/ case _ = wild card case, | = or
# print(help(module)), import module as variable,
# variable scope = accessible & visible, scope resolution = LEGB(Local-> Enclosed-> Global -> Built-In)
# __ double underscore(dunder)/ from module import */ if __name__ == '__main__': / main()

# Basic Banking Application

# Create a functions for showing the balance of the user's account through an f-string print statement
def show_balance(balance):
    print(f"The balance is ${balance:.2f}")

# Create a deposit function to showing allow the user to input money into their account
def deposit():
    amount = float(input("Enter the deposit amount: "))
    if amount < 0:
        return 0
    else:
        return amount

# Create a withdrawal function to allow the user to withdrawal money from their account
def withdraw(balance):
    amount = float(input("Enter the withdrawable amount: "))
    if amount > balance:
        print("Unable to process!")
        return 0
    elif amount < 0:
        print("Must be positive!")
        return 0
    else:
        return amount



# Main function first with variables of balance, Boolean statement of if the program is in use, and a while loop for user
# input of each function through the use of numerical entry
def main():
    balance = 0
    on = True
    while on:
        print("Banking App")
        print("1.Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        user_input = input("Enter your number(1-4)? ")
        if user_input == '1':
            show_balance(balance)
        elif user_input == '2':
            balance += deposit()
        elif user_input == '3':
            balance -= withdraw(balance)
        elif user_input == '4':
            on = False
        else:
            print("That is not a valid input. Try again!")
    print("Have a good day!")

# Call main function separately or as a module
if __name__ == '__main__':
    main()


