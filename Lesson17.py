# Text Encryption Program

import string
import random

# Instantiate a variable consisting of letters, digits, and punctuations from the string library. Then put it in a list
code = string.ascii_letters + string.digits + string.punctuation
code = list(code)

# Create a variable for the key by copying from the first variable and shuffling it randomly
cypher = code.copy()
random.shuffle(cypher)

# Display the randomized code and its encryption
#print(f"{code}")
#print(f"{cypher}")


# Encryption section with a user input, assign empty string for the encrypted message. For every char in list, find the
# index number of the pre-crypted string and added into the cypher
message = input("Enter the texts to encrypt?: ")
cipher = ""

for text in cypher:
    index = code.index(text)
    cipher += cypher[index]

print(f"{message}")
print(f"{cipher}")

# Decryption section which is the reverse of the encryption method
encrypted_message = input("Enter the texts to decrypt?: ")
decode = ""

for letter in encrypted_message:
    index = cypher.index(letter)
    decode += code[index]

print(f"{encrypted_message}")
print(f"{decode}")