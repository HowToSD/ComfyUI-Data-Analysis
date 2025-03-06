from typing import Any, Dict
import pandas as pd
import datetime


class PandasAtSetDatetime:
    """
    Sets a Python datetime.datetime data in a cell in a pandas DataFrame.

    This modifies the input DataFrame in place.

    category: Transformation
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
                "dataframe": ("DATAFRAME", {}),
                "row_index": ("STRING", {"default": ""}),
                "row_index_type":(("string", "int"),),
                "column_label": ("STRING", {"default": ""}),
                "column_label_type":(("string", "int"),),
                "data": ("PYDATETIME", {})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame,
             row_index: str,
             row_index_type: str,
             column_label: str,
             column_label_type: str,
             data: datetime.datetime) -> tuple:
        """
        Selects specific cell from a pandas DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.
            row_index (str): The row index (row label) for the cell.
            row_index_type (str): The data type of the row index.
            column_label (str): The column label for the cell.
            column_label_type (str): The data type of the column label.
            data: datetime.datetime (datetime.datetime): The value to set in the cell.
             
        Returns:
            tuple: A tuple containing the value of the cell in string.
        """
        row_index = int(row_index) if row_index_type == "int" else row_index
        column_label = int(column_label) if column_label_type == "int" else column_label

        dataframe.at[row_index, column_label] = data
        return (dataframe,)
