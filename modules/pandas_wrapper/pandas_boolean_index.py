from typing import Any, Dict
import pandas as pd

class PandasBooleanIndex:
    """
    Selects rows from a pandas DataFrame based on the boolean index in the Series.

    category: Data subset selection
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
                "boolean_index_series": ("PDSERIES", {})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame, boolean_index_series: pd.Series) -> tuple:
        """
        Selects rows from a pandas DataFrame based on the boolean index in the Series.

        Args:
            dataframe (DataFrame): The DataFrame.
            boolean_index_series: (pd.Series): The Series containing boolean index.

        Returns:
            tuple: A tuple containing the filtered DataFrame.
        """
        if not isinstance(boolean_index_series, pd.Series):
            raise ValueError("boolean_index_series is not a Series.")

        df2 = dataframe[boolean_index_series]
        return (df2,)
