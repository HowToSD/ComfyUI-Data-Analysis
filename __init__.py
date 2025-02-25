# This file is auto-generated. Do not edit manually.
from typing import Dict, Type, TypeVar
from .modules.cda.cda_float_create import CDAFloatCreate
from .modules.cda.cda_int_create import CDAIntCreate
from .modules.cda.cda_json_create import CDAJSONCreate
from .modules.cda.cda_show_float import CDAShowFloat
from .modules.cda.cda_show_int import CDAShowInt
from .modules.cda.cda_string_create import CDAStringCreate
from .modules.cda.cda_text_create import CDATextCreate
from .modules.cda.py_kv_float_create import PyKvFloatCreate
from .modules.cda.py_kv_int_create import PyKvIntCreate
from .modules.cda.py_kv_string_create import PyKvStringCreate
from .modules.matplotlib.mpl_bar import MPLBar
from .modules.matplotlib.mpl_line import MPLLine
from .modules.matplotlib.mpl_pie_chart import MPLPieChart
from .modules.matplotlib.mpl_scatter import MPLScatter
from .modules.numpy_wrapper.numpy_float_create import NumpyFloatCreate
from .modules.numpy_wrapper.numpy_int_create import NumpyIntCreate
from .modules.pandas_wrapper.pandas_add import PandasAdd
from .modules.pandas_wrapper.pandas_add_scalar_float import PandasAddScalarFloat
from .modules.pandas_wrapper.pandas_add_scalar_int import PandasAddScalarInt
from .modules.pandas_wrapper.pandas_add_series import PandasAddSeries
from .modules.pandas_wrapper.pandas_as_float import PandasAsFloat
from .modules.pandas_wrapper.pandas_as_int import PandasAsInt
from .modules.pandas_wrapper.pandas_as_string import PandasAsString
from .modules.pandas_wrapper.pandas_columns import PandasColumns
from .modules.pandas_wrapper.pandas_corr import PandasCorr
from .modules.pandas_wrapper.pandas_cos import PandasCos
from .modules.pandas_wrapper.pandas_count import PandasCount
from .modules.pandas_wrapper.pandas_cov import PandasCov
from .modules.pandas_wrapper.pandas_create import PandasCreate
from .modules.pandas_wrapper.pandas_create_from_dict import PandasCreateFromDict
from .modules.pandas_wrapper.pandas_create_from_multiple_dict import PandasCreateFromMultipleDict
from .modules.pandas_wrapper.pandas_create_from_numpy import PandasCreateFromNumpy
from .modules.pandas_wrapper.pandas_create_series_from_dict import PandasCreateSeriesFromDict
from .modules.pandas_wrapper.pandas_create_with_index import PandasCreateWithIndex
from .modules.pandas_wrapper.pandas_crosstab import PandasCrosstab
from .modules.pandas_wrapper.pandas_cummax import PandasCummax
from .modules.pandas_wrapper.pandas_cummin import PandasCummin
from .modules.pandas_wrapper.pandas_cumprod import PandasCumprod
from .modules.pandas_wrapper.pandas_cumsum import PandasCumsum
from .modules.pandas_wrapper.pandas_div import PandasDiv
from .modules.pandas_wrapper.pandas_div_scalar_float import PandasDivScalarFloat
from .modules.pandas_wrapper.pandas_div_scalar_int import PandasDivScalarInt
from .modules.pandas_wrapper.pandas_div_series import PandasDivSeries
from .modules.pandas_wrapper.pandas_drop_duplicates import PandasDropDuplicates
from .modules.pandas_wrapper.pandas_dropna import PandasDropNA
from .modules.pandas_wrapper.pandas_exp import PandasExp
from .modules.pandas_wrapper.pandas_fillna_scalar_float import PandasFillNAScalarFloat
from .modules.pandas_wrapper.pandas_fillna_scalar_int import PandasFillNAScalarInt
from .modules.pandas_wrapper.pandas_group_by import PandasGroupBy
from .modules.pandas_wrapper.pandas_head import PandasHead
from .modules.pandas_wrapper.pandas_horizontal_concat import PandasHorizontalConcat
from .modules.pandas_wrapper.pandas_horizontal_split import PandasHorizontalSplit
from .modules.pandas_wrapper.pandas_iloc_row_series import PandasIlocRowSeries
from .modules.pandas_wrapper.pandas_iloc_rows_dataframe import PandasIlocRowsDataFrame
from .modules.pandas_wrapper.pandas_iloc_rows_slice_dataframe import PandasIlocRowsSliceDataFrame
from .modules.pandas_wrapper.pandas_index import PandasIndex
from .modules.pandas_wrapper.pandas_index_to_string import PandasIndexToString
from .modules.pandas_wrapper.pandas_isna import PandasIsNA
from .modules.pandas_wrapper.pandas_join import PandasJoin
from .modules.pandas_wrapper.pandas_kurtosis import PandasKurtosis
from .modules.pandas_wrapper.pandas_load_csv import PandasLoadCSV
from .modules.pandas_wrapper.pandas_load_csv_with_encoding import PandasLoadCSVWithEncoding
from .modules.pandas_wrapper.pandas_load_csv_with_index import PandasLoadCSVWithIndex
from .modules.pandas_wrapper.pandas_load_html import PandasLoadHTML
from .modules.pandas_wrapper.pandas_load_json import PandasLoadJSON
from .modules.pandas_wrapper.pandas_loc_cell_str import PandasLocCellStr
from .modules.pandas_wrapper.pandas_loc_row_multiindex_dataframe import PandasLocRowMultiIndexDataFrame
from .modules.pandas_wrapper.pandas_loc_row_series import PandasLocRowSeries
from .modules.pandas_wrapper.pandas_log import PandasLog
from .modules.pandas_wrapper.pandas_max import PandasMax
from .modules.pandas_wrapper.pandas_mean import PandasMean
from .modules.pandas_wrapper.pandas_median import PandasMedian
from .modules.pandas_wrapper.pandas_melt import PandasMelt
from .modules.pandas_wrapper.pandas_min import PandasMin
from .modules.pandas_wrapper.pandas_mode import PandasMode
from .modules.pandas_wrapper.pandas_mul import PandasMul
from .modules.pandas_wrapper.pandas_mul_scalar_float import PandasMulScalarFloat
from .modules.pandas_wrapper.pandas_mul_scalar_int import PandasMulScalarInt
from .modules.pandas_wrapper.pandas_mul_series import PandasMulSeries
from .modules.pandas_wrapper.pandas_pivot import PandasPivot
from .modules.pandas_wrapper.pandas_pow import PandasPow
from .modules.pandas_wrapper.pandas_pow_scalar_float import PandasPowScalarFloat
from .modules.pandas_wrapper.pandas_pow_scalar_int import PandasPowScalarInt
from .modules.pandas_wrapper.pandas_pow_series import PandasPowSeries
from .modules.pandas_wrapper.pandas_rename import PandasRename
from .modules.pandas_wrapper.pandas_replace import PandasReplace
from .modules.pandas_wrapper.pandas_save_csv import PandasSaveCSV
from .modules.pandas_wrapper.pandas_save_json import PandasSaveJSON
from .modules.pandas_wrapper.pandas_select_columns import PandasSelectColumns
from .modules.pandas_wrapper.pandas_select_rows import PandasSelectRows
from .modules.pandas_wrapper.pandas_series_to_dataframe import PandasSeriesToDataFrame
from .modules.pandas_wrapper.pandas_series_to_string import PandasSeriesToString
from .modules.pandas_wrapper.pandas_set_index import PandasSetIndex
from .modules.pandas_wrapper.pandas_show_dataframe import PandasShowDataFrame
from .modules.pandas_wrapper.pandas_show_index import PandasShowIndex
from .modules.pandas_wrapper.pandas_show_series import PandasShowSeries
from .modules.pandas_wrapper.pandas_show_text import PandasShowText
from .modules.pandas_wrapper.pandas_sin import PandasSin
from .modules.pandas_wrapper.pandas_skew import PandasSkew
from .modules.pandas_wrapper.pandas_sort import PandasSort
from .modules.pandas_wrapper.pandas_std import PandasStd
from .modules.pandas_wrapper.pandas_strftime import PandasStrftime
from .modules.pandas_wrapper.pandas_sub import PandasSub
from .modules.pandas_wrapper.pandas_sub_scalar_float import PandasSubScalarFloat
from .modules.pandas_wrapper.pandas_sub_scalar_int import PandasSubScalarInt
from .modules.pandas_wrapper.pandas_sub_series import PandasSubSeries
from .modules.pandas_wrapper.pandas_sum import PandasSum
from .modules.pandas_wrapper.pandas_summary import PandasSummary
from .modules.pandas_wrapper.pandas_tan import PandasTan
from .modules.pandas_wrapper.pandas_to_datetime import PandasToDatetime
from .modules.pandas_wrapper.pandas_to_numpy import PandasToNumpy
from .modules.pandas_wrapper.pandas_to_string import PandasToString
from .modules.pandas_wrapper.pandas_transpose import PandasTranspose
from .modules.pandas_wrapper.pandas_value_counts import PandasValueCounts
from .modules.pandas_wrapper.pandas_var import PandasVar
from .modules.pandas_wrapper.pandas_vertical_concat import PandasVerticalConcat
from .modules.pandas_wrapper.pandas_vertical_split import PandasVerticalSplit
from .modules.pandas_wrapper.pandas_xs import PandasXs
from .modules.pytorch_wrapper.pt_flatten import PtFlatten
from .modules.pytorch_wrapper.pt_float_create import PtFloatCreate
from .modules.pytorch_wrapper.pt_from_image import PtFromImage
from .modules.pytorch_wrapper.pt_from_latent import PtFromLatent
from .modules.pytorch_wrapper.pt_from_numpy import PtFromNumpy
from .modules.pytorch_wrapper.pt_int_create import PtIntCreate
from .modules.pytorch_wrapper.pt_size import PtSize
from .modules.pytorch_wrapper.pt_size_create import PtSizeCreate
from .modules.pytorch_wrapper.pt_size_to_numpy import PtSizeToNumpy
from .modules.pytorch_wrapper.pt_size_to_string import PtSizeToString
from .modules.pytorch_wrapper.pt_to_image import PtToImage
from .modules.pytorch_wrapper.pt_to_latent import PtToLatent
from .modules.pytorch_wrapper.pt_to_numpy import PtToNumpy
from .modules.pytorch_wrapper.pt_to_rgb_tensors import PtToRgbTensors
from .modules.seaborn_wrapper.sns_bar import SNSBar
from .modules.seaborn_wrapper.sns_histogram import SNSHistogram
from .modules.seaborn_wrapper.sns_line import SNSLine
from .modules.seaborn_wrapper.sns_scatter import SNSScatter
T = TypeVar("T")


