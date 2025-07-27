# Python writing file(.txt, .json, .csv)/ with open as = file mode

# Create a file type to create and insert the destination path
# output_data = "Python is great."
# path = "C:\\Users\\xbw24\\Desktop\\output.txt"

# plain text file
# Do a try except the opens to the abs path which appends the data with new line to the output file. Exception override
# due to duplicates else file creation is successful and confirmation print formatted string statement.
# ''' or ``'''' for paragraph comment
"""try:
    with open (path, "a") as file:
        file.write("\n" + output_data)
        print("The file is written.")
except FileExistsError:
        print(f"{path} already exists.")
else:
        print(f"{path} is created.")
finally:
        print(f"{path} is located at the specific absolute file path.")"""

import json
import writer

# JSON file writer/ json.dump/ json.load(read)
# create a variable to store the data into a json file inside a dictionary.
"""scientist = {
    "Alan Turing" : "Turing Test",
    "Tim Berners-Lee" : "WWW",
    "Ada Lovelace" : "Analytical Machine",
    "Linus Torvalds" : "Linux"
}
path = "C:\\Users\\xbw24\\Desktop\\output.json"
try:
    with open (path, "w") as file:
        json.dump(scientist, file, indent=3)
        print("The file is written.")
except FileExistsError:
        print(f"{path} already exists.")"""


# Comma-separated file writer
# csv.reader/
import csv

#scientists = [["Name" ,"Birthyear", "Invention"],["Alan Turing" , 1912, "Turing Test"],["Tim Berners-Lee" , 1955, "WWW"],["Ada Lovelace" , 1815, "Analytical Machine"],["Linus Torvalds" , 1969,  "Linux"]]
"""csv_data = [["Month", "Day", "Year"],
            ["March", 9, 1990],
            ["January", 23, 1993],
            ["May", 16, 1989]]

# Create a file path variable with csv extension and try exception that opens the file, then create a writer
# object and pass along the file argument. A for loop that lets writer iterate over the data and use writerow function
# to create a csv file with confirmation and duplication exception
path = "C:\\Users\\xbw24\\Desktop\\output.csv"
try:
    with open (path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in csv_data:
            writer.writerow(row)
        print("The csv file is written.")
except FileExistsError:
        print(f"{path} already exists.")"""





