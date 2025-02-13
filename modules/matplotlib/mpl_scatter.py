from typing import Any, Dict
from matplotlib import pyplot as plt
import pandas as pd
from .common import common_input_types
from .util import plot_post_steps

class MPLScatter:
    """
    MPLPlotScatter:
        A class for generating scatter plots from a pandas DataFrame.
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
                  dataframe_json: str,
                  x_column_name: str,
                  y_column_name: str,
                  title: str,
                  x_axis_label: str,
                  y_axis_label: str,
                  x_tick_as_int: bool) -> tuple:
        """
        Generates a scatter plot from a pandas DataFrame.

        Args:
            dataframe_json (str): A JSON string representation of the DataFrame.
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
        # Deserialize JSON string to DataFrame
        df = pd.read_json(dataframe_json)

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
