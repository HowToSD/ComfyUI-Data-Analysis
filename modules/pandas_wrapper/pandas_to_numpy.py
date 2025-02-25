from typing import Any, Dict
import pandas as pd

class PandasToNumpy:
    """
    Converts a pandas DataFrame to Numpy ndarray.

    category: Data type conversion
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
            }
        }

    RETURN_TYPES: tuple = ("NDARRAY",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame) -> tuple:
        """
        Converts a pandas DataFrame to a NumPy ndarray.

        Args:
            dataframe (DataFrame): The DataFrame.

        Returns:
            tuple: A tuple containing the NumPy representation of the DataFrame.
        """
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError("PandasToNumpy expects pd.DataFrame.")
        return (dataframe.to_numpy(),)
