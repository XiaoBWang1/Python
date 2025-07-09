# Positional, default, keyword, arbitrary. * unpacking operator.
# *args allow multiple non-keyword arguments. **kwargs allows for multiple keyword arguments
# membership operator (in/not in)
# list comprehension = [expression / in (value) / in (iterables) / if (condition)]
# match case = switch case/ case _ = wild card case, | = or
# print(help(module)), import module as variable,
# variable scope = accessible & visible, scope resolution = LEGB(Local-> Enclosed-> Global -> Built-In
# __ double underscore(dunder)/ from module import */ if __name__ = __'main'__ main()

# Basic Banking Application

# Create 3 functions for each respective user action
def showBalance(balance):

    print(f"The balance is ${balance:.2f}")

def deposit():

    amount = float(input("Enter the deposit amount: "))

    if amount >= 0:
        return 0
    else:
        return amount

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


balance = 0
on = True
while on:

    print("Banking App")
    print("1.Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")


    userInput = input("Enter your number(1-4)? ")

    if userInput == '1':
        showBalance(balance)
    elif userInput == '2':
        balance += deposit()
    elif userInput == '3':
        balance = withdraw(balance)
    elif userInput == '4':
        on = False
    else:
        print("That is not a valid input. Try again!")

print("Have a good day!")


