import pandas as pd
import sys

#Check if argument (path) was inserted
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = "Work_with_python/data_python.xlsx"

try:
    data = pd.read_excel(path)

    #Check if number of columns is sufficient
    expected_columns = 18
    if len(data.columns) < expected_columns:
        print("Insufficient number of columns in the file:", path)

    else:
        #list unique values with number of its occurance in columns I-R
        for x in data.columns[8:18]:
            value_counts = data[x].value_counts(dropna=False)
            print(value_counts)
            print ("")

        #number of "Vypnuté" and "Zapnuté" [H] of user
        count = data.groupby("ID user")["Z/V"].value_counts().unstack(fill_value=0)
        print("Users and their total number of \"Vypnuté\" and \"Zapnuté\"")
        print(count)

except FileNotFoundError:
    print("File not found: ", path)

except pd.errors.ParserError:
    print("Invalid file format:", path)
