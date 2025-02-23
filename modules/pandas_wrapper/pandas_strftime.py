from typing import Any, Dict
import pandas as pd
import pandas.api.types as ptypes


class PandasStrftime:
    """
    Converts one or more datetime columns in a DataFrame to string columns.

    Refer to [https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior](Python document) for date/time format strings.

    category: Date and time processing
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
                "column_names": ("STRING", {"default": ""}),
                "date_format": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame, column_names: str, date_format: str) -> tuple:
        """
        Converts one or more datetime columns in a DataFrame to string columns.

        Args:
            dataframe (DataFrame): The DataFrame.
            column_names (str): A comma-separated string of column names containing datetime values.
            date_format (str): A date format string for strftime.

        Returns:
            tuple: A tuple containing the DataFrame with formatted date columns.
        """
        date_columns = [col.strip() for col in column_names.split(",")]
        
        df2 = dataframe.copy()
        df2[date_columns] = df2[date_columns].apply(
            # Keep the datetime column check in case the user specifies the non-date column
            lambda col: col.dt.strftime(date_format) if ptypes.is_datetime64_any_dtype(col) else col
        )

        return (df2,)
