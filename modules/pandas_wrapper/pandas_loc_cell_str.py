from typing import Any, Dict
from io import StringIO
import pandas as pd

class PandasLocCellStr:
    """
    PandasLocCellStr:
        A class for selecting a cell from a pandas DataFrame and output as a string.
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `cell` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe_json": ("STRING", {"multiline": True}),
                "row_index": ("STRING", {"default": ""}),
                "row_index_type":(("string", "int"),),
                "column_index": ("STRING", {"default": ""}),
                "column_index_type":(("string", "int"),)
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "cell"
    CATEGORY: str = "Data Analysis"

    def cell(self, dataframe_json: str,
             row_index: str,
             row_index_type: str,
             column_index: str,
             column_index_type: str) -> tuple:
        """
        Selects specific cell from a pandas DataFrame.

        Args:
            dataframe_json (str): A JSON string representation of the DataFrame.
            row_index (str): The row index (row label) for the cell.
            row_index_type (str): The data type of the row index.
            column_index (str): The column index (row label) for the cell.
            column_index_type (str): The data type of the column index.
             
        Returns:
            tuple: A tuple containing the value of the cell in string.
        """
        # Deserialize JSON string to DataFrame
        df = pd.read_json(StringIO(dataframe_json))
        row_index = int(row_index) if row_index_type == "int" else row_index
        column_index = int(column_index) if column_index_type == "int" else column_index

        value = df.loc[row_index, column_index]
        return (str(value),)
