# Python writing file(.txt, .json, .csv)/ with open as = file mode

# Create a file type to create and insert the destination path
output_data = "Python is great."
path = "C:\\Users\\xbw24\\Desktop\\output.txt"

# Write a text file
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

