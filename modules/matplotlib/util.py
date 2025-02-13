import io
from typing import Any, Dict
import numpy as np
import matplotlib.figure
import matplotlib.axes
from matplotlib import pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd
from PIL import Image
import torch


def plot_post_steps(
    fig: matplotlib.figure.Figure,
    ax: matplotlib.axes.Axes,
    plt: plt,
    title: str,
    x_axis_label: str,
    y_axis_label: str,
    x_tick_as_int: bool
) -> tuple:
    r"""Plots a post-processed step plot using Matplotlib.

    Args:
        fig (matplotlib.figure.Figure): The figure object for the plot.
        ax (matplotlib.axes.Axes): The axes object for the plot.
        plt (module): The Matplotlib module.
        title (str): The title of the plot.
        x_axis_label (str): The label for the x-axis.
        y_axis_label (str): The label for the y-axis.
        x_tick_as_int (bool): If ``True``, use integers for x-axis ticks. 
            For example, if ticks display floating point numbers (e.g., 2002.5), 
            setting this flag forces integer values instead.

    Returns:
        tuple: A tuple containing the image tensor representation of the plot.
    """
    if x_tick_as_int:
        ax.xaxis.set_major_locator(mticker.MaxNLocator(integer=True))

    # Set title and labels
    ax.set_title(title)
    ax.set_xlabel(x_axis_label)
    ax.set_ylabel(y_axis_label)

    # Save the plot to a buffer
    buf = io.BytesIO()
    fig.savefig(buf, format='PNG')
    buf.seek(0)
    plt.close(fig)  # Close the figure to free memory

    # Load image and convert to tensor
    image = Image.open(buf).convert("RGB")
    image_tensor = torch.from_numpy(np.array(image)).float() / 255.0  # Normalize to [0,1]
    image_tensor = image_tensor.unsqueeze(0)
    return (image_tensor,)