from typing import Any, Dict
import pandas as pd


class PandasIndexToString:
    """
    Converts a pandas Index to a string representation.

    category: Display data
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
                "index": ("PDINDEX", {}),
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, ind: pd.Index) -> tuple:
        """
        Converts a Pandas Index to a string representation.

        Args:
            ind (pd.Index): The index.

        Returns:
            tuple: A tuple containing the string representation of the Index.
        """
        return (str(ind),)
