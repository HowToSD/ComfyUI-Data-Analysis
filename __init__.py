from typing import Dict, Type, TypeVar
from .modules.matplotlib.mpl_bar import MPLBar
from .modules.matplotlib.mpl_line import MPLLine
from .modules.matplotlib.mpl_scatter import MPLScatter
from .modules.pandas_wrapper.pandas_columns import PandasColumns
from .modules.pandas_wrapper.pandas_create import PandasCreate
from .modules.pandas_wrapper.pandas_create_with_index import PandasCreateWithIndex
from .modules.pandas_wrapper.pandas_head import PandasHead
from .modules.pandas_wrapper.pandas_index import PandasIndex
from .modules.pandas_wrapper.pandas_join import PandasJoin
from .modules.pandas_wrapper.pandas_load_csv import PandasLoadCSV
from .modules.pandas_wrapper.pandas_load_csv_with_index import PandasLoadCSVWithIndex
from .modules.pandas_wrapper.pandas_loc_cell_str import PandasLocCellStr
from .modules.pandas_wrapper.pandas_save_csv import PandasSaveCSV
from .modules.pandas_wrapper.pandas_select_columns import PandasSelectColumns
from .modules.pandas_wrapper.pandas_select_rows import PandasSelectRows
from .modules.pandas_wrapper.pandas_show_dataframe import PandasShowDataFrame
from .modules.pandas_wrapper.pandas_show_text import PandasShowText
from .modules.pandas_wrapper.pandas_sort import PandasSort
from .modules.pandas_wrapper.pandas_summary import PandasSummary
from .modules.pandas_wrapper.pandas_to_string import PandasToString

T = TypeVar("T")

NODE_CLASS_MAPPINGS: Dict[str, Type[T]] = {
    "MPLBar": MPLBar,
    "MPLLine": MPLLine,
    "MPLScatter": MPLScatter,
    "PandasColumns": PandasColumns,
    "PandasCreate": PandasCreate,
    "PandasCreateWithIndex": PandasCreateWithIndex,
    "PandasHead": PandasHead,
    "PandasIndex": PandasIndex,
    "PandasJoin": PandasJoin,
    "PandasLoadCSV": PandasLoadCSV,
    "PandasLoadCSVWithIndex": PandasLoadCSVWithIndex,
    "PandasLocCellStr": PandasLocCellStr,
    "PandasSaveCSV": PandasSaveCSV,
    "PandasSelectColumns": PandasSelectColumns,
    "PandasSelectRows": PandasSelectRows,
    "PandasShowDataFrame": PandasShowDataFrame,
    "PandasShowText": PandasShowText,
    "PandasSort": PandasSort,
    "PandasSummary": PandasSummary,
    "PandasToString": PandasToString,
}
"""
NODE_CLASS_MAPPINGS (Dict[str, Type[T]]):
    A dictionary mapping node names to their corresponding class implementations.
"""

NODE_DISPLAY_NAME_MAPPINGS: Dict[str, str] = {
    "MPLBar": "MPL Bar Chart",
    "MPLLine": "MPL Line Plot",
    "MPLScatter": "MPL Scatter Plot",
    "PandasColumns": "Pandas Columns",
    "PandasCreate": "Pandas Create",
    "PandasCreateWithIndex": "Pandas Create with Index",
    "PandasHead": "Pandas Head",
    "PandasIndex": "Pandas Index",
    "PandasJoin": "Pandas Join",
    "PandasLoadCSV": "Pandas Load CSV",
    "PandasLoadCSVWithIndex": "Pandas Load CSV with Index",
    "PandasLocCellStr": "Pandas Loc Cell Str",
    "PandasSaveCSV": "Pandas Save CSV",
    "PandasSelectColumns": "Pandas Select Columns",
    "PandasSelectRows": "Pandas Select Rows",
    "PandasShowDataFrame": "Pandas Show DataFrame",
    "PandasShowText": "Pandas Show Text",
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
