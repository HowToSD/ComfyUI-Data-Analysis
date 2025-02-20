from typing import Any, Dict
import pandas as pd


class PandasRename:
    """
    Renames an index (row label) or a column label.

    Note below node parameter description is incomplete due to a reference generator's bug:
    * axis takes columns or index.

    category: Transformation
    """
    # TODO: Fix parameter description in node reference doc.

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
                "current_label": ("STRING", {"default": ""}),
                "new_label": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame, axis: str, current_label: str, new_label: str) -> tuple:
        """
        Renames an index (row label) or a column label.

        Args:
            dataframe (DataFrame): The DataFrame.
            axis (str): Index (row label) or column label.
            current_label (str): The current label.
            new_label (str): The new label.

        Returns:
            tuple: A tuple containing a JSON string of the renamed DataFrame.
        """
        if axis=="index":
            df_out = dataframe.rename(index={current_label:new_label})
        elif axis=="columns":
            df_out = dataframe.rename(columns={current_label:new_label})
        else:
            raise ValueError("Invalid axis. Only index or columns are supported.")
        return (df_out,)
