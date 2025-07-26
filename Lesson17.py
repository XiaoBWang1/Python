# Text Encryption Program

import string
import random


# Instantiate a variable consisting of letters, digits, and punctuations from the string library, then put it in a list
code = string.ascii_letters + string.digits + string.punctuation
code = list(code)

# Create a variable for the key by copying from the first variable and shuffling it randomly
key = code.copy()
random.shuffle(key)

# Display the randomized code and its encryption
#print(f"{code}")
#print(f"{key}")

# Encryption section with a user input, assign empty string for the encrypted message. For every char in list, find the
# index number of the pre-crypted string and added into the key
message = input("Enter the texts to encrypt?: ")
cipher = ""

for text in message:
    index = code.index(text)
    cipher += key[index]

print(f"{message}")
print(f"{cipher}")

# Decryption section which is the reverse of the encryption method. Using a for loop to find the indices of the user
# input in the cypher then append it to the decryption
encrypted_message = input("Enter the texts to decrypt?: ")
decoded_message = ""

for char in encrypted_message:
    index = key.index(char)
    decoded_message += code[index]

print(f"{encrypted_message}")
print(f"{decoded_message}")