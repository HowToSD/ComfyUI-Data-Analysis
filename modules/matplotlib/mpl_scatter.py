from typing import Any, Dict
from matplotlib import pyplot as plt
from io import StringIO
import pandas as pd
from .common import common_input_types
from .util import plot_post_steps
from ..pandas_wrapper.utils import column_label_string_to_target_type

class MPLScatter:
    """
    MPL Scatter Plot:
        Generates a scatter plot from a pandas DataFrame.

    category: Plot
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `scatter_plot` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return common_input_types()

    RETURN_TYPES: tuple = ("IMAGE",)
    FUNCTION: str = "scatter_plot"
    CATEGORY: str = "Data Analysis"

    def scatter_plot(self,
                  dataframe: pd.DataFrame,
                  x_column_name: str,
                  y_column_name: str,
                  title: str,
                  x_axis_label: str,
                  y_axis_label: str,
                  x_tick_as_int: bool) -> tuple:
        """
        Generates a scatter plot from a pandas DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.
            x_column_name (str): The column name for the x-axis.
            y_column_name (str): The column name for the y-axis.
            title (str): The title of the plot.
            x_axis_label (str): The label for the x-axis data.
            y_axis_label (str): The label for the y-axis data.
            x_tick_as_int (bool): If set, use integers for x ticks. For example,
                                  if ticks show floating point numbers for years, e.g. 2002.5,
                                  setting this flag will show integer values instead.
        Returns:
            tuple: A tuple containing the image tensor representation of the plot.
        """

        df = dataframe
        x_column_name = column_label_string_to_target_type(df, x_column_name)
        y_column_name = column_label_string_to_target_type(df, y_column_name)

        # Create the plot
        fig, ax = plt.subplots()
        ax.scatter(df[x_column_name], df[y_column_name])

        return plot_post_steps(
            fig,
            ax,
            plt,
            title,
            x_axis_label,
            y_axis_label,
            x_tick_as_int)
