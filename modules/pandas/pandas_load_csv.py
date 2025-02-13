from typing import Any, Dict
import pandas as pd


class PandasLoadCSV:
    """
    PandasLoadCSV:
        A class for loading CSV files into a pandas DataFrame.
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `load_csv` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "file_path": ("STRING", {"multiline": False}),
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "load_csv"
    CATEGORY: str = "Data Analysis"

    def load_csv(self, file_path: str) -> tuple:
        """
        Loads a CSV file into a pandas DataFrame and converts it to a JSON string.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            tuple: A tuple containing a JSON string representation of the DataFrame.
        """
        # Read CSV file into DataFrame
        df = pd.read_csv(file_path)

        # Convert DataFrame to JSON
        result_json = df.to_json()

        return (result_json,)
