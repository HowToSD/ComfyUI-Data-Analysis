from typing import Any, Dict
import pandas as pd

class PandasSeriesToDataFrame:
    """
    Converts a Pandas Series to a DataFrame.

    category: Transformation
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
                "series": ("PDSERIES", {}),
                "label": ("STRING", {"default": ""}),
                "transpose": ("BOOLEAN", {"default": True})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, series: pd.Series, label: str, transpose: bool) -> tuple:
        """
        Converts a Pandas Series to a DataFrame.

        Args:
            series (Series): The Series.
            label (str): The label for the Series in the DataFrame.
            transpose (bool): Whether to transpose the DataFrame after conversion.
                              If True, Series will become a row. Otherwise it will become a column.

        Returns:
            tuple: A tuple containing the DataFrame.
        """
        df = series.to_frame(name=label) if label else series.to_frame()
        df = df.transpose() if transpose else df
        return (df,)
