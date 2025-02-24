import os
import sys
from typing import Any, Dict
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from cda.utils import python_dict_first_value_len

class PandasCreateFromDict:
    """
    Creates a pandas DataFrame from a Python dictionary.

    category: IO
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `create` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "data": ("PYDICT", {}),
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, data: Dict) -> tuple:
        """
        Creates a pandas DataFrame from a Python dictionary.

        Args:
            data (Dict): A Python dictionary.

        Returns:
            tuple: A tuple containing a the DataFrame.
        """
        if not data:
            df = pd.DataFrame()  # Return an empty DataFrame if no data is provided.
        else:
            value_length = python_dict_first_value_len(data)
            df = pd.DataFrame(data, index=list(range(value_length)))

        return (df,)
