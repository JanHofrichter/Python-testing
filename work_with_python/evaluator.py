import pandas as pd
import logging
import sys

def logger (text):
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s" 
    logging.basicConfig(format = log_format, level = logging.INFO)
    
    logger = logging.getLogger()
    logger.info(text)

def read_data(path):
    try:
        data = pd.read_excel(path)
        return data
    except FileNotFoundError:
        print("File not found:", path)
    except pd.errors.ParserError:
        print("Invalid file format:", path)

def evaluate_data(data):
    expected_columns_count = 18
    if len(data.columns) < expected_columns_count:
        print("Insufficient number of columns in the file.")
    else:
        for column in data.columns[8:18]:
            values = data[column].value_counts(dropna=False)
            logger(f"{values}\n")

        count = data.groupby("ID user")["Z/V"].value_counts().unstack(fill_value=0)
        print("Users and their total number of \"Vypnuté\" and \"Zapnuté\":\n")

        logger(count)

def main():
    # Check if argument (path) was inserted
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "work_with_python/data_python.xlsx"

    data = read_data(path)
    evaluate_data(data)

if __name__ == '__main__':
    main()
