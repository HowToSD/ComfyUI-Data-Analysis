from typing import Any, Dict
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
from .util import plot_post_steps
from .util import set_up_sns_style_palette
from ..pandas_wrapper.utils import column_label_string_to_target_type

class SNSBoxplot:
    """
    SNS Boxplot:
    Generates a boxplot from a Pandas DataFrame using Seaborn.

    You can generate a boxplot from either a single column or two columns.  
    * For two columns, the first column should contain the category, and the second column should contain the corresponding numerical values.  
    * For a wide-format table, use the Pandas Melt node to create a category column first. This column is referred to as the "variable" column in melting.  
    * For a single-column dataset, leave the category field blank.

    For example, if you have a DataFrame tracking apple and banana prices at various stores:
    ```
     Fruit  Price
     apple    5
     apple    3
     apple    2
     appel    2.5
     banana   4
     banana   2
     banana   2
    ```
    If you specify `Fruit` as the category and `Price` as the value, two boxplots will be generated: one for apples and one for bananas.

    ![Boxplot](../images/boxplot.png)

    Refer to [Seaborn documentation](https://seaborn.pydata.org/generated/seaborn.boxplot.html) for more information.

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
                "category_column_name": ("STRING", {"default": ""}),
                "value_column_name": ("STRING", {"default": ""}),
                "title": ("STRING", {"default": ""}),
                "style": ("STRING", {"default": ""}),
                "palette": ("STRING", {"default": ""})
            }
        }

    RETURN_TYPES: tuple = ("IMAGE",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self,
                  dataframe: pd.DataFrame,
                  category_column_name: str,
                  value_column_name: str,
                  title: str,
                  style: str=None,
                  palette: str=None) -> tuple:
        """
        Generates a bar chart from a pandas DataFrame.

        Args:
            dataframe (DataFrame): The DataFrame.
            category_column_name (str): The category (variable) column name.
            value_column_name (str): The column name for the value data.
            title (str): The title of the plot.
            style (str): Style of the plot
            palette (str): Palette of the plot
        Returns:
            tuple: A tuple containing the image tensor representation of the plot.
        """
        df = dataframe
        set_up_sns_style_palette(style, palette)
        category_column_name = column_label_string_to_target_type(df, category_column_name, return_none=True)
        value_column_name = column_label_string_to_target_type(df, value_column_name)

        # Create the plot
        fig, ax = plt.subplots()
        if category_column_name:
            sns.boxplot(x=df[category_column_name],y=df[value_column_name], ax=ax)
        else:
            sns.boxplot(y=df[value_column_name], ax=ax)
        
        return plot_post_steps(
            fig,
            ax,
            plt,
            title,
            None,
            None,
            None)
