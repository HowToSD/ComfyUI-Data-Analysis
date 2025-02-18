from typing import Any, Dict
import pandas as pd

class PandasIndex:
    """
    PandasColumns:
        A class for retrieving the row labels (index) of a pandas DataFrame.
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `row_index` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe": ("DATAFRAME", {})
            }
        }

    RETURN_TYPES: tuple = ("PDINDEX",)
    FUNCTION: str = "row_index"
    CATEGORY: str = "Data Analysis"

    def row_index(self, dataframe: pd.DataFrame) -> tuple:
        """
        Returns the row labels (index) of a pandas DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.

        Returns:
            tuple: A tuple containing a pandas.Index for row labels.
        """
        row_index = dataframe.index
        return (row_index,)
