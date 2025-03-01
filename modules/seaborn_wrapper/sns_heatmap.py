from typing import Any, Dict
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
from .util import plot_post_steps


class SNSHeatmap:
    """
    SNS Heatmap:
    Generates a heatmap from a Pandas DataFrame using Seaborn.

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
                "title": ("STRING", {"default": ""}),
                "palette": ("STRING", {"default": ""})
            }
        }

    RETURN_TYPES: tuple = ("IMAGE",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self,
         dataframe: pd.DataFrame,
         title: str,
         palette: str=None) -> tuple:
        """
        Generates a heatmap from a Pandas DataFrame using Seaborn.

        Args:
            dataframe (DataFrame): The DataFrame.
            title (str): The title of the plot.
            palette (str): Palette of the plot
        Returns:
            tuple: A tuple containing the image tensor representation of the plot.
        """
        # set_up_sns_style_palette(style, palette) won't work for heatmap

        # Create the plot
        fig, ax = plt.subplots()
        corr = dataframe.corr()
        if palette:
            sns.heatmap(corr, annot=True, ax=ax, cmap=sns.color_palette(palette, as_cmap=True))
        else:
            sns.heatmap(corr, annot=True, ax=ax)

        return plot_post_steps(
            fig,
            ax,
            plt,
            title,
            None,
            None,
            None)
