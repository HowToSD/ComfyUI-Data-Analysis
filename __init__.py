from typing import Dict, Type, TypeVar
from .modules.cda.cda_float_create import CDAFloatCreate
from .modules.cda.cda_int_create import CDAIntCreate
from .modules.cda.cda_json_create import CDAJSONCreate
from .modules.cda.cda_show_float import CDAShowFloat
from .modules.cda.cda_show_int import CDAShowInt
from .modules.cda.cda_string_create import CDAStringCreate
from .modules.cda.cda_text_create import CDATextCreate
from .modules.matplotlib.mpl_bar import MPLBar
from .modules.matplotlib.mpl_line import MPLLine
from .modules.matplotlib.mpl_scatter import MPLScatter
from .modules.pandas_wrapper.pandas_add import PandasAdd
from .modules.pandas_wrapper.pandas_add_series import PandasAddSeries
from .modules.pandas_wrapper.pandas_as_float import PandasAsFloat
from .modules.pandas_wrapper.pandas_as_int import PandasAsInt
from .modules.pandas_wrapper.pandas_as_string import PandasAsString
from .modules.pandas_wrapper.pandas_columns import PandasColumns
from .modules.pandas_wrapper.pandas_count import PandasCount
from .modules.pandas_wrapper.pandas_create import PandasCreate
from .modules.pandas_wrapper.pandas_create_with_index import PandasCreateWithIndex
from .modules.pandas_wrapper.pandas_div import PandasDiv
from .modules.pandas_wrapper.pandas_div_series import PandasDivSeries
from .modules.pandas_wrapper.pandas_dropna import PandasDropNA
from .modules.pandas_wrapper.pandas_exp import PandasExp
from .modules.pandas_wrapper.pandas_log import PandasLog
from .modules.pandas_wrapper.pandas_sin import PandasSin
from .modules.pandas_wrapper.pandas_cos import PandasCos
from .modules.pandas_wrapper.pandas_tan import PandasTan
from .modules.pandas_wrapper.pandas_group_by import PandasGroupBy
from .modules.pandas_wrapper.pandas_head import PandasHead
from .modules.pandas_wrapper.pandas_horizontal_concat import PandasHorizontalConcat
from .modules.pandas_wrapper.pandas_horizontal_split import PandasHorizontalSplit
from .modules.pandas_wrapper.pandas_iloc_row_series import PandasIlocRowSeries
from .modules.pandas_wrapper.pandas_iloc_rows_dataframe import PandasIlocRowsDataFrame
from .modules.pandas_wrapper.pandas_index import PandasIndex
from .modules.pandas_wrapper.pandas_index_to_string import PandasIndexToString
from .modules.pandas_wrapper.pandas_isna import PandasIsNA
from .modules.pandas_wrapper.pandas_join import PandasJoin
from .modules.pandas_wrapper.pandas_load_csv import PandasLoadCSV
from .modules.pandas_wrapper.pandas_load_csv_with_encoding import PandasLoadCSVWithEncoding
from .modules.pandas_wrapper.pandas_load_csv_with_index import PandasLoadCSVWithIndex
from .modules.pandas_wrapper.pandas_load_html import PandasLoadHTML
from .modules.pandas_wrapper.pandas_load_json import PandasLoadJSON
from .modules.pandas_wrapper.pandas_loc_cell_str import PandasLocCellStr
from .modules.pandas_wrapper.pandas_loc_row_series import PandasLocRowSeries
from .modules.pandas_wrapper.pandas_max import PandasMax
from .modules.pandas_wrapper.pandas_mean import PandasMean
from .modules.pandas_wrapper.pandas_median import PandasMedian
from .modules.pandas_wrapper.pandas_min import PandasMin
from .modules.pandas_wrapper.pandas_mode import PandasMode
from .modules.pandas_wrapper.pandas_mul import PandasMul
from .modules.pandas_wrapper.pandas_mul_series import PandasMulSeries
from .modules.pandas_wrapper.pandas_pow import PandasPow
from .modules.pandas_wrapper.pandas_pow_series import PandasPowSeries
from .modules.pandas_wrapper.pandas_rename import PandasRename
from .modules.pandas_wrapper.pandas_replace import PandasReplace
from .modules.pandas_wrapper.pandas_save_csv import PandasSaveCSV
from .modules.pandas_wrapper.pandas_save_json import PandasSaveJSON
from .modules.pandas_wrapper.pandas_select_columns import PandasSelectColumns
from .modules.pandas_wrapper.pandas_select_rows import PandasSelectRows
from .modules.pandas_wrapper.pandas_series_to_string import PandasSeriesToString
from .modules.pandas_wrapper.pandas_series_to_dataframe import PandasSeriesToDataFrame
from .modules.pandas_wrapper.pandas_show_dataframe import PandasShowDataFrame
from .modules.pandas_wrapper.pandas_show_index import PandasShowIndex
from .modules.pandas_wrapper.pandas_show_series import PandasShowSeries
from .modules.pandas_wrapper.pandas_show_text import PandasShowText
from .modules.pandas_wrapper.pandas_sort import PandasSort
from .modules.pandas_wrapper.pandas_std import PandasStd
from .modules.pandas_wrapper.pandas_sub import PandasSub
from .modules.pandas_wrapper.pandas_sub_series import PandasSubSeries
from .modules.pandas_wrapper.pandas_sum import PandasSum
from .modules.pandas_wrapper.pandas_summary import PandasSummary
from .modules.pandas_wrapper.pandas_to_string import PandasToString
from .modules.pandas_wrapper.pandas_transpose import PandasTranspose
from .modules.pandas_wrapper.pandas_var import PandasVar
from .modules.pandas_wrapper.pandas_vertical_concat import PandasVerticalConcat
from .modules.pandas_wrapper.pandas_vertical_split import PandasVerticalSplit

