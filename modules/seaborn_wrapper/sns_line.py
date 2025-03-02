from typing import Any, Dict
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
from .common import common_input_types
from .util import plot_post_steps
from .util import set_up_sns_style_palette
from .util import process_y_columns_and_labels
from ..pandas_wrapper.utils import column_label_string_to_target_type

class SNSLine:
    """
    SNS Line Plot:
    Generates a line plot from a pandas DataFrame using Seaborn.

    For plotting multiple lines, enter a comma-separated column labels in y_column_name.
    If you want to display a legend for each line, enter a comma-separated legend label
    in legend label.

    ![SNS Line Plot](../images/sns_line.png)

    The `style` parameter can be chosen from:
    * darkgrid (default) – Grid with a dark background.
    * whitegrid – Grid with a white background.
    * dark – Dark background, no grid.
    * white – White background, no grid.
    * ticks – White background with tick marks.

    The `palette` parameter can be chosen from:
    * deep (default) – High contrast, good for multiple categories.
    * muted – Softer colors, easier on the eyes.
    * pastel – Light colors, suitable for minimalistic styles.
    * bright – Vibrant and highly saturated colors.
    * dark – Darker, high-contrast colors.
    * colorblind – Optimized for color vision deficiencies.

    category: Plot
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `line_plot` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return common_input_types()

    RETURN_TYPES: tuple = ("IMAGE",)
    FUNCTION: str = "line_plot"
    CATEGORY: str = "Data Analysis"

    def line_plot(self,
                  dataframe: pd.DataFrame,
                  x_column_name: str,
                  y_column_name: str,
                  title: str,
                  x_axis_label: str,
                  y_axis_label: str,
                  legend_label: str,
                  x_tick_as_int: bool,
                  style: str=None,
                  palette: str=None) -> tuple:
        """
        Generates a line plot from a pandas DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.
            x_column_name (str): The column name for the x-axis.
            y_column_name (str): The column name for the y-axis.
            title (str): The title of the plot.
            x_axis_label (str): The label for the x-axis data.
            y_axis_label (str): The label for the y-axis data.
            legend_label (str): The legend label of the plot.
            x_tick_as_int (bool): If set, use integers for x ticks. For example,
                                  if ticks show floating point numbers for years, e.g. 2002.5,
                                  setting this flag will show integer values instead.
            style (str): Style of the plot
            palette (str): Palette of the plot
        Returns:
            tuple: A tuple containing the image tensor representation of the plot.
        """
        df = dataframe
        set_up_sns_style_palette(style, palette)
        x_column_name = column_label_string_to_target_type(df, x_column_name)
        y_columns, labels = process_y_columns_and_labels(df, y_column_name, legend_label)

        fig, ax = plt.subplots()
        for i in range(len(y_columns)):
            sns.lineplot(x=df[x_column_name], y=df[y_columns[i]], ax=ax, label=labels[i])

        return plot_post_steps(
            fig,
            ax,
            plt,
            title,
            x_axis_label,
            y_axis_label,
            x_tick_as_int)
