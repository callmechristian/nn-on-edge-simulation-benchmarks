import pandas as pd
import sys

def append_to_df(data, filename):
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

def main():
    """Appends rows to an existing Pandas DataFrame saved in the given file.

    Usage:
    python3 append-to-table.py <filename>.csv <row1_value> <row2_value> ...
    """
    args = sys.argv

    if len(args) < 3:
        print("Usage: python3 utils/append-to-table.py <filename>.csv <row1_value> <row2_value> ...")
        return

    filename = args[1]
    data = [args[2:]]

    append_to_df(data, "dataframes/" + filename)

if __name__ == "__main__":
    main()