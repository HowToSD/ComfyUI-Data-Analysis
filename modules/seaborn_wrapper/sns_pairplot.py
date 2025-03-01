from typing import Any, Dict
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
from .util import plot_post_steps
from .util import set_up_sns_style_palette


class SNSPairplot:
    """
    SNS Pairplot:
    Generates a pairplot from a Pandas DataFrame using Seaborn.

    Specify a column name for the hue parameter to color the data points based on that column.

    category: Plot
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `bar_chart` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe": ("DATAFRAME", {}),
                "hue_column_name": ("STRING", {"default": ""}),
                "title": ("STRING", {"default": ""}),
                "style": ("STRING", {"default": ""}),
                "palette": ("STRING", {"default": ""})
            }
        }

    RETURN_TYPES: tuple = ("IMAGE",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self,
                  dataframe: pd.DataFrame,
                  hue_column_name: str,
                  title: str,
                  style: str=None,
                  palette: str=None) -> tuple:
        """
        Generates a pairplot from a pandas DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.
            hue_column_name (str): The category (variable) column name.
            title (str): The title of the plot.
            style (str): Style of the plot
            palette (str): Palette of the plot
        Returns:
            tuple: A tuple containing the image tensor representation of the plot.
        """
        df = dataframe
        set_up_sns_style_palette(style, palette)

        # Create the plot
        if hue_column_name:
            pp = sns.pairplot(df, hue=hue_column_name)
        else:
            pp = sns.pairplot(df)
        
        pp.figure.suptitle(title, y=0.95)
        pp.figure.tight_layout(rect=[0, 0, 1, 0.95]) 
        fig = pp.figure

        return plot_post_steps(
            fig,
            None,
            plt,
            title,
            None,
            None,
            None)
