from typing import Any, Dict
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
from .common import common_input_types_y_only_bin
from .util import plot_post_steps
from .util import set_up_sns_style_palette
from .util import process_y_columns_and_labels


class SNSHistogram:
    """
    SNS Histogram:
    Generates a histogram from a Pandas DataFrame using Seaborn.

    Currently, plotting multiple series of data is not supported.
    For style and palette parameters, refer to [SNS Line Plot documentation](sns_line.md).

    category: Plot
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `bar_chart` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return common_input_types_y_only_bin()

    RETURN_TYPES: tuple = ("IMAGE",)
    FUNCTION: str = "bar_chart"
    CATEGORY: str = "Data Analysis"

    def bar_chart(self,
                  dataframe: pd.DataFrame,
                  y_column_name: str,
                  title: str,
                  y_axis_label: str,
                  # legend_label: str,
                  bins: int,
                  style: str=None,
                  palette: str=None) -> tuple:
        """
        Generates a bar chart from a pandas DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.
            y_column_name (str): The column name for the y-axis.
            title (str): The title of the plot.
            y_axis_label (str): The label for the y-axis data.
            bins (int): Number of bins.
            style (str): Style of the plot
            palette (str): Palette of the plot
        Returns:
            tuple: A tuple containing the image tensor representation of the plot.
        """
        df = dataframe
        set_up_sns_style_palette(style, palette)

        # TODO: For future enhancement, restore legend_label as the last arg.
        y_columns, labels = process_y_columns_and_labels(df, y_column_name, "")

        # Create the plot
        fig, ax = plt.subplots()
        for i in range(len(y_columns)):
            sns.histplot(df[y_columns[i]], bins=bins, ax=ax, label=labels[i])
            break  # TODO: Remove this if we decide support multiple plots

        return plot_post_steps(
            fig,
            ax,
            plt,
            title,
            None,
            y_axis_label,
            None)
