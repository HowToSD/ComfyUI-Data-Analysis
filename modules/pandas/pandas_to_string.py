from typing import Any, Dict
import pandas as pd

class PandasToString:
    """
    PandasToString:
        A class for converting a pandas DataFrame to a string representation.
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `to_string` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe_json": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "to_string"
    CATEGORY: str = "Data Analysis"

    def to_string(self, dataframe_json: str) -> tuple:
        """
        Converts a pandas DataFrame to a string representation.

        Args:
            dataframe_json (str): A JSON string representation of the DataFrame.

        Returns:
            tuple: A tuple containing the string representation of the DataFrame.
        """
        # Deserialize JSON string to DataFrame
        df = pd.read_json(dataframe_json)
        return (str(df),)