"""
NODE_CLASS_MAPPINGS (Dict[str, Type[T]]):
    A dictionary mapping node names to their corresponding class implementations.
"""

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
    "MPLPieChart": MPLPieChart,
    "MPLScatter": MPLScatter,
    "NumpyFloatCreate": NumpyFloatCreate,
    "NumpyIntCreate": NumpyIntCreate,
    "PandasAdd": PandasAdd,
    "PandasAddScalarFloat": PandasAddScalarFloat,
    "PandasAddScalarInt": PandasAddScalarInt,
    "PandasAddSeries": PandasAddSeries,
    "PandasAsFloat": PandasAsFloat,
    "PandasAsInt": PandasAsInt,
    "PandasAsString": PandasAsString,
    "PandasColumns": PandasColumns,
    "PandasCorr": PandasCorr,
    "PandasCos": PandasCos,
    "PandasCount": PandasCount,
    "PandasCov": PandasCov,
    "PandasCreate": PandasCreate,
    "PandasCreateFromDict": PandasCreateFromDict,
    "PandasCreateFromMultipleDict": PandasCreateFromMultipleDict,
    "PandasCreateFromNumpy": PandasCreateFromNumpy,
    "PandasCreateSeriesFromDict": PandasCreateSeriesFromDict,
    "PandasCreateWithIndex": PandasCreateWithIndex,
    "PandasCrosstab": PandasCrosstab,
    "PandasCummax": PandasCummax,
    "PandasCummin": PandasCummin,
    "PandasCumprod": PandasCumprod,
    "PandasCumsum": PandasCumsum,
    "PandasDiv": PandasDiv,
    "PandasDivScalarFloat": PandasDivScalarFloat,
    "PandasDivScalarInt": PandasDivScalarInt,
    "PandasDivSeries": PandasDivSeries,
    "PandasDropDuplicates": PandasDropDuplicates,
    "PandasDropNA": PandasDropNA,
    "PandasExp": PandasExp,
    "PandasFillNAScalarFloat": PandasFillNAScalarFloat,
    "PandasFillNAScalarInt": PandasFillNAScalarInt,
    "PandasGroupBy": PandasGroupBy,
    "PandasHead": PandasHead,
    "PandasHorizontalConcat": PandasHorizontalConcat,
    "PandasHorizontalSplit": PandasHorizontalSplit,
    "PandasIlocRowSeries": PandasIlocRowSeries,
    "PandasIlocRowsDataFrame": PandasIlocRowsDataFrame,
    "PandasIlocRowsSliceDataFrame": PandasIlocRowsSliceDataFrame,
    "PandasIndex": PandasIndex,
    "PandasIndexToString": PandasIndexToString,
    "PandasIsNA": PandasIsNA,
    "PandasJoin": PandasJoin,
    "PandasKurtosis": PandasKurtosis,
    "PandasLoadCSV": PandasLoadCSV,
    "PandasLoadCSVWithEncoding": PandasLoadCSVWithEncoding,
    "PandasLoadCSVWithIndex": PandasLoadCSVWithIndex,
    "PandasLoadHTML": PandasLoadHTML,
    "PandasLoadJSON": PandasLoadJSON,
    "PandasLocCellStr": PandasLocCellStr,
    "PandasLocRowMultiIndexDataFrame": PandasLocRowMultiIndexDataFrame,
    "PandasLocRowSeries": PandasLocRowSeries,
    "PandasLog": PandasLog,
    "PandasMax": PandasMax,
    "PandasMean": PandasMean,
    "PandasMedian": PandasMedian,
    "PandasMelt": PandasMelt,
    "PandasMin": PandasMin,
    "PandasMode": PandasMode,
    "PandasMul": PandasMul,
    "PandasMulScalarFloat": PandasMulScalarFloat,
    "PandasMulScalarInt": PandasMulScalarInt,
    "PandasMulSeries": PandasMulSeries,
    "PandasPivot": PandasPivot,
    "PandasPow": PandasPow,
    "PandasPowScalarFloat": PandasPowScalarFloat,
    "PandasPowScalarInt": PandasPowScalarInt,
    "PandasPowSeries": PandasPowSeries,
    "PandasRename": PandasRename,
    "PandasReplace": PandasReplace,
    "PandasSaveCSV": PandasSaveCSV,
    "PandasSaveJSON": PandasSaveJSON,
    "PandasSelectColumns": PandasSelectColumns,
    "PandasSelectRows": PandasSelectRows,
    "PandasSeriesToDataFrame": PandasSeriesToDataFrame,
    "PandasSeriesToString": PandasSeriesToString,
    "PandasSetIndex": PandasSetIndex,
    "PandasShowDataFrame": PandasShowDataFrame,
    "PandasShowIndex": PandasShowIndex,
    "PandasShowSeries": PandasShowSeries,
    "PandasShowText": PandasShowText,
    "PandasSin": PandasSin,
    "PandasSkew": PandasSkew,
    "PandasSort": PandasSort,
    "PandasStd": PandasStd,
    "PandasStrftime": PandasStrftime,
    "PandasSub": PandasSub,
    "PandasSubScalarFloat": PandasSubScalarFloat,
    "PandasSubScalarInt": PandasSubScalarInt,
    "PandasSubSeries": PandasSubSeries,
    "PandasSum": PandasSum,
    "PandasSummary": PandasSummary,
    "PandasTan": PandasTan,
    "PandasToDatetime": PandasToDatetime,
    "PandasToNumpy": PandasToNumpy,
    "PandasToString": PandasToString,
    "PandasTranspose": PandasTranspose,
    "PandasValueCounts": PandasValueCounts,
    "PandasVar": PandasVar,
    "PandasVerticalConcat": PandasVerticalConcat,
    "PandasVerticalSplit": PandasVerticalSplit,
    "PandasXs": PandasXs,
    "PtFlatten": PtFlatten,
    "PtFloatCreate": PtFloatCreate,
    "PtFromImage": PtFromImage,
    "PtFromLatent": PtFromLatent,
    "PtFromNumpy": PtFromNumpy,
    "PtIntCreate": PtIntCreate,
    "PtSize": PtSize,
    "PtSizeCreate": PtSizeCreate,
    "PtSizeToNumpy": PtSizeToNumpy,
    "PtSizeToString": PtSizeToString,
    "PtToImage": PtToImage,
    "PtToLatent": PtToLatent,
    "PtToNumpy": PtToNumpy,
    "PtToRgbTensors": PtToRgbTensors,
    "PyKvFloatCreate": PyKvFloatCreate,
    "PyKvIntCreate": PyKvIntCreate,
    "PyKvStringCreate": PyKvStringCreate,
    "SNSBar": SNSBar,
    "SNSHistogram": SNSHistogram,
    "SNSLine": SNSLine,
    "SNSScatter": SNSScatter,
}


