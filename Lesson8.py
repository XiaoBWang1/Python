# Indexing = [start : end : step] , [::-1] reverses string

# Input for user, then index last 4 digits and print the 4 integers
creditcard = input("Please enter your full credit card number: ")
last4digits = creditcard[8:11:]
print(last4digits)