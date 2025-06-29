# Temperature Converter

# Two input statement for user input
unit = input("Please enter the temperature in Celsius or Fahrenheit(C/F): ")
temperature = float(input("Enter the temperature in degrees? "))

# If/elif/else statement to differentiate the different units(C/F) or display invalid input
if unit == "C":
    temperature = round((9 * temperature) / 5 + 32, 2)
    print(f"The temperature in Celsius is {temperature}°F.")
elif unit == "F":
    temperature = round((temperature * 32 / 9), 2)
    print(f"The temperature in Fahrenheit is {temperature}°C.")
else:
    print(f"{unit} is not available. Please enter C/F.")