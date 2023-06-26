import pandas as pd
import logging
import sys
from collections import Counter

log_format = "%(asctime)s %(levelname)s %(name)s: %(message)s"
logging.basicConfig(level = logging.INFO, format = log_format)
logger = logging.getLogger()

#Check if input file path and format are valid
def read_data(path):
    try:
        data = pd.read_excel(path)
        return data
    except FileNotFoundError:
        logger.exception("Invalid file path as argument, you entered: '{}'".format(path))
    except ValueError:
        logger.exception("Invalid format of file as argument -> .xlsx; you entered: '{}'".format(path))


def evaluate_data(data):
    expected_columns_count = 18
    #Check if number of columns is sufficient
    if len(data.columns) < expected_columns_count:
        logger.exception("Insufficient number of columns in the file.")
    else:
        #Iterate threw I-R columns, log unique values and its frequency of appearance
        for column in data.columns[8:18]:
            new_data = []
            for element in data[column]:
                try:
                    #Try if element in string is convertable to list,dict,etc.
                    to_type = eval(element)
                    if (type(to_type) == list and len(to_type)>1):
                            for x in to_type:
                                new_data.append(x)

                    elif (len(to_type)<=1):
                        #list []/ list [element]/ dict {}
                        new_data.append(to_type[0])

                    else: 
                        #dict
                        for key, value in to_type.items():
                            new_data.append({key: value})

                except:
                    #NaN elements
                    new_data.append(element)


            series = pd.Series(new_data)

            #Logging unique values with its occurency
            value_counts = series.value_counts(dropna=False)
            print(column)
            logger.info(str(value_counts) + '\n')

        if "ID user" and "Z/V" in data.columns:
            #Log number of "Vypnute" and "Zapnute" of every user
            count = data.groupby("ID user")["Z/V"].value_counts().unstack(fill_value=0)
            logger.info("Users and their total number of \"Zapnuté\" and \"Vypnuté\":\n")
            logger.info(count)
        else:
            logger.exception("Column not found: 'ID user' or 'Z/V'")

def main():
    # Check if argument (path) was inserted
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "work_with_python/data_python.xlsx"

    data = read_data(path)
    if data is not None:
        evaluate_data(data)

if __name__ == '__main__':
    main()
