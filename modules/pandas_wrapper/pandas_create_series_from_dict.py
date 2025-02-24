import os
import sys
from typing import Dict, Any, Tuple
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from cda.utils import python_dict_first_value_len

class PandasCreateSeriesFromDict:
    """
    Creates a Pandas Series from a Python dictionary.

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
                "data": ("PYDICT", {}),
            }
        }

    RETURN_TYPES: tuple = ("PDSERIES",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, data: Dict[Any, Any]) -> Tuple[pd.Series]:
        """
        Creates a Pandas Series from a Python dictionary.

        Args:
            data (Dict[Any, Any]): A dictionary with exactly one key-value pair.

        Returns:
            Tuple[pd.Series]: A tuple containing a Pandas Series.

        Raises:
            ValueError: If the dictionary does not have exactly one key-value pair,
                        or if the value is not a scalar.
        """
        if not isinstance(data, dict):
            raise ValueError("Input must be a dictionary.")

        if len(data) == 0:
            return (pd.Series(),)
        else:
            for v in iter(data.values()):
                if isinstance(v, (list, dict, set, tuple)):
                    raise ValueError("Value must be a scalar.")

            return (pd.Series(data),)

