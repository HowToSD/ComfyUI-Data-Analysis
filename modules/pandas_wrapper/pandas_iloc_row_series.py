from typing import Any, Dict
from io import StringIO
import pandas as pd
from .utils import series_to_jsons

class PandasIlocRowSeries:
    """
    PandasLocRowSeries:
        A class for selecting a row from a pandas DataFrame and returning it as a Series.
        The row is specified by its integer position, similar to an index in other software.
        Note: In Pandas, "index" refers to a unique label assigned to each row or column. See https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html
    """

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `select_row` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe_json": ("STRING", {"multiline": True}),
                "row_integer_position": ("INT", {"default": 0, "min": 0, "max": 2**31})
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "select_row"
    CATEGORY: str = "Data Analysis"

    def select_row(self, dataframe_json: str,
             row_integer_position: int) -> tuple:
        """
        Selects a specific row using a row label (row index) from a pandas DataFrame,
        and returns the JSON serialized Series object.

        Args:
            dataframe_json (str): A JSON string representation of the DataFrame.
            row_integer_position (int): The row integer position.

        Returns:
            tuple: A tuple containing the value of the row in string. The string is
                   a JSON string containing the serialized Pandas Series object.
        """
        # Deserialize JSON string to DataFrame
        df = pd.read_json(StringIO(dataframe_json))
        value = df.iloc[row_integer_position]
        return (series_to_jsons(value),)
