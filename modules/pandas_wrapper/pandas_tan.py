from typing import Any, Dict
import pandas as pd
import numpy as np


class PandasTan:
    """
    Applies the tangent function to a pandas DataFrame and converting non-numeric values to NaN.
    
    category: Math
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
                "dataframe": ("DATAFRAME", {})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame) -> tuple:
        """
        Converts non-numeric values to NaN and applies the tangent function to the DataFrame.

        The tangent function is the ratio of the sine to the cosine, representing the slope of a line
        from the origin to a point on the unit circle.

        Args:
            dataframe (DataFrame): The DataFrame.

        Returns:
            tuple: A tuple containing the processed DataFrame.
        """
        dataframe = dataframe.apply(pd.to_numeric, errors='coerce')
        dataframe = np.tan(dataframe)
        return (dataframe,)
