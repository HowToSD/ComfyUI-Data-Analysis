from typing import Any, Dict
from io import StringIO
import pandas as pd


class PandasLoadJSON:
    """
    Pandas Load JSON:
    Loads JSON files into a pandas DataFrame.

    category: IO
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `load_json` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "file_path": ("STRING", {"multiline": False}),
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "load_json"
    CATEGORY: str = "Data Analysis"

    # Mark this class to always execute.
    # Refer to
    # https://docs.comfy.org/custom-nodes/backend/server_overview
    @classmethod
    def IS_CHANGED(cls, **kw):
        return float("NaN")

    def load_json(self, file_path: str) -> tuple:
        """
        Loads a JSON file into a pandas DataFrame.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            tuple: A tuple containing a DataFrame.
        """
        # Read JSON file into DataFrame
        df = pd.read_json(file_path)
        return (df,)
