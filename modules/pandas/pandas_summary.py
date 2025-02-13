from typing import Any, Dict
import pandas as pd

class PandasSummary:
    """
    PandasSummary:
        A class for analyzing and summarizing a pandas DataFrame.
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `analyze_dataframe` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe_json": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "analyze_dataframe"
    CATEGORY: str = "Data Analysis"

    def analyze_dataframe(self, dataframe_json: str) -> tuple:
        """
        Analyzes a pandas DataFrame and returns a summary.

        Args:
            dataframe_json (str): A JSON string representation of the DataFrame.

        Returns:
            tuple: A tuple containing a string representation of the DataFrame summary.
        """
        # Deserialize JSON string to DataFrame
        df = pd.read_json(dataframe_json)

        # Perform summary operation
        summary = df.describe()

        return (str(summary),)
