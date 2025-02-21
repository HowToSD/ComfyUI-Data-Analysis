from typing import Any, Dict
from io import StringIO
import pandas as pd

class PandasSetIndex:
    """
    Create index (row label) from existing column or columns.

    You can specify a single column or a comma-separated list of column labels in `column_names`.  
    If `drop=True`, the specified columns are removed from column labels and become the index.  
    If `drop=False`, the columns remain in the DataFrame column labels while also being used as the index.  
    If `append=True`, the new index is added alongside the existing index.
    
    Below screenshots illustrate these options:

    ![Pandas Set Index](../images/set_index1.png)

    ![Pandas Set Index](../images/set_index2.png)

    This class internally calls `pandas.DataFrame.set_index()`.
    
    category: Data transformation
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
                "dataframe": ("DATAFRAME", {}),
                "column_names": ("STRING", {"default": ""}),
                "drop": ("BOOLEAN", {"default": True}),
                "append": ("BOOLEAN", {"default": False})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame, column_names: str, drop: bool, append: bool) -> tuple:
        """
        Create index (row label) from existing column or columns.

        Args:
            dataframe (DataFrame): The DataFrame.
            column_names (str): A single column label or a comma-separated string of column names to select.
            drop (bool): If `drop=True`, the specified columns are removed from column labels and become the index.  
                         If `drop=False`, the columns remain in the DataFrame column labels while also being used as the index.  
            append (bool): If `append=True`, the new index is added alongside the existing index.

        Returns:
            tuple: A tuple containing the DataFrame.
        """
        columns = [col.strip() for col in column_names.split(",")]
        for c in columns:
            if c not in dataframe.columns:
                raise ValueError(f"Invalid column name {c}")
        if len(columns) > 1:
            arg = columns
        else:
            arg = columns[0]

        df2 = dataframe.set_index(arg, drop=drop, append=append)
        return (df2,)
