from typing import Any, Dict
from io import StringIO
import pandas as pd


class PandasLoadExcel:
    """
    Loads Excel files into a pandas DataFrame.

    This node uses read_excel method.
    See [Pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html) for details.

    If sheet_name is not specified, first sheet will be read.

    category: IO
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
                "sheet_name": ("STRING", {"default": ""}),
                
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    @classmethod
    def IS_CHANGED(cls, **kw):
        return float("NaN")

    def f(self, file_path: str, sheet_name: str) -> tuple:
        """
        Loads an Excel file into a pandas DataFrame.

        Args:
            file_path (str): The path to the Excel file.

        Returns:
            tuple: A tuple containing a DataFrame.
        """
        if len(sheet_name) == 0:
            sheet_name = 0  # Read first sheet
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        return (df,)
