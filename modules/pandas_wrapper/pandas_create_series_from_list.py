from typing import List, Any, Tuple, Dict
import pandas as pd


class PandasCreateSeriesFromList:
    """
    Creates a Pandas Series from a Python list.

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
                "data": ("PYLIST", {}),
            }
        }

    RETURN_TYPES: tuple = ("PDSERIES",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, data: List[Any]) -> Tuple[pd.Series]:
        """
        Creates a Pandas Series from a Python list.

        Args:
            data (List[Any]): A list with cell values.

        Returns:
            Tuple[pd.Series]: A tuple containing a Pandas Series.

        Raises:
            ValueError: If the data is not a list.
        """
        if not isinstance(data, list):
            raise ValueError("Input must be a list.")

        if len(data) == 0:
            return (pd.Series(),)
        else:
             return (pd.Series(data),)