"""
NODE_DISPLAY_NAME_MAPPINGS (Dict[str, str]):
    A dictionary mapping node names to user-friendly display names.
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
    "MPLPieChart": "MPL Pie Chart",
    "MPLScatter": "MPL Scatter Plot",
    "NumpyFloatCreate": "Numpy Float Create",
    "NumpyIntCreate": "Numpy Int Create",
    "PandasAdd": "Pandas Add",
    "PandasAddScalarFloat": "Pandas Add Scalar Float",
    "PandasAddScalarInt": "Pandas Add Scalar Int",
    "PandasAddSeries": "Pandas Add Series",
    "PandasAsFloat": "Pandas As Float",
    "PandasAsInt": "Pandas As Int",
    "PandasAsString": "Pandas As String",
    "PandasColumns": "Pandas Columns",
    "PandasCorr": "Pandas Corr",
    "PandasCos": "Pandas Cos",
    "PandasCount": "Pandas Count",
    "PandasCov": "Pandas Cov",
    "PandasCreate": "Pandas Create",
    "PandasCreateFromDict": "Pandas Create From Dict",
    "PandasCreateFromMultipleDict": "Pandas Create From Multiple Dict",
    "PandasCreateFromNumpy": "Pandas Create From Numpy",
    "PandasCreateSeriesFromDict": "Pandas Create Series From Dict",
    "PandasCreateWithIndex": "Pandas Create With Index",
    "PandasCrosstab": "Pandas Crosstab",
    "PandasCummax": "Pandas Cummax",
    "PandasCummin": "Pandas Cummin",
    "PandasCumprod": "Pandas Cumprod",
    "PandasCumsum": "Pandas Cumsum",
    "PandasDiv": "Pandas Div",
    "PandasDivScalarFloat": "Pandas Div Scalar Float",
    "PandasDivScalarInt": "Pandas Div Scalar Int",
    "PandasDivSeries": "Pandas Div Series",
    "PandasDropDuplicates": "Pandas Drop Duplicates",
    "PandasDropNA": "Pandas Drop NA",
    "PandasExp": "Pandas Exp",
    "PandasFillNAScalarFloat": "Pandas Fill NA Scalar Float",
    "PandasFillNAScalarInt": "Pandas Fill NA Scalar Int",
    "PandasGroupBy": "Pandas Group By",
    "PandasHead": "Pandas Head",
    "PandasHorizontalConcat": "Pandas Horizontal Concat",
    "PandasHorizontalSplit": "Pandas Horizontal Split",
    "PandasIlocRowSeries": "Pandas Iloc Row Series",
    "PandasIlocRowsDataFrame": "Pandas Iloc Rows DataFrame",
    "PandasIlocRowsSliceDataFrame": "Pandas Iloc Rows Slice DataFrame",
    "PandasIndex": "Pandas Index",
    "PandasIndexToString": "Pandas Index To String",
    "PandasIsNA": "Pandas Is NA",
    "PandasJoin": "Pandas Join",
    "PandasKurtosis": "Pandas Kurtosis",
    "PandasLoadCSV": "Pandas Load CSV",
    "PandasLoadCSVWithEncoding": "Pandas Load CSV With Encoding",
    "PandasLoadCSVWithIndex": "Pandas Load CSV With Index",
    "PandasLoadHTML": "Pandas Load HTML",
    "PandasLoadJSON": "Pandas Load JSON",
    "PandasLocCellStr": "Pandas Loc Cell Str",
    "PandasLocRowMultiIndexDataFrame": "Pandas Loc Row MultiIndex DataFrame",
    "PandasLocRowSeries": "Pandas Loc Row Series",
    "PandasLog": "Pandas Log",
    "PandasMax": "Pandas Max",
    "PandasMean": "Pandas Mean",
    "PandasMedian": "Pandas Median",
    "PandasMelt": "Pandas Melt",
    "PandasMin": "Pandas Min",
    "PandasMode": "Pandas Mode",
    "PandasMul": "Pandas Mul",
    "PandasMulScalarFloat": "Pandas Mul Scalar Float",
    "PandasMulScalarInt": "Pandas Mul Scalar Int",
    "PandasMulSeries": "Pandas Mul Series",
    "PandasPivot": "Pandas Pivot",
    "PandasPow": "Pandas Pow",
    "PandasPowScalarFloat": "Pandas Pow Scalar Float",
    "PandasPowScalarInt": "Pandas Pow Scalar Int",
    "PandasPowSeries": "Pandas Pow Series",
    "PandasRename": "Pandas Rename",
    "PandasReplace": "Pandas Replace",
    "PandasSaveCSV": "Pandas Save CSV",
    "PandasSaveJSON": "Pandas Save JSON",
    "PandasSelectColumns": "Pandas Select Columns",
    "PandasSelectRows": "Pandas Select Rows",
    "PandasSeriesToDataFrame": "Pandas Series To DataFrame",
    "PandasSeriesToString": "Pandas Series To String",
    "PandasSetIndex": "Pandas Set Index",
    "PandasShowDataFrame": "Pandas Show DataFrame",
    "PandasShowIndex": "Pandas Show Index",
    "PandasShowSeries": "Pandas Show Series",
    "PandasShowText": "Pandas Show Text",
    "PandasSin": "Pandas Sin",
    "PandasSkew": "Pandas Skew",
    "PandasSort": "Pandas Sort",
    "PandasStd": "Pandas Std",
    "PandasStrftime": "Pandas Strftime",
    "PandasSub": "Pandas Sub",
    "PandasSubScalarFloat": "Pandas Sub Scalar Float",
    "PandasSubScalarInt": "Pandas Sub Scalar Int",
    "PandasSubSeries": "Pandas Sub Series",
    "PandasSum": "Pandas Sum",
    "PandasSummary": "Pandas Summary",
    "PandasTan": "Pandas Tan",
    "PandasToDatetime": "Pandas To Datetime",
    "PandasToNumpy": "Pandas To Numpy",
    "PandasToString": "Pandas To String",
    "PandasTranspose": "Pandas Transpose",
    "PandasValueCounts": "Pandas Value Counts",
    "PandasVar": "Pandas Var",
    "PandasVerticalConcat": "Pandas Vertical Concat",
    "PandasVerticalSplit": "Pandas Vertical Split",
    "PandasXs": "Pandas Xs",
    "PtFlatten": "Pt Flatten",
    "PtFloatCreate": "Pt Float Create",
    "PtFromImage": "Pt From Image",
    "PtFromLatent": "Pt From Latent",
    "PtFromNumpy": "Pt From Numpy",
    "PtIntCreate": "Pt Int Create",
    "PtSize": "Pt Size",
    "PtSizeCreate": "Pt Size Create",
    "PtSizeToNumpy": "Pt Size To Numpy",
    "PtSizeToString": "Pt Size To String",
    "PtToImage": "Pt To Image",
    "PtToLatent": "Pt To Latent",
    "PtToNumpy": "Pt To Numpy",
    "PtToRgbTensors": "Pt To Rgb Tensors",
    "PyKvFloatCreate": "Py Kv Float Create",
    "PyKvIntCreate": "Py Kv Int Create",
    "PyKvStringCreate": "Py Kv String Create",
    "SNSBar": "SNS Bar Chart",
    "SNSHistogram": "SNS Histogram",
    "SNSLine": "SNS Line Plot",
    "SNSScatter": "SNS Scatter Plot",
}


"""
Below two lines were taken from:
https://github.com/pythongosssss/ComfyUI-Custom-Scripts/blob/main/__init__.py
See credit/credit.md for the full license.
"""

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
