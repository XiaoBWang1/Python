# Text Encryption Program

import string
import random

# Instantiate a variable consisting of letters, digits, and punctuations from the string library
code = " " + string.ascii_letters + string.digits + string.punctuation
code = list(code)

# Create a variable of the key by copying from the first variable and shuffling it
cypher = code.copy()
random.shuffle(cypher)

# Display the randomized code and its encryption
#print(f"{code}")
#print(f"{cypher}")


# Encryption
message = input("Enter the texts to encrypt?: ")
cipher = ""

for text in cipher:
    index = code.index(text)
    cipher += cypher[index]

print(f"{message}")
print(f"{cipher}")