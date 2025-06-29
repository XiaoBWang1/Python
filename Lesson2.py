# Python Calculator

# Input statement for the operators and 2 numbers for output
operator = input("Enter an operator(+, -, *, /): ")
num1 =  float(input("Enter the first number: "))
num2 =  float(input("Enter the second number: "))

# If, else if, and else statement to differentiate the 4 different operators
if operator == "+":
    result = num1 + num2
    print(round(result, 2))
elif operator == "-":
    result = num1 - num2
    print(round(result, 2))
elif operator == "*":
    result = num1 * num2
    print(round(result, 2))
elif operator == "/":
    result = num1 / num2
    print(round(result, 2))
else:
     print(f"{operator} is not valid, please enter again.")