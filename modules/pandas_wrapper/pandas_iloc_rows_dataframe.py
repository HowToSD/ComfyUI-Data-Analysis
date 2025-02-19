from typing import Any, Dict
from io import StringIO
import json
import pandas as pd
from .utils import series_to_jsons

class PandasIlocRowsDataFrame:
    """
    Selects rows from a pandas DataFrame and returning it as a DataFrame.
    Rows are specified by the list of integer positions.

    category: Data subset selection
    """

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `select_rows` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe": ("DATAFRAME", {}),
                "row_int_pos_list_json": ("STRING", {"multiline": False})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "select_rows"
    CATEGORY: str = "Data Analysis"

    def select_rows(self, dataframe: pd.DataFrame,
             row_int_pos_list_json: str) -> tuple:
        """
        Select rows from a pandas DataFrame and returning it as a DataFrame.
        Rows are specified by the list of integer positions and returned as
        the JSON serialized DataFrame object.

        Args:
            dataframe (DataFrame): The DataFrame.
            row_int_pos_list_json (str): A list containing row integer positions.

        Returns:
            tuple: A tuple containing the value of the row in string. The string is
                   a JSON string containing the serialized Pandas Series object.
        """
        row_int_pos_list = json.loads(row_int_pos_list_json)
        df2 = dataframe.iloc[row_int_pos_list]
        return (df2,)