T = TypeVar("T")

NODE_CLASS_MAPPINGS: Dict[str, Type[T]] = {
    "CDAFloatCreate": CDAFloatCreate,
    "CDAIntCreate": CDAIntCreate,
    "CDAJSONCreate": CDAJSONCreate,
    "CDAShowFloat": CDAShowFloat,
    "CDAShowInt": CDAShowInt,
    "CDAStringCreate": CDAStringCreate,
    "CDATextCreate": CDATextCreate,
    "MPLBar": MPLBar,
    "MPLLine": MPLLine,
    "MPLScatter": MPLScatter,
    "PandasAdd": PandasAdd,
    "PandasAddSeries": PandasAddSeries,
    "PandasAsFloat": PandasAsFloat,
    "PandasAsInt": PandasAsInt,
    "PandasAsString": PandasAsString,
    "PandasColumns": PandasColumns,
    "PandasCount": PandasCount,
    "PandasCreate": PandasCreate,
    "PandasCreateWithIndex": PandasCreateWithIndex,
    "PandasDiv": PandasDiv,
    "PandasDivSeries": PandasDivSeries,
    "PandasDropNA": PandasDropNA,
    "PandasExp": PandasExp,
    "PandasLog": PandasLog,
    "PandasSin": PandasSin,
    "PandasCos": PandasCos,
    "PandasTan": PandasTan,
    "PandasGroupBy": PandasGroupBy,
    "PandasHead": PandasHead,
    "PandasHorizontalConcat": PandasHorizontalConcat,
    "PandasHorizontalSplit": PandasHorizontalSplit,
    "PandasIlocRowSeries": PandasIlocRowSeries,
    "PandasIlocRowsDataFrame": PandasIlocRowsDataFrame,
    "PandasIndex": PandasIndex,
    "PandasIndexToString": PandasIndexToString,
    "PandasIsNA": PandasIsNA,
    "PandasJoin": PandasJoin,
    "PandasLoadCSV": PandasLoadCSV,
    "PandasLoadCSVWithEncoding": PandasLoadCSVWithEncoding,
    "PandasLoadCSVWithIndex": PandasLoadCSVWithIndex,
    "PandasLoadHTML": PandasLoadHTML,
    "PandasLoadJSON": PandasLoadJSON,
    "PandasLocCellStr": PandasLocCellStr,
    "PandasLocRowSeries": PandasLocRowSeries,
    "PandasMax": PandasMax,
    "PandasMean": PandasMean,
    "PandasMedian": PandasMedian,
    "PandasMin": PandasMin,
    "PandasMode": PandasMode,
    "PandasMul": PandasMul,
    "PandasMulSeries": PandasMulSeries,
    "PandasRename": PandasRename,
    "PandasReplace": PandasReplace,
    "PandasPow": PandasPow,
    "PandasPowSeries": PandasPowSeries,
    "PandasSaveCSV": PandasSaveCSV,
    "PandasSaveJSON": PandasSaveJSON,
    "PandasSelectColumns": PandasSelectColumns,
    "PandasSelectRows": PandasSelectRows,
    "PandasSeriesToString": PandasSeriesToString,
    "PandasSeriesToDataFrame": PandasSeriesToDataFrame,
    "PandasShowDataFrame": PandasShowDataFrame,
    "PandasShowIndex": PandasShowIndex,
    "PandasShowSeries": PandasShowSeries,
    "PandasShowText": PandasShowText,
    "PandasSort": PandasSort,
    "PandasStd": PandasStd,
    "PandasSub": PandasSub,
    "PandasSubSeries": PandasSubSeries,
    "PandasSum": PandasSum,
    "PandasSummary": PandasSummary,
    "PandasToString": PandasToString,
    "PandasTranspose": PandasTranspose,
    "PandasVar": PandasVar,
    "PandasVerticalConcat": PandasVerticalConcat,
    "PandasVerticalSplit": PandasVerticalSplit
}
"""
NODE_CLASS_MAPPINGS (Dict[str, Type[T]]):
    A dictionary mapping node names to their corresponding class implementations.
"""

