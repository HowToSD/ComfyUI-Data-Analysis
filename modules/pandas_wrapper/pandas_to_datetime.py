from typing import Any, Dict
import pandas as pd
import pandas.api.types as ptypes


class PandasToDatetime:
    """
    Converts one or more string columns in a DataFrame to datetime columns.

    Note: When only the time portion is provided, the date defaults to 1900-01-01.
    Refer to [https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior](the Python documentation) for valid date/time format strings.

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
        Converts one or more string columns to datetime columns.

        Args:
            dataframe (DataFrame): The DataFrame.
            column_names (str): A comma-separated string of column names containing date time strings.
            date_format (str): A date format.

        Returns:
            tuple: A tuple containing the DataFrame with selected columns.
        """
        date_columns = [col.strip() for col in column_names.split(",")]
        df2 = dataframe.apply(lambda col: pd.to_datetime(col, format=date_format) if col.name in date_columns else col)
        return (df2,)
