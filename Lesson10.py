# Nested Loop | collection = list [], tuple(), set{} | print(help("x"))

# Create a 2-dimensional list that contains elements of the variable
Cars = [["Toyota", "Honda", "Nissan"],
        ["Ford", "GMC", "Tesla"],
        ["Volkswagen", "Stellantis", "BMW"]]

# Nested for loop to display the all the element in the collection of the instantiated variable
for collection in Cars:
    for car in collection:
        print(car, end= " ")
    print()