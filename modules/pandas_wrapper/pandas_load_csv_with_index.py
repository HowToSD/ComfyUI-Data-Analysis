from typing import Any, Dict
from io import StringIO
import pandas as pd


class PandasLoadCSVWithIndex:
    """
    Pandas Load CSV With Index:
    Loads CSV files into a pandas DataFrame.
    Input data is assume to have an index.

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
                "index_col": ("INT", {"default": 0, "min": 0, "max": 10000})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "load_csv"
    CATEGORY: str = "Data Analysis"

    def load_csv(self, file_path: str, index_col: int=0) -> tuple:
        """
        Loads a CSV file into a pandas DataFrame and converts it to a JSON string.
        Input data is assume to have an index.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            tuple: A tuple containing a JSON string representation of the DataFrame.
        """
        # Read CSV file into DataFrame
        df = pd.read_csv(file_path, index_col=index_col)
        return (df,)
