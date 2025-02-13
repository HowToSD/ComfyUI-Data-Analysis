from typing import Dict, Type, TypeVar
from .modules.matplotlib.mpl_bar import MPLBar
from .modules.matplotlib.mpl_line import MPLLine
from .modules.matplotlib.mpl_scatter import MPLScatter
from .modules.pandas.pandas_head import PandasHead
from .modules.pandas.pandas_join import PandasJoin
from .modules.pandas.pandas_load_csv import PandasLoadCSV
from .modules.pandas.pandas_select_columns import PandasSelectColumns
from .modules.pandas.pandas_select_rows import PandasSelectRows
from .modules.pandas.pandas_show_dataframe import PandasShowDataFrame
from .modules.pandas.pandas_sort import PandasSort
from .modules.pandas.pandas_summary import PandasSummary
from .modules.pandas.pandas_to_string import PandasToString

T = TypeVar("T")

NODE_CLASS_MAPPINGS: Dict[str, Type[T]] = {
    "MPLBar": MPLBar,
    "MPLLine": MPLLine,
    "MPLScatter": MPLScatter,
    "PandasHead": PandasHead,
    "PandasJoin": PandasJoin,
    "PandasLoadCSV": PandasLoadCSV,
    "PandasSelectColumns": PandasSelectColumns,
    "PandasSelectRows": PandasSelectRows,
    "PandasShowDataFrame": PandasShowDataFrame,
    "PandasSort": PandasSort,
    "PandasSummary": PandasSummary,
    "PandasToString": PandasToString,
}
"""
NODE_CLASS_MAPPINGS (Dict[str, Type[T]]):
    A dictionary mapping node names to their corresponding class implementations.

    - "MPLBar": Generates a bar chart from DataFrame data.
    - "MPLLine": Generates a line plot from DataFrame data.
    - "MPLScatter": Generates a scatter plot from DataFrame data.
    - "PandasHead": Handles retrieving the first few rows of a DataFrame.
    - "PandasJoin": Provides functionality to join multiple DataFrames.
    - "PandasLoadCSV": Loads CSV data into a DataFrame.
    - "PandasSelectColumns": Selects specific columns from a DataFrame.
    - "PandasSelectRows": Filters specific rows from a DataFrame.
    - "PandasShowDataFrame": Displays the content of the DataFrame.
    - "PandasSort": Sorts a DataFrame based on given criteria.
    - "PandasSummary": Provides a summary of a DataFrame.
    - "PandasToString": Converts a DataFrame to a string representation.
"""

NODE_DISPLAY_NAME_MAPPINGS: Dict[str, str] = {
    "MPLBar": "MPL Bar Chart",
    "MPLLine": "MPL Line Plot",
    "MPLScatter": "MPL Scatter Plot",
    "PandasHead": "Pandas Head",
    "PandasJoin": "Pandas Join",
    "PandasLoadCSV": "Pandas Load CSV",
    "PandasSelectColumns": "Pandas Select Columns",
    "PandasSelectRows": "Pandas Select Rows",
    "PandasShowDataFrame": "Pandas Show DataFrame",
    "PandasSort": "Pandas Sort",
    "PandasSummary": "Pandas Summary",
    "PandasToString": "Pandas To String",
}
"""
NODE_DISPLAY_NAME_MAPPINGS (Dict[str, str]):
    A dictionary mapping node names to user-friendly display names.
"""

"""
Below two lines were taken from:
https://github.com/pythongosssss/ComfyUI-Custom-Scripts/blob/main/__init__.py
See credit/credit.md for the full license.
"""
WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