NODE_DISPLAY_NAME_MAPPINGS: Dict[str, str] = {
    "CDAFloatCreate": "CDA Float Create",
    "CDAIntCreate": "CDA Int Create",
    "CDAJSONCreate": "CDA JSON Create",
    "CDAShowFloat": "CDA Show Float",
    "CDAShowInt": "CDA Show Int",
    "CDAStringCreate": "CDA String Create",
    "CDATextCreate": "CDA Text Create",
    "MPLBar": "MPL Bar Chart",
    "MPLLine": "MPL Line Plot",
    "MPLScatter": "MPL Scatter Plot",
    "PandasAdd": "Pandas Add",
    "PandasAddSeries": "Pandas Add Series",
    "PandasAsFloat": "Pandas As Float",
    "PandasAsInt": "Pandas As Int",
    "PandasAsString": "Pandas As String",
    "PandasColumns": "Pandas Columns",
    "PandasCount": "Pandas Count",
    "PandasCreate": "Pandas Create",
    "PandasCreateWithIndex": "Pandas Create With Index",
    "PandasDiv": "Pandas Div",
    "PandasDivSeries": "Pandas Div Series",
    "PandasDropNA": "Pandas Drop NA",
    "PandasExp": "Pandas Exp",
    "PandasLog": "Pandas Log",
    "PandasSin": "Pandas Sin",
    "PandasCos": "Pandas Cos",
    "PandasTan": "Pandas Tan",
    "PandasGroupBy": "Pandas Group By",
    "PandasHead": "Pandas Head",
    "PandasHorizontalConcat": "Pandas Horizontal Concat",
    "PandasHorizontalSplit": "Pandas Horizontal Split",
    "PandasIlocRowSeries": "Pandas Iloc Row Series",
    "PandasIlocRowsDataFrame": "Pandas Iloc Rows DataFrame",
    "PandasIndex": "Pandas Index",
    "PandasIndexToString": "Pandas Index To String",
    "PandasIsNA": "Pandas Is NA",
    "PandasJoin": "Pandas Join",
    "PandasLoadCSV": "Pandas Load CSV",
    "PandasLoadCSVWithEncoding": "Pandas Load CSV With Encoding",
    "PandasLoadCSVWithIndex": "Pandas Load CSV With Index",
    "PandasLoadHTML": "Pandas Load HTML",
    "PandasLoadJSON": "Pandas Load JSON",
    "PandasLocCellStr": "Pandas Loc Cell Str",
    "PandasLocRowSeries": "Pandas Loc Row Series",
    "PandasMax": "Pandas Max",
    "PandasMean": "Pandas Mean",
    "PandasMedian": "Pandas Median",
    "PandasMin": "Pandas Min",
    "PandasMode": "Pandas Mode",
    "PandasMul": "Pandas Mul",
    "PandasMulSeries": "Pandas Mul Series",
    "PandasPow": "Pandas Pow",
    "PandasPowSeries": "Pandas Pow Series",
    "PandasRename": "Pandas Rename",
    "PandasReplace": "Pandas Replace",
    "PandasSaveCSV": "Pandas Save CSV",
    "PandasSaveJSON": "Pandas Save JSON",
    "PandasSelectColumns": "Pandas Select Columns",
    "PandasSelectRows": "Pandas Select Rows",
    "PandasSeriesToString": "Pandas Series To String",
    "PandasSeriesToDataFrame": "Pandas Series To DataFrame",
    "PandasShowDataFrame": "Pandas Show DataFrame",
    "PandasShowIndex": "Pandas Show Index",
    "PandasShowSeries": "Pandas Show Series",
    "PandasShowText": "Pandas Show Text",
    "PandasSort": "Pandas Sort",
    "PandasStd": "Pandas Std",
    "PandasSub": "Pandas Sub",
    "PandasSubSeries": "Pandas Sub Series",
    "PandasSum": "Pandas Sum",
    "PandasSummary": "Pandas Summary",
    "PandasToString": "Pandas To String",
    "PandasTranspose": "Pandas Transpose",
    "PandasVar": "Pandas Var",
    "PandasVerticalConcat": "Pandas Vertical Concat",
    "PandasVerticalSplit": "Pandas Vertical Split"
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
