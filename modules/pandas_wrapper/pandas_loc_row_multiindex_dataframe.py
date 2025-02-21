from typing import Any, Dict
import pandas as pd

class PandasLocRowMultiIndexDataFrame:
    """
    Selects a row from a pandas DataFrame with MultiIndex and output as a DataFrame.

    Specify comma-separated MultiIndex labels (row index) and the data type for the MultiIndex to select a row.

    Below screenshots illustrate these options:
    ![PandasLocRowMultiIndexDataFrame](../images/multiindex.png)

    The top DataFrame has an integer-type MultiIndex, while the bottom DataFrame has a string-type MultiIndex. In both cases, two index values are specified to select a single row while the correct MultiIndex data type is also selected. Note that mixed data types for MultiIndex are not currently supported.

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
                "row_index": ("STRING", {"default": ""}),
                "row_index_type":(("string", "int"),)
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame,
             row_index: str,
             row_index_type: str) -> tuple:
        """
        Selects a specific row using a comma-separated MultiIndex labels (row index) from a pandas DataFrame, and returns the DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.
            row_index (str): A comma-separated MultiIndex label for the row.
            row_index_type (str): The data type of the row index.

        Returns:
            tuple: A tuple containing the Pandas DataFrame.
        """
        # We need to pass a tuple of MultiIndex.
        # e.g. if the first index is A, second is B, we need to pass:
        # ("A", "B")
        ind_list = [ind.strip() for ind in row_index.split(",")]
        
        # This will throw an exception if the MultiIndex is not an int.
        if row_index_type == "int": 
            ind_list = [int(ind) for ind in ind_list]
        
        ind_tuple = tuple(ind_list)

        # We need to wrap it to get the DataFrame. Otherwise, we will get a Series.
        ind_tuple_list = [ind_tuple] 
        value = dataframe.loc[ind_tuple_list]
        return (value,)
