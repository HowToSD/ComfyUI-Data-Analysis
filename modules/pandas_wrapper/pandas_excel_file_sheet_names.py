from typing import Any, Dict
import pandas as pd


class PandasExcelFileSheetNames:
    """
    Returns the string list of sheet names contained in the Excel file.

    This node uses ExcelFile method using the openpyxl package.
    The openpyxl package is specified as a dependency in requirements.txt, so you should not need to manually install it.
    See [Pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.html) for details.

    To display the list, connect output to PyListToString node to convert the list to a string, then connect the output to Pandas Show Text node to display the string.

    category: IO
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
                "file_path": ("STRING", {"multiline": False}),
            }
        }

    RETURN_TYPES: tuple = ("PYLIST",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    @classmethod
    def IS_CHANGED(cls, **kw):
        return float("NaN")

    def f(self, file_path: str) -> tuple:
        """
        Returns the string list of sheet names contained in the Excel file.

        Args:
            file_path (str): The path to the Excel file.

        Returns:
            tuple: A tuple containing a string list of sheet names.
        """
        pylist = pd.ExcelFile(file_path, engine="openpyxl").sheet_names
        return (pylist,)
