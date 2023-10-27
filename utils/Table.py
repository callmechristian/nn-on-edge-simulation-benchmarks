import pandas as pd
import sys

class Table:
    def append_to_df(filename, data):
        """Appends rows to an existing Pandas DataFrame saved in the given file.

        Args:
        data: A list of lists where each inner list represents a row to be appended to the DataFrame.
        filename: The name of the file containing the DataFrame to which rows will be appended.
        """
        try:
            # Read the existing DataFrame from the file
            existing_df = pd.read_csv(filename)
        except FileNotFoundError:
            print(f"Error: The file {filename} does not exist. Use 'create-table.py' to create the initial DataFrame.")
            return

        # Create a new DataFrame from the data and append it to the existing DataFrame
        new_data_df = pd.DataFrame(data, columns=existing_df.columns)
        updated_df = pd.concat([existing_df, new_data_df], ignore_index=True)

        # Save the updated DataFrame back to the file
        updated_df.to_csv(filename, index=False)
        print(f"{len(data)} row(s) appended to {filename}.")

    def create_empty_df(filename, column_names):
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
    """Creates an empty dataframe or appends rows to an existing Pandas DataFrame saved in the given file.

    Usage:
    python3 utils/Table.py append <filename>.csv <row1_value> <row2_value> ...
    python3 utils/Table.py create <filename>.csv <column_names> 
    """
    args = sys.argv

    if len(args) < 3:
        print("Usage: python3 utils/Table.py <mode> <filename>.csv <values> ... \n where <mode> is create|append")
        return

    mode = args[0]
    if(mode == "create"):
        column_names = sys.argv[2:]
        filename = sys.argv[1]

        Table.create_empty_df(column_names, "dataframes/"+filename)

    if(mode == "append"):
        filename = args[1]
        data = [args[2:]]

        Table.append_to_df(data, "dataframes/" + filename)

if __name__ == "__main__":
    main()