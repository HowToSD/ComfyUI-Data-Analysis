from typing import Any, Dict
from matplotlib import pyplot as plt
import pandas as pd
from .util import plot_post_steps
from ..pandas_wrapper.utils import column_label_string_to_target_type

class MPLPieChart:
    """
    MPL Pie Chart:
    Generates a pie chart from a pandas DataFrame.

    Below screenshot shows a workflow to generate a pie chart from categorical data.
    ![Pie chart](../images/pie_chart.png)

    category: Plot
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `line_plot` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe": ("DATAFRAME", {}),
                "label_column_name": ("STRING", {"default": ""}),
                "data_column_name": ("STRING", {"default": ""}),
                "title": ("STRING", {"default": ""})
            }
        }

    RETURN_TYPES: tuple = ("IMAGE",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self,
                  dataframe: pd.DataFrame,
                  label_column_name: str,
                  data_column_name: str,
                  title: str) -> tuple:
        """
        Generates a pie chart from a Pandas DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.
            label_column_name (str): The column name for the labels.
            data_column_name (str): The column name for the data.
            title (str): The title of the plot.

        Returns:
            tuple: A tuple containing the image tensor representation of the plot.
        """

        df = dataframe
        label_column_name = column_label_string_to_target_type(df, label_column_name)
        data_column_name = column_label_string_to_target_type(df, data_column_name)

        # Create the plot
        fig, ax = plt.subplots()
        ax.pie(df[data_column_name], labels=df[label_column_name], autopct='%1.1f%%', startangle=140)
        return plot_post_steps(
            fig,
            ax,
            plt,
            title,
            "",
            "",
            False)
