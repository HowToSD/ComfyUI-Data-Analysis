from typing import Any, Dict
import pandas as pd
import ast

class PandasRenameAdvanced:
    """
    Renames one or more indices (row labels) or column labels to new labels.

    Specify the replacement in a Python dictionary format:
    ```
    {
        "old_foo": "new_bar",
        0: 5
    }
    ```
    A string label has to be double-quoted.

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
                "dataframe": ("DATAFRAME", {}),
                "axis": (("columns", "index"),),
                "replacement_pairs": ("STRING", {"default":"{}", "multiline": True})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame, axis: str, replacement_pairs: str) -> tuple:
        """
        Renames one or more indices (row labels) or column labels to new labels.

        Args:
            dataframe (DataFrame): The DataFrame.
            axis (str): Index (row label) or column label.
            replacement_pairs (str): Replacement pairs specified in the Python dictionary format.

        Returns:
            tuple: A tuple containing the DataFrame.
        """
        try:
            d = ast.literal_eval(replacement_pairs)
            if not isinstance(d, dict):
                raise ValueError("replacement_pairs must be a dictionary.")

            # Check that values in the dictionary are not lists, tuples, or dictionaries
            if any(isinstance(value, (list, tuple, dict)) for value in d.values()):
                raise ValueError("replacement_pairs values must not be lists, tuples, or dictionaries.")

        except (SyntaxError, ValueError) as e:
            raise ValueError(f"Invalid replacement_pairs format: {e}")

        if axis == "index":
            df_out = dataframe.rename(index=d)
        elif axis == "columns":
            df_out = dataframe.rename(columns=d)
        else:
            raise ValueError("Invalid axis. Only 'index' or 'columns' are supported.")
        
        return (df_out,)
