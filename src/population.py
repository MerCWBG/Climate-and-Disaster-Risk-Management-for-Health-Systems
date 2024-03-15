import pandas as pd


class Population:
    def __init__(self):
        pass

    def read_csv(self, file_path):
        """
        Read a CSV file and return a DataFrame.

        Args:
            file_path (str): Path to the CSV file.

        Returns:
            DataFrame: DataFrame containing the data from the CSV file.
        """
        try:
            df = pd.read_csv(file_path)
            return df
        except FileNotFoundError:
            print(f"The file {file_path} was not found.")
            return None
