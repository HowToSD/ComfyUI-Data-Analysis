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
from .modules.numpy_wrapper.numpy_show import NumpyShow
from .modules.numpy_wrapper.numpy_squeeze import NumpySqueeze
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
from .modules.pandas_wrapper.pandas_create_from_tensor import PandasCreateFromTensor
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
from .modules.pandas_wrapper.pandas_feature_split_to_numpy import PandasFeatureSplitToNumpy
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
from .modules.pandas_wrapper.pandas_load_excel import PandasLoadExcel
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
from .modules.pandas_wrapper.pandas_rename_advanced import PandasRenameAdvanced
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
from .modules.pytorch_wrapper.pt_abs import PtAbs
from .modules.pytorch_wrapper.pt_acos import PtAcos
from .modules.pytorch_wrapper.pt_add import PtAdd
from .modules.pytorch_wrapper.pt_arange import PtArange
from .modules.pytorch_wrapper.pt_argmax import PtArgmax
from .modules.pytorch_wrapper.pt_argmin import PtArgmin
from .modules.pytorch_wrapper.pt_asin import PtAsin
from .modules.pytorch_wrapper.pt_atan import PtAtan
from .modules.pytorch_wrapper.pt_bitwise_and import PtBitwiseAnd
from .modules.pytorch_wrapper.pt_bitwise_left_shift import PtBitwiseLeftShift
from .modules.pytorch_wrapper.pt_bitwise_not import PtBitwiseNot
from .modules.pytorch_wrapper.pt_bitwise_or import PtBitwiseOr
from .modules.pytorch_wrapper.pt_bitwise_right_shift import PtBitwiseRightShift
from .modules.pytorch_wrapper.pt_bitwise_xor import PtBitwiseXor
from .modules.pytorch_wrapper.pt_bmm import PtBmm
from .modules.pytorch_wrapper.pt_bool_create import PtBoolCreate
from .modules.pytorch_wrapper.pt_cos import PtCos
from .modules.pytorch_wrapper.pt_cosh import PtCosh
from .modules.pytorch_wrapper.pt_data_loader import PtDataLoader
from .modules.pytorch_wrapper.pt_div import PtDiv
from .modules.pytorch_wrapper.pt_einsum import PtEinsum
from .modules.pytorch_wrapper.pt_eq import PtEq
from .modules.pytorch_wrapper.pt_evaluate_classification_model import PtEvaluateClassificationModel
from .modules.pytorch_wrapper.pt_exp import PtExp
from .modules.pytorch_wrapper.pt_flatten import PtFlatten
from .modules.pytorch_wrapper.pt_float_create import PtFloatCreate
from .modules.pytorch_wrapper.pt_floor_divide import PtFloorDiv
from .modules.pytorch_wrapper.pt_from_image import PtFromImage
from .modules.pytorch_wrapper.pt_from_latent import PtFromLatent
from .modules.pytorch_wrapper.pt_from_numpy import PtFromNumpy
from .modules.pytorch_wrapper.pt_full import PtFull
from .modules.pytorch_wrapper.pt_gather import PtGather
from .modules.pytorch_wrapper.pt_ge import PtGe
from .modules.pytorch_wrapper.pt_gt import PtGt
from .modules.pytorch_wrapper.pt_index_select import PtIndexSelect
from .modules.pytorch_wrapper.pt_int_create import PtIntCreate
from .modules.pytorch_wrapper.pt_le import PtLe
from .modules.pytorch_wrapper.pt_linspace import PtLinspace
from .modules.pytorch_wrapper.pt_load_model import PtLoadModel
from .modules.pytorch_wrapper.pt_log import PtLog
from .modules.pytorch_wrapper.pt_logical_and import PtLogicalAnd
from .modules.pytorch_wrapper.pt_logical_not import PtLogicalNot
from .modules.pytorch_wrapper.pt_logical_or import PtLogicalOr
from .modules.pytorch_wrapper.pt_logical_xor import PtLogicalXor
from .modules.pytorch_wrapper.pt_lt import PtLt
from .modules.pytorch_wrapper.pt_masked_select import PtMaskedSelect
from .modules.pytorch_wrapper.pt_matmul import PtMatMul
from .modules.pytorch_wrapper.pt_max import PtMax
from .modules.pytorch_wrapper.pt_mean import PtMean
from .modules.pytorch_wrapper.pt_median import PtMedian
from .modules.pytorch_wrapper.pt_min import PtMin
from .modules.pytorch_wrapper.pt_mm import PtMm
from .modules.pytorch_wrapper.pt_mul import PtMul
from .modules.pytorch_wrapper.pt_ne import PtNe
from .modules.pytorch_wrapper.pt_neg import PtNeg
from .modules.pytorch_wrapper.pt_ones import PtOnes
from .modules.pytorch_wrapper.pt_permute import PtPermute
from .modules.pytorch_wrapper.pt_pow import PtPow
from .modules.pytorch_wrapper.pt_prod import PtProd
from .modules.pytorch_wrapper.pt_rand import PtRand
from .modules.pytorch_wrapper.pt_rand_int import PtRandInt
from .modules.pytorch_wrapper.pt_randn import PtRandn
from .modules.pytorch_wrapper.pt_remainder import PtRemainder
from .modules.pytorch_wrapper.pt_reshape import PtReshape
from .modules.pytorch_wrapper.pt_save_model import PtSaveModel
from .modules.pytorch_wrapper.pt_scatter import PtScatter
from .modules.pytorch_wrapper.pt_show_size import PtShowSize
from .modules.pytorch_wrapper.pt_show_text import PtShowText
from .modules.pytorch_wrapper.pt_sin import PtSin
from .modules.pytorch_wrapper.pt_sinh import PtSinh
from .modules.pytorch_wrapper.pt_size import PtSize
from .modules.pytorch_wrapper.pt_size_create import PtSizeCreate
from .modules.pytorch_wrapper.pt_size_to_numpy import PtSizeToNumpy
from .modules.pytorch_wrapper.pt_size_to_string import PtSizeToString
from .modules.pytorch_wrapper.pt_sqrt import PtSqrt
from .modules.pytorch_wrapper.pt_squeeze import PtSqueeze
from .modules.pytorch_wrapper.pt_std import PtStd
from .modules.pytorch_wrapper.pt_sub import PtSub
from .modules.pytorch_wrapper.pt_sum import PtSum
from .modules.pytorch_wrapper.pt_tan import PtTan
from .modules.pytorch_wrapper.pt_tanh import PtTanh
from .modules.pytorch_wrapper.pt_to_image import PtToImage
from .modules.pytorch_wrapper.pt_to_latent import PtToLatent
from .modules.pytorch_wrapper.pt_to_numpy import PtToNumpy
from .modules.pytorch_wrapper.pt_to_rgb_tensors import PtToRgbTensors
from .modules.pytorch_wrapper.pt_train_classification_model import PtTrainClassificationModel
from .modules.pytorch_wrapper.pt_unsqueeze import PtUnsqueeze
from .modules.pytorch_wrapper.pt_var import PtVar
from .modules.pytorch_wrapper.pt_view import PtView
from .modules.pytorch_wrapper.pt_where import PtWhere
from .modules.pytorch_wrapper.pt_zeros import PtZeros
from .modules.pytorch_wrapper.ptn_conv_model import PtnConvModel
from .modules.pytorch_wrapper.ptn_linear_model import PtnLinearModel
from .modules.pytorch_wrapper.pto_adam import PtoAdam
from .modules.pytorch_wrapper.ptv_dataset import PtvDataset
from .modules.pytorch_wrapper.ptv_dataset_loader import PtvDatasetLoader
from .modules.pytorch_wrapper.ptv_transforms_to_tensor import PtvTransformsToTensor
from .modules.seaborn_wrapper.sns_bar import SNSBar
from .modules.seaborn_wrapper.sns_boxplot import SNSBoxplot
from .modules.seaborn_wrapper.sns_heatmap import SNSHeatmap
from .modules.seaborn_wrapper.sns_histogram import SNSHistogram
from .modules.seaborn_wrapper.sns_line import SNSLine
from .modules.seaborn_wrapper.sns_pairplot import SNSPairplot
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
    "NumpyShow": NumpyShow,
    "NumpySqueeze": NumpySqueeze,
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
    "PandasCreateFromTensor": PandasCreateFromTensor,
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
    "PandasFeatureSplitToNumpy": PandasFeatureSplitToNumpy,
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
    "PandasLoadExcel": PandasLoadExcel,
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
    "PandasRenameAdvanced": PandasRenameAdvanced,
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
    "PtAbs": PtAbs,
    "PtAcos": PtAcos,
    "PtAdd": PtAdd,
    "PtArange": PtArange,
    "PtArgmax": PtArgmax,
    "PtArgmin": PtArgmin,
    "PtAsin": PtAsin,
    "PtAtan": PtAtan,
    "PtBitwiseAnd": PtBitwiseAnd,
    "PtBitwiseLeftShift": PtBitwiseLeftShift,
    "PtBitwiseNot": PtBitwiseNot,
    "PtBitwiseOr": PtBitwiseOr,
    "PtBitwiseRightShift": PtBitwiseRightShift,
    "PtBitwiseXor": PtBitwiseXor,
    "PtBmm": PtBmm,
    "PtBoolCreate": PtBoolCreate,
    "PtCos": PtCos,
    "PtCosh": PtCosh,
    "PtDataLoader": PtDataLoader,
    "PtDiv": PtDiv,
    "PtEinsum": PtEinsum,
    "PtEq": PtEq,
    "PtEvaluateClassificationModel": PtEvaluateClassificationModel,
    "PtExp": PtExp,
    "PtFlatten": PtFlatten,
    "PtFloatCreate": PtFloatCreate,
    "PtFloorDiv": PtFloorDiv,
    "PtFromImage": PtFromImage,
    "PtFromLatent": PtFromLatent,
    "PtFromNumpy": PtFromNumpy,
    "PtFull": PtFull,
    "PtGather": PtGather,
    "PtGe": PtGe,
    "PtGt": PtGt,
    "PtIndexSelect": PtIndexSelect,
    "PtIntCreate": PtIntCreate,
    "PtLe": PtLe,
    "PtLinspace": PtLinspace,
    "PtLoadModel": PtLoadModel,
    "PtLog": PtLog,
    "PtLogicalAnd": PtLogicalAnd,
    "PtLogicalNot": PtLogicalNot,
    "PtLogicalOr": PtLogicalOr,
    "PtLogicalXor": PtLogicalXor,
    "PtLt": PtLt,
    "PtMaskedSelect": PtMaskedSelect,
    "PtMatMul": PtMatMul,
    "PtMax": PtMax,
    "PtMean": PtMean,
    "PtMedian": PtMedian,
    "PtMin": PtMin,
    "PtMm": PtMm,
    "PtMul": PtMul,
    "PtNe": PtNe,
    "PtNeg": PtNeg,
    "PtOnes": PtOnes,
    "PtPermute": PtPermute,
    "PtPow": PtPow,
    "PtProd": PtProd,
    "PtRand": PtRand,
    "PtRandInt": PtRandInt,
    "PtRandn": PtRandn,
    "PtRemainder": PtRemainder,
    "PtReshape": PtReshape,
    "PtSaveModel": PtSaveModel,
    "PtScatter": PtScatter,
    "PtShowSize": PtShowSize,
    "PtShowText": PtShowText,
    "PtSin": PtSin,
    "PtSinh": PtSinh,
    "PtSize": PtSize,
    "PtSizeCreate": PtSizeCreate,
    "PtSizeToNumpy": PtSizeToNumpy,
    "PtSizeToString": PtSizeToString,
    "PtSqrt": PtSqrt,
    "PtSqueeze": PtSqueeze,
    "PtStd": PtStd,
    "PtSub": PtSub,
    "PtSum": PtSum,
    "PtTan": PtTan,
    "PtTanh": PtTanh,
    "PtToImage": PtToImage,
    "PtToLatent": PtToLatent,
    "PtToNumpy": PtToNumpy,
    "PtToRgbTensors": PtToRgbTensors,
    "PtTrainClassificationModel": PtTrainClassificationModel,
    "PtUnsqueeze": PtUnsqueeze,
    "PtVar": PtVar,
    "PtView": PtView,
    "PtWhere": PtWhere,
    "PtZeros": PtZeros,
    "PtnConvModel": PtnConvModel,
    "PtnLinearModel": PtnLinearModel,
    "PtoAdam": PtoAdam,
    "PtvDataset": PtvDataset,
    "PtvDatasetLoader": PtvDatasetLoader,
    "PtvTransformsToTensor": PtvTransformsToTensor,
    "PyKvFloatCreate": PyKvFloatCreate,
    "PyKvIntCreate": PyKvIntCreate,
    "PyKvStringCreate": PyKvStringCreate,
    "SNSBar": SNSBar,
    "SNSBoxplot": SNSBoxplot,
    "SNSHeatmap": SNSHeatmap,
    "SNSHistogram": SNSHistogram,
    "SNSLine": SNSLine,
    "SNSPairplot": SNSPairplot,
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
    "NumpyShow": "Numpy Show",
    "NumpySqueeze": "Numpy Squeeze",
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
    "PandasCreateFromTensor": "Pandas Create From Tensor",
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
    "PandasFeatureSplitToNumpy": "Pandas Feature Split To Numpy",
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
    "PandasLoadExcel": "Pandas Load Excel",
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
    "PandasRenameAdvanced": "Pandas Rename Advanced",
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
    "PtAbs": "Pt Abs",
    "PtAcos": "Pt Acos",
    "PtAdd": "Pt Add",
    "PtArange": "Pt Arange",
    "PtArgmax": "Pt Argmax",
    "PtArgmin": "Pt Argmin",
    "PtAsin": "Pt Asin",
    "PtAtan": "Pt Atan",
    "PtBitwiseAnd": "Pt Bitwise And",
    "PtBitwiseLeftShift": "Pt Bitwise Left Shift",
    "PtBitwiseNot": "Pt Bitwise Not",
    "PtBitwiseOr": "Pt Bitwise Or",
    "PtBitwiseRightShift": "Pt Bitwise Right Shift",
    "PtBitwiseXor": "Pt Bitwise Xor",
    "PtBmm": "Pt Bmm",
    "PtBoolCreate": "Pt Bool Create",
    "PtCos": "Pt Cos",
    "PtCosh": "Pt Cosh",
    "PtDataLoader": "Pt Data Loader",
    "PtDiv": "Pt Div",
    "PtEinsum": "Pt Einsum",
    "PtEq": "Pt Eq",
    "PtEvaluateClassificationModel": "Pt Evaluate Classification Model",
    "PtExp": "Pt Exp",
    "PtFlatten": "Pt Flatten",
    "PtFloatCreate": "Pt Float Create",
    "PtFloorDiv": "Pt Floor Div",
    "PtFromImage": "Pt From Image",
    "PtFromLatent": "Pt From Latent",
    "PtFromNumpy": "Pt From Numpy",
    "PtFull": "Pt Full",
    "PtGather": "Pt Gather",
    "PtGe": "Pt Ge",
    "PtGt": "Pt Gt",
    "PtIndexSelect": "Pt Index Select",
    "PtIntCreate": "Pt Int Create",
    "PtLe": "Pt Le",
    "PtLinspace": "Pt Linspace",
    "PtLoadModel": "Pt Load Model",
    "PtLog": "Pt Log",
    "PtLogicalAnd": "Pt Logical And",
    "PtLogicalNot": "Pt Logical Not",
    "PtLogicalOr": "Pt Logical Or",
    "PtLogicalXor": "Pt Logical Xor",
    "PtLt": "Pt Lt",
    "PtMaskedSelect": "Pt Masked Select",
    "PtMatMul": "Pt Mat Mul",
    "PtMax": "Pt Max",
    "PtMean": "Pt Mean",
    "PtMedian": "Pt Median",
    "PtMin": "Pt Min",
    "PtMm": "Pt Mm",
    "PtMul": "Pt Mul",
    "PtNe": "Pt Ne",
    "PtNeg": "Pt Neg",
    "PtOnes": "Pt Ones",
    "PtPermute": "Pt Permute",
    "PtPow": "Pt Pow",
    "PtProd": "Pt Prod",
    "PtRand": "Pt Rand",
    "PtRandInt": "Pt Rand Int",
    "PtRandn": "Pt Randn",
    "PtRemainder": "Pt Remainder",
    "PtReshape": "Pt Reshape",
    "PtSaveModel": "Pt Save Model",
    "PtScatter": "Pt Scatter",
    "PtShowSize": "Pt Show Size",
    "PtShowText": "Pt Show Text",
    "PtSin": "Pt Sin",
    "PtSinh": "Pt Sinh",
    "PtSize": "Pt Size",
    "PtSizeCreate": "Pt Size Create",
    "PtSizeToNumpy": "Pt Size To Numpy",
    "PtSizeToString": "Pt Size To String",
    "PtSqrt": "Pt Sqrt",
    "PtSqueeze": "Pt Squeeze",
    "PtStd": "Pt Std",
    "PtSub": "Pt Sub",
    "PtSum": "Pt Sum",
    "PtTan": "Pt Tan",
    "PtTanh": "Pt Tanh",
    "PtToImage": "Pt To Image",
    "PtToLatent": "Pt To Latent",
    "PtToNumpy": "Pt To Numpy",
    "PtToRgbTensors": "Pt To Rgb Tensors",
    "PtTrainClassificationModel": "Pt Train Classification Model",
    "PtUnsqueeze": "Pt Unsqueeze",
    "PtVar": "Pt Var",
    "PtView": "Pt View",
    "PtWhere": "Pt Where",
    "PtZeros": "Pt Zeros",
    "PtnConvModel": "Ptn Conv Model",
    "PtnLinearModel": "Ptn Linear Model",
    "PtoAdam": "Pto Adam",
    "PtvDataset": "Ptv Dataset",
    "PtvDatasetLoader": "Ptv Dataset Loader",
    "PtvTransformsToTensor": "Ptv Transforms To Tensor",
    "PyKvFloatCreate": "Py Kv Float Create",
    "PyKvIntCreate": "Py Kv Int Create",
    "PyKvStringCreate": "Py Kv String Create",
    "SNSBar": "SNS Bar Chart",
    "SNSBoxplot": "SNS Boxplot",
    "SNSHeatmap": "SNS Heatmap",
    "SNSHistogram": "SNS Histogram",
    "SNSLine": "SNS Line Plot",
    "SNSPairplot": "SNS Pairplot",
    "SNSScatter": "SNS Scatter Plot",
}


"""
Below two lines were taken from:
https://github.com/pythongosssss/ComfyUI-Custom-Scripts/blob/main/__init__.py
See credit/credit.md for the full license.
"""

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
