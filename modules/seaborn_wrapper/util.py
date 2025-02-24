import io
from typing import List, Tuple
import numpy as np
import matplotlib.figure
import matplotlib.axes
from matplotlib import pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
from PIL import Image
import torch
import pandas as pd
import seaborn as sns
from typing import Optional
from ..pandas_wrapper.utils import column_labels_string_to_list
from ..pandas_wrapper.utils import comma_separated_labels_string_to_list


def process_y_columns_and_labels(df:pd.DataFrame, y_column_name: str, legend_label: str) -> Tuple[List[str], List[str]]:
    """
    Generates a y column list and legend label list from the comma-separated y column names and legend label string.
    
    Args:
        df (pd.DataFrame): The input dataframe containing the data.
        y_column_name (str): A comma-separated string of column names to be used as y-values.
        legend_label (str): A comma-separated string of labels corresponding to the y columns.
    
    Returns:
        List[str]: A list of processed y column names.
        List[str]: A list of processed legend labels.
    """
    y_columns = column_labels_string_to_list(df, y_column_name)
    if legend_label:
        labels = comma_separated_labels_string_to_list(legend_label)
        if len(labels) < len(y_columns):
            labels = labels + [""] * (len(y_columns) - len(labels))
    else:
        labels = [""] * len(y_columns)

    return y_columns, labels


def set_up_sns_style_palette(style: Optional[str], palette: Optional[str]) -> None:
    """
    Sets the Seaborn theme with the given style and palette.

    Args:
        style (Optional[str]): The style to apply to the Seaborn theme (e.g., 'darkgrid', 'whitegrid').
        palette (Optional[str]): The color palette to apply (e.g., 'deep', 'muted').

    Returns:
        None
    """
    if style and palette:
        sns.set_theme(style=style, palette=palette)
    elif style:
        sns.set_theme(style=style)
    elif palette:
        sns.set_theme(palette=palette)
    else:
        sns.set_theme()


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
    if x_axis_label:
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