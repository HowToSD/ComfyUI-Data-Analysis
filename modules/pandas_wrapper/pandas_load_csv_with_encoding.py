from typing import Any, Dict
from io import StringIO
import pandas as pd


class PandasLoadCSVWithEncoding:
    """
    PandasLoadCSVWithEncoding:
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
                "encoding": ("STRING", {"multiline": False})
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "load_csv"
    CATEGORY: str = "Data Analysis"

    def load_csv(self, file_path: str, encoding: str) -> tuple:
        """
        Loads a CSV file into a pandas DataFrame and converts it to a JSON string. Allows specifying the file encoding to support formats other than UTF-8.

        Refer to the below documents for the list of encodings:
        https://docs.python.org/3/library/codecs.html#standard-encodings

        Args:
            file_path (str): The path to the CSV file.
            encoding (str): Encoding of the file.

        Returns:
            tuple: A tuple containing a JSON string representation of the DataFrame.
        """
        # Read CSV file into DataFrame
        df = pd.read_csv(file_path, encoding=encoding)

        # Convert DataFrame to JSON
        result_json = df.to_json()

        return (result_json,)
