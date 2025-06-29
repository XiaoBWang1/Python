# Weight Converter

# Two input statement for weight and unit
weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

# If/elif/else statement to determine which unit(K/L) and a invalid warning statement
if unit == "K":
    weight = weight * 2.205
    unit = "Kgs"
elif unit == "Lb":
    weight = weight / 2.205
    unit = "Lbs"
else:
    print(f"Your {unit} is not valid. Please enter a valid unit(K or L).")

# Print the converted input into output
print(f"Your weight conversion is {round(weight, 2)} {unit}")