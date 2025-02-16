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
                "column_label": ("STRING", {"default": ""}),
                "column_label_type":(("string", "int"),)
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "cell"
    CATEGORY: str = "Data Analysis"

    def cell(self, dataframe_json: str,
             row_index: str,
             row_index_type: str,
             column_label: str,
             column_label_type: str) -> tuple:
        """
        Selects specific cell from a pandas DataFrame.

        Args:
            dataframe_json (str): A JSON string representation of the DataFrame.
            row_index (str): The row index (row label) for the cell.
            row_index_type (str): The data type of the row index.
            column_label (str): The column label for the cell.
            column_label_type (str): The data type of the column label.
             
        Returns:
            tuple: A tuple containing the value of the cell in string.
        """
        # Deserialize JSON string to DataFrame
        df = pd.read_json(StringIO(dataframe_json))
        row_index = int(row_index) if row_index_type == "int" else row_index
        column_label = int(column_label) if column_label_type == "int" else column_label

        value = df.loc[row_index, column_label]
        return (str(value),)
