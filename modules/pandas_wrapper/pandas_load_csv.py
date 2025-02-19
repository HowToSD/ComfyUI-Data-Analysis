from typing import Any, Dict
from io import StringIO
import pandas as pd


class PandasLoadCSV:
    """
    Pandas Load CSV:
    Loads CSV files into a pandas DataFrame.

    category: IO
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

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "load_csv"
    CATEGORY: str = "Data Analysis"

    def load_csv(self, file_path: str) -> tuple:
        """
        Loads a CSV file into a pandas DataFrame.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            tuple: A tuple containing a DataFrame.
        """
        # Read CSV file into DataFrame
        df = pd.read_csv(file_path)
        return (df,)
