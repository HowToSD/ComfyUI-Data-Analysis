from typing import Any, Dict
import pandas as pd


class PandasLoadHTML:
    """
    Pandas Load HTML:
    Scans an HTML file or webpage for tables and returns the number of DataFrames 
    found, followed by a list of up to 10 DataFrames. Each table is represented 
    as a separate DataFrame. If fewer than 10 tables are found, empty DataFrames 
    fill the remaining slots.

    When loading from a URL, additional cleanup may be required.
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
                "file_path": ("STRING", {"multiline": False}),
            }
        }

    # TODO: Reference doc generator script cannot parse programatically defined
    #       list yet, so we need to list return types for now.
    RETURN_TYPES: tuple = ("INT",
                           "DATAFRAME", "DATAFRAME", "DATAFRAME","DATAFRAME",
                           "DATAFRAME", "DATAFRAME", "DATAFRAME", "DATAFRAME",
                           "DATAFRAME", "DATAFRAME")
    RETURN_NAMES: tuple = ("Number of DataFrames",
                           "DataFrame1", "DataFrame2", "DataFrame3", "DataFrame4",
                           "DataFrame5", "DataFrame6", "DataFrame7", "DataFrame8",
                           "DataFrame9", "DataFrame10")
    assert(len(RETURN_NAMES) == len(RETURN_TYPES))

    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    @classmethod
    def IS_CHANGED(cls, **kw):
        return float("NaN")

    def f(self, file_path: str) -> tuple:
        """
        Loads an HTML file into a pandas DataFrame.

        Args:
            file_path (str): The path to the HTML file. The path can be a URL.

        Returns:
            tuple: A tuple containing a DataFrame.
        """
        try:
            dfs = pd.read_html(file_path, flavor="lxml")
        except:
            dfs = []
            num_dfs = 0

        if dfs is None:
            num_dfs = 0
            dfs =  []
        else:
            num_dfs = len(dfs)

        df_slot_count = len(PandasLoadHTML.RETURN_TYPES) - 1
        filler_count = df_slot_count - num_dfs
        empty_dfs = [pd.DataFrame({})] * filler_count  # If filler = 0, this will still return []
        dfs_out = dfs + empty_dfs
        return tuple([num_dfs] + dfs_out)
