from typing import Any, Dict
import pandas as pd

class PandasXs:
    """
    Selects a subset of a Pandas DataFrame using specified index labels or positions.

    This function extracts a portion of a DataFrame based on MultiIndex labels (row indices or column labels).

    Users must specify:
    * The labels to select (comma-separated for multiple labels).
    * The level(s) within the MultiIndex (integer positions).
    * The axis (whether selecting from rows or columns).

    **Understanding "Level":**
    In a MultiIndex DataFrame, a level refers to the hierarchical position of an index within the MultiIndex, which can be referenced using a 0-based integer position or an assigned level name.
    Selecting the level using an integer position is similar to integer-based selection in `iloc`.

    When specifying a label, Pandas needs to know which level of the MultiIndex to search. 
    For example, if selecting "dog" as a row label and the DataFrame has multiple index levels, 
    you must indicate whether to look in the first index (level 0) or the second index (level 1). 

    If selecting multiple labels, their corresponding levels should be provided as a comma-separated list.
    
    Example:
        Given a DataFrame with a 3-level MultiIndex, the first index is at level 0, the second at level 1, and the third at level 2. Selecting "dog" and "brown" at levels 1 and 2 requires specifying 1, 2 in the Level field of the node. These values are internally converted into a list and passed to Pandas.

    The `axis` field specifies whether selection applies to row indices (`axis=0`) or column labels (`axis=1`).

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
                "row_or_column_label": ("STRING", {"default": ""}),
                "label_type":(("string", "int"),),
                "level": ("STRING", {"default": ""}),
                "level_type":(("int", "string"),),
                "axis": (("index", "columns"),)
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame,
             row_or_column_label: str,
             label_type: str,
             level: str,
             level_type: str,
             axis: str) -> tuple:
        """
        Selects a subset of a Pandas DataFrame using specified index labels or positions.

        Args:
            dataframe (DataFrame): The DataFrame.
            row_or_column (str): A comma-separated MultiIndex label for the row or label.
            label_type (str): The data type of the row index or column label.
            level (str): A comma-separated level list for the MultiIndex to select.
            level_type (str): The data type of the level.
            axis (str): Specifies whether labels are for a row or column.

        Returns:
            tuple: A tuple containing the Pandas DataFrame.
        """
        # Extract index list
        # We need to pass a tuple of MultiIndex.
        # e.g. if the first index is A, second is B, we need to pass:
        # ("A", "B")
        ind_list = [e.strip() for e in row_or_column_label.split(",")]
        
        # This will throw an exception if the MultiIndex is not an int.
        if label_type == "int": 
            ind_list = [int(e) for e in ind_list]

        ind_tuple = tuple(ind_list)  # Convert the list to a tuple
        if len(ind_tuple) == 1:  # Do not enclose in tuple if only 1 index is specified
            ind = ind_tuple[0]
        else:
            ind = ind_tuple

        # Extract level list
        if len(level) == 0:
            level = None
        else:
            level_list = [e.strip() for e in level.split(",")]

            # This will throw an exception if the MultiIndex is not an int.
            if level_type == "int": 
                level_list = [int(e) for e in level_list]

            if len(level_list) == 1:
                level = level_list[0]
            else:
                level = level_list

        df_out = dataframe.sort_index().xs(
            ind,
            level=level,
            axis=axis
        )
        return (df_out,)
