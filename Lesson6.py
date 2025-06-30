# Password security test

# User input
username = input("Enter the username: ")

# If/elif/else statement to facilitate the various conditions for allowable password criteria
if len(username) < 10:
    print("Need more character. Please try agin!")
elif len(username) > 100:
    print("Too many character. Please shorten it!")
elif not username.find(" ") == -1:
    print("Username cannot have spaces")
elif username.isalpha():
    print("Only contain letters, must also incorporate numbers.")
elif not username.isalpha():
    print("Only contain numbers, must also incorporate letters.")
else:
    print("Welcome to your account.")