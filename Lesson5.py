# Logical operator and,or,not.

# Assign both integer to temperature and Boolean to their respective input
temperature = 77
sunny = True

# If/elif/else statement with logical operator(and/or/not) to determine output
if temperature >= 70 and sunny:
    print("It is hot and sunny outside")
elif temperature <= 50 or sunny:
    print("It is cold and sunny today.")
elif temperature <= 0 and not sunny:
    print("It is freezing and cloudy.")
elif temperature >= 100 and sunny:
    print("It is too hot and sunny outside.")
else:
    print("Please retry again with the proper input.")
