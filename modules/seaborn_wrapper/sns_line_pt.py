import os
import sys
from typing import Any, Dict
from matplotlib import pyplot as plt
import seaborn as sns
import torch
import ast
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from seaborn_wrapper.common import common_input_types_pt
from seaborn_wrapper.util import plot_post_steps
from seaborn_wrapper.util import set_up_sns_style_palette
from seaborn_wrapper.util import comma_separated_labels_string_to_list

class SNSLinePt:
    """
    SNS Line Plot Pt:
    Generates a line plot from a PyTorch tensor using Seaborn.

    For plotting multiple lines, enter a comma-separated column labels in y_axis_dims.
    If you want to display a legend for each line, enter a comma-separated legend label
    in legend label.

    category: Plot
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `line_plot` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return common_input_types_pt()

    RETURN_TYPES: tuple = ("IMAGE",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self,
                  tens: torch.Tensor,
                  x_axis_dim: int,
                  y_axis_dims: str,
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
            tens (torch.Tensor): The tensor.
            x_axis_dim (int): The index in tensor for the x-axis.
            y_axix_dims (str): The indices in tensor for the y-axis.
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
        y_axes = ast.literal_eval(y_axis_dims)
        if isinstance(y_axes, int):
            y_axes = [y_axes]

        if tens.dim() != 2:
            raise ValueError("Only rank 2 tensors are supported.")

        label_list = comma_separated_labels_string_to_list(legend_label)
        if len(y_axes) != len(label_list):
            if len(label_list) > len(y_axes):
               raise ValueError("More labels were specified than y-axis indices.")
            else:
               label_list += [""] * (len(y_axes) - len(label_list))

        set_up_sns_style_palette(style, palette)

        fig, ax = plt.subplots()
        for i in range(len(y_axes)):
            sns.lineplot(
                x=tens[:, x_axis_dim].detach().cpu().numpy(),
                y=tens[:, y_axes[i]].detach().cpu().numpy(),
                ax=ax, label=label_list[i])

        return plot_post_steps(
            fig,
            ax,
            plt,
            title,
            x_axis_label,
            y_axis_label,
            x_tick_as_int)
