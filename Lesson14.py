# Dice Roll Game
import random

# print("\u25CF, \u2500, \u250c, \u2510, \u2518, \u2514")/ ASCII unit code
# ●, ─, ┌, ┐, ┘, └


# Create a dictionary with tuple consists of strings in tuples
diceRoll = {

1:("┌───────┐",
   "|       |",
   "|   ●   |",
   "|       |",
   "└───────┘" ),

2:("┌───────┐",
   "| ●     |",
   "|       |",
   "|     ● |",
   "└───────┘" ),

3:("┌───────┐",
   "| ●     |",
   "|   ●   |",
   "|     ● |",
   "└───────┘" ),

4:("┌───────┐",
   "| ●   ● |",
   "|       |",
   "| ●   ● |",
   "└───────┘" ),

5:("┌───────┐",
   "| ●   ● |",
   "|   ●   |",
   "| ●   ● |",
   "└───────┘" ),

6:("┌───────┐",
   "| ●   ● |",
   "| ●   ● |",
   "| ●   ● |",
   "└───────┘" ),
}

# Create 3 variables for input, list of dice, and a total amount of user input
dice = []
total = 0
diceNumber = int(input("How many dice rolls?: "))

# A for loop the number of dice in range of the 1 through 6
for die in range(diceNumber):
    dice.append(random.randint(1,6))

# Nested for loop in range of the 5 numbers of line, then another for loop
# to get the die number in the list and then print the dictionary
# and use the get function for the die number with the line countenance
# with an end line empty string to format and lastly print all horizontally
for line in range(5):
   for die in dice:
       print(diceRoll.get(die)[line], end = " ")
   print()

# Nested for loop for die from the user input, then another for loop to get the
# value of the key 1-6 and print the ASCII art vertically
#for die in range(diceNumber):
#   for line in diceRoll.get(dice[die]):
#        print(line)

# Create a for loop for a total of amount of die of the user input
for die in dice:
    total += die
print(f"The total is {total}.", end = "")