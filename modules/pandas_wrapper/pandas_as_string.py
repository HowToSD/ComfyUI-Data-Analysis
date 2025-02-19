from typing import Any, Dict
import pandas as pd


class PandasAsString:
    """
    Converts all cells in a pandas DataFrame to string type.
    
    category: Data type conversion
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe": ("DATAFRAME", {})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "convert_to_string"
    CATEGORY: str = "Data Analysis"

    def convert_to_string(self, dataframe: pd.DataFrame) -> tuple:
        """
        Converts all cells in the DataFrame to string type.

        Args:
            dataframe (DataFrame): The DataFrame.

        Returns:
            tuple: A tuple containing the DataFrame with all values as strings.
        """
        # Convert all values to string
        df = dataframe.astype(str)
        return (df,)
