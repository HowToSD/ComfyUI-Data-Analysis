from typing import Any, Dict
from io import StringIO
import pandas as pd


class PandasCreate:
    """
    Creates a pandas DataFrame using values entered in the text field.

    category: IO
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
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "create"
    CATEGORY: str = "Data Analysis"

    def create(self, data: str) -> tuple:
        """
        Create a pandas DataFrame using values entered in the text field and converts it to a DataFrame.

        Args:
            data (str): String value in the text field.

        Returns:
            tuple: A tuple containing a the DataFrame.
        """
        # Read CSV file into DataFrame
        df = pd.read_csv(StringIO(data))
        return (df,)
