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
from seaborn_wrapper.common import common_input_types_y_only_bin_pt
from seaborn_wrapper.util import plot_post_steps
from seaborn_wrapper.util import set_up_sns_style_palette


class SNSHistogramPt:
    """
    SNS Histogram Pt:
    Generates a histogram from a PyTorch tensor using Seaborn.

    category: Plot
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return common_input_types_y_only_bin_pt()

    RETURN_TYPES: tuple = ("IMAGE",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self,
                  tens: torch.Tensor,
                  y_axis_dims: str,
                  title: str,
                  y_axis_label: str,
                  # legend_label: str,
                  bins: int,
                  style: str=None,
                  palette: str=None) -> tuple:
        """
        Generates a histogram from a PyTorch tensor using Seaborn.

        Args:
            tens (torch.Tensor): The tensor.
            y_axix_dims (str): The indices in tensor for the y-axis.
            y_column_name (str): The column name for the y-axis.
            title (str): The title of the plot.
            y_axis_label (str): The label for the y-axis data.
            bins (int): Number of bins.
            style (str): Style of the plot
            palette (str): Palette of the plot
        Returns:
            tuple: A tuple containing the image tensor representation of the plot.
        """
        y_axes = ast.literal_eval(y_axis_dims)
        if isinstance(y_axes, int):
            y_axes = [y_axes]

        if tens.dim() > 2:
            raise ValueError("Only rank 1 or 2 tensors are supported.")

        if tens.dim() == 1:
            tens2 = torch.unsqueeze(tens, 1)
        else:
            tens2 = tens

        labels = [""] * len(y_axes)
        set_up_sns_style_palette(style, palette)

         # Create the plot
        fig, ax = plt.subplots()
        for i in range(len(y_axes)):
            sns.histplot(tens2[:, y_axes[i]].detach().cpu().numpy(),
                         bins=bins, ax=ax, label=labels[i])
            break  # TODO: Remove this if we decide support multiple plots

        return plot_post_steps(
            fig,
            ax,
            plt,
            title,
            None,
            y_axis_label,
            None)