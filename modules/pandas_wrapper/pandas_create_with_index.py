from typing import Any, Dict
from io import StringIO
import pandas as pd


class PandasCreateWithIndex:
    """
    PandasCreateWithIndex:
        A class for creating a pandas DataFrame using values entered in the text field.
        Input data is assume to have an index.
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `create` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "data": ("STRING", {"multiline": True}),
                "index_col": ("INT", {"default": 0, "min": 0, "max": 10000})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "create"
    CATEGORY: str = "Data Analysis"

    def create(self, data: str, index_col: int=0) -> tuple:
        """
        Create a pandas DataFrame using values entered in the text field and converts it to a JSON string.
        Input data is assume to have an index.

        Args:
            data (str): String value in the text field.
            index_col (int): Position of the index column.

        Returns:
            tuple: A tuple containing a JSON string representation of the DataFrame.
        """
        # Read CSV file into DataFrame
        df = pd.read_csv(StringIO(data), index_col=index_col)
        return (df,)
