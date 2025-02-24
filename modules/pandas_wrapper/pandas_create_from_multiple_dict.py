import os
import sys
from typing import Any, Dict
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from cda.utils import python_dict_first_value_len

class PandasCreateFromMultipleDict:
    """
    Creates a pandas DataFrame from multiple Python dictionaries.

    Use this node to create a DataFrame from below nodes:
    * Py Kv Float Create
    * Py Kv Int Create
    * Py Kv String Create
    Each of above can be used to set a column name and the value for the column.

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
                "dict1": ("PYDICT", {}),
                "dict2": ("PYDICT", {}),
            },
            "optional":{
                "dict3": ("PYDICT", {}),
                "dict4": ("PYDICT", {}),
                "dict5": ("PYDICT", {}),
                "dict6": ("PYDICT", {}),
                "dict7": ("PYDICT", {}),
                "dict8": ("PYDICT", {}),
                "dict9": ("PYDICT", {}),
                "dict10": ("PYDICT", {})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self,
          dict1: Dict, 
          dict2: Dict,
          dict3: Dict=None,
          dict4: Dict=None,
          dict5: Dict=None,
          dict6: Dict=None,
          dict7: Dict=None,
          dict8: Dict=None,
          dict9: Dict=None,
          dict10: Dict=None
          ) -> tuple:
        """
        Creates a pandas DataFrame from a Python dictionary.

        Args:
            dict1, 2, ... ,10 (Dict): A Python dictionary.

        Returns:
            tuple: A tuple containing a the DataFrame.
        """
        dict_list = [d for d in (dict1, dict2, dict3, dict4, dict5, dict6, dict7, dict8, dict9, dict10) if d]

        if dict_list[0] is None or dict_list[1] is None:
            raise ValueError("Either or both of the first two dictionaries are None.")

        if not dict_list[0] or not dict_list[1]:
            # Return an empty DataFrame if an empty dict is provided for the first dictionary
            # or the second dictionary.
            df = pd.DataFrame()
        else:
            expected_length = python_dict_first_value_len(dict_list[0])

            for d in dict_list[1:]:
                if expected_length != python_dict_first_value_len(d):
                    raise ValueError("Length of the value elements are not the same.")

            merged_dict = {}
            for d in dict_list:
                merged_dict.update(d)
            df = pd.DataFrame(merged_dict, index=list(range(expected_length)))
        return (df,)
