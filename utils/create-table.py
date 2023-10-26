import pandas as pd
import sys

def create_empty_df(column_names, filename):
    """Creates an empty Pandas DataFrame with the given column names and saves it to the given file.

    Args:
    column_names: A list of strings containing the column names for the DataFrame.
    filename: The name of the file to save the DataFrame to.

    ==============
    Example usage:

    column_names = ["name", "age", "occupation"]
    filename = "my_data.csv"

    create_empty_df(column_names, filename)
    """

    df = pd.DataFrame(columns=column_names)
    df.to_csv(filename, index=False)

def main():
    """Creates an empty Pandas DataFrame with the given column names and saves it to the given file.

    Usage:
    python3 utils/create-table.py <filename>.csv <column_names> 
    """
    column_names = sys.argv[2:]
    filename = sys.argv[1]

    create_empty_df(column_names, "dataframes/"+filename)

if __name__ == "__main__":
    main()