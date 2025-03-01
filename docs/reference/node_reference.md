# Node Reference
## Aggregation
| Node | Description |
| --- | --- |
| [Pandas Group By](pandas_group_by.md) | Computes aggregate values for groups in a DataFrame. |
## Arithmetic method
| Node | Description |
| --- | --- |
| [Pandas Add](pandas_add.md) | Adds two pandas DataFrames. |
| [Pandas Add Scalar Float](pandas_add_scalar_float.md) | Adds a floating-point number to a Pandas DataFrame. |
| [Pandas Add Scalar Int](pandas_add_scalar_int.md) | Adds an integer to a Pandas DataFrame. |
| [Pandas Add Series](pandas_add_series.md) | Adds a Pandas Series to a pandas DataFrames. |
| [Pandas Div](pandas_div.md) | Divides a Pandas DataFrame by another DataFrame. |
| [Pandas Div Scalar Float](pandas_div_scalar_float.md) | Divides a Pandas DataFrame by a floating-point number. |
| [Pandas Div Scalar Int](pandas_div_scalar_int.md) | Divides a Pandas DataFrame by an integer. |
| [Pandas Div Series](pandas_div_series.md) | Divides a Pandas DataFrame by a Pandas Series. |
| [Pandas Mul](pandas_mul.md) | Multiplies two pandas DataFrames. |
| [Pandas Mul Scalar Float](pandas_mul_scalar_float.md) | Multiplies a Pandas DataFrame by a floating-point number. |
| [Pandas Mul Scalar Int](pandas_mul_scalar_int.md) | Multiplies a Pandas DataFrame by a floating-point number. |
| [Pandas Mul Series](pandas_mul_series.md) | Multiplies a Pandas DataFrame by a Pandas Series. |
| [Pandas Pow](pandas_pow.md) | Exponentiates two pandas DataFrames. |
| [Pandas Pow Scalar Float](pandas_pow_scalar_float.md) | Raises a Pandas DataFrame to the power of a floating-point number. |
| [Pandas Pow Scalar Int](pandas_pow_scalar_int.md) | Raises a Pandas DataFrame to the power of an integer. |
| [Pandas Pow Series](pandas_pow_series.md) | Raises a Pandas DataFrame to the power of a Pandas Series. |
| [Pandas Sub](pandas_sub.md) | Subtracts a Pandas DataFrame from another DataFrame. |
| [Pandas Sub Scalar Float](pandas_sub_scalar_float.md) | Subtracts a floating-point number from a Pandas DataFrame. |
| [Pandas Sub Scalar Int](pandas_sub_scalar_int.md) | Subtracts an integer from a Pandas DataFrame. |
| [Pandas Sub Series](pandas_sub_series.md) | Subtracts a Pandas Series from a Pandas DataFrame. |
## Categorical summary
| Node | Description |
| --- | --- |
| [Pandas Crosstab](pandas_crosstab.md) | Creates a contingency table (crosstab, or cross-tabulation) from two or more columns in a DataFrame. |
| [Pandas Value Counts](pandas_value_counts.md) | Creates a frequency table from one or more columns in a DataFrame. |
## Cumulative calculations
| Node | Description |
| --- | --- |
| [Pandas Cummax](pandas_cummax.md) | Computes the cummax (cumulative max) of the DataFrame. |
| [Pandas Cummin](pandas_cummin.md) | Computes the cummin (cumulative minimum) of the DataFrame. |
| [Pandas Cumprod](pandas_cumprod.md) | Computes the cumprod (cumulative product) of the DataFrame. |
| [Pandas Cumsum](pandas_cumsum.md) | Computes the cumsum (cumulative sum) of the DataFrame. |
## Data cleansing
| Node | Description |
| --- | --- |
| [Pandas Drop Duplicates](pandas_drop_duplicates.md) | Drops duplicate rows from a Pandas DataFrame. |
| [Pandas Drop NA](pandas_dropna.md) | Drops missing values from a pandas DataFrame. |
| [Pandas Fill NA Scalar Float](pandas_fillna_scalar_float.md) | Replaces missing values in a Pandas DataFrame with a floating-point number. |
| [Pandas Fill NA Scalar Int](pandas_fillna_scalar_int.md) | Replaces missing values in a Pandas DataFrame with an integer. |
| [Pandas Is NA](pandas_isna.md) | Checks a pandas DataFrame for missing values. |
| [Pandas Replace](pandas_replace.md) | Replaces part or all of a string in each DataFrame cell with a specified string using a wildcard for matching.  If you want to remove some characters, then leave the replace_string field blank. |
## Data subset selection
| Node | Description |
| --- | --- |
| [Pandas Head](pandas_head.md) | Retrieves the first few rows of a pandas DataFrame. |
| [Pandas Iloc Row Series](pandas_iloc_row_series.md) | Selects a row from a pandas DataFrame and returning it as a Series. |
| [Pandas Iloc Rows Data Frame](pandas_iloc_rows_dataframe.md) | Selects rows from a pandas DataFrame and returning it as a DataFrame. |
| [Pandas Iloc Rows Slice Data Frame](pandas_iloc_rows_slice_dataframe.md) | Selects rows from a pandas DataFrame using a slice defined by a start and end integer position. The start position is inclusive, while the end position is exclusive. Returns the selected rows as a DataFrame. |
| [Pandas Loc Cell Str](pandas_loc_cell_str.md) | Selects a cell from a pandas DataFrame and output as a string. |
| [Pandas Loc Row MultiIndex DataFrame](pandas_loc_row_multiindex_dataframe.md) | Selects a row or rows from a pandas DataFrame with MultiIndex and output as a DataFrame. |
| [Pandas Loc Row Series](pandas_loc_row_series.md) | Selects a row from a pandas DataFrame and output as a Series. |
| [Pandas Select Columns](pandas_select_columns.md) | Selects specific columns from a pandas DataFrame. |
| [Pandas Select Rows](pandas_select_rows.md) | Selects specific rows from a pandas DataFrame based on a condition.  This node internally calls DataFrame.query(). |
| [Pandas Xs](pandas_xs.md) | Selects a subset of a Pandas DataFrame using specified index labels or positions. |
## Data type conversion
| Node | Description |
| --- | --- |
| [Pandas As Float](pandas_as_float.md) | Converts all cells in a pandas DataFrame to float type. |
| [Pandas As Int](pandas_as_int.md) | Converts all cells in a pandas DataFrame to integer type. |
| [Pandas As String](pandas_as_string.md) | Converts all cells in a pandas DataFrame to string type. |
| [Pandas To Numpy](pandas_to_numpy.md) | Converts a pandas DataFrame to Numpy ndarray. |
## DataFrame information
| Node | Description |
| --- | --- |
| [Pandas Columns](pandas_columns.md) | Retrieves the column labels of a pandas DataFrame. |
| [Pandas Index](pandas_index.md) | Retrieves the row labels (index) of a pandas DataFrame. |
## Date and time processing
| Node | Description |
| --- | --- |
| [Pandas Strftime](pandas_strftime.md) | Converts one or more datetime columns in a DataFrame to string columns. |
| [Pandas To Datetime](pandas_to_datetime.md) | Converts one or more string columns in a DataFrame to datetime columns. |
## Display data
| Node | Description |
| --- | --- |
| [CDA Show Float](cda_show_float.md) | Displays a floating-point number as text. |
| [CDA Show Int](cda_show_int.md) | Displays a Pandas Int as text. |
| [Pandas Index To String](pandas_index_to_string.md) | Converts a pandas Index to a string representation. |
| [Pandas Series To String](pandas_series_to_string.md) | Converts a pandas Series to a string representation. |
| [Pandas Show Data Frame](pandas_show_dataframe.md) | Displays a Pandas DataFrame as text. |
| [Pandas Show Index](pandas_show_index.md) | Displays a Pandas Index as text. |
| [Pandas Show Series](pandas_show_series.md) | Displays a Pandas Series as text. |
| [Pandas Show Text](pandas_show_text.md) | Displays a string. |
| [Pandas To String](pandas_to_string.md) | Converts a pandas DataFrame to a string representation. |
| [Pt Show Size](pt_show_size.md) | Displays PyTorch Size object as a string. |
| [Pt Show Text](pt_show_text.md) | Displays PyTorch tensor as a string. Note that the tensor is partially printed out when |
## IO
| Node | Description |
| --- | --- |
| [CDA Float Create](cda_float_create.md) | Creates a Python float using a value entered in the text field. |
| [CDA Int Create](cda_int_create.md) | Creates a Python int using a value entered in the text field. |
| [CDA JSON Create](cda_json_create.md) | Creates a serialized JSON object using values entered in the text field. |
| [CDA String Create](cda_string_create.md) | Creates a Python String using a value entered in a single-line text field. |
| [CDA Text Create](cda_text_create.md) | Creates a Python String using a value entered in a multi-line text field. |
| [Pandas Create](pandas_create.md) | Creates a pandas DataFrame using values entered in the text field. |
| [Pandas Create From Dict](pandas_create_from_dict.md) | Creates a pandas DataFrame from a Python dictionary. |
| [Pandas Create From Multiple Dict](pandas_create_from_multiple_dict.md) | Creates a pandas DataFrame from multiple Python dictionaries. |
| [Pandas Create From Numpy](pandas_create_from_numpy.md) | Creates a pandas DataFrame from a NumPy ndarray. |
| [Pandas Create From Tensor](pandas_create_from_tensor.md) | Creates a pandas DataFrame from a PyTorch tensor. |
| [Pandas Create Series From Dict](pandas_create_series_from_dict.md) | Creates a Pandas Series from a Python dictionary. |
| [Pandas Create With Index](pandas_create_with_index.md) | Creates a pandas DataFrame using values entered in the text field. Input data is assumed to have an index. |
| [Pandas Load CSV](pandas_load_csv.md) | Loads CSV files into a pandas DataFrame. |
| [Pandas Load CSV With Encoding](pandas_load_csv_with_encoding.md) | Loads CSV files into a pandas DataFrame. |
| [Pandas Load CSV With Index](pandas_load_csv_with_index.md) | Loads CSV files into a pandas DataFrame. |
| [Pandas Load HTML](pandas_load_html.md) | Scans an HTML file or webpage for tables and returns the number of DataFrames  |
| [Pandas Load JSON](pandas_load_json.md) | Loads JSON files into a pandas DataFrame. |
| [Pandas Save CSV](pandas_save_csv.md) | Saves a PandasDataFrame to a CSV file. |
| [Pandas Save JSON](pandas_save_json.md) | Saves a PandasDataFrame to a JSON file. |
## Math
| Node | Description |
| --- | --- |
| [Pandas Cos](pandas_cos.md) | Apply the cosine function to a pandas DataFrame and converting non-numeric values to NaN. |
| [Pandas Exp](pandas_exp.md) | Apply the exponential function to a pandas DataFrame and converting non-numeric values to NaN. |
| [Pandas Log](pandas_log.md) | Applying the natural logarithm function to a pandas DataFrame and converting non-numeric values to NaN. |
| [Pandas Sin](pandas_sin.md) | Applies the sine function to a pandas DataFrame and converting non-numeric values to NaN. |
| [Pandas Tan](pandas_tan.md) | Applies the tangent function to a pandas DataFrame and converting non-numeric values to NaN. |
## Miscellaneous
| Node | Description |
| --- | --- |
| [Pt Flatten](pt_flatten.md) | Flattens a PyTorch tensor into a 1D tensor. |
## Numpy
| Node | Description |
| --- | --- |
| [Numpy Float Create](numpy_float_create.md) | Creates a NumPy ndarray with 32-bit floating point precision  |
| [Numpy Int Create](numpy_int_create.md) | Creates a NumPy ndarray with 32-bit integer  |
| [Numpy Show](numpy_show.md) | Displays a Numpy ndarray as text. |
| [Numpy Squeeze](numpy_squeeze.md) | Removes a dimension at the specified position in the input array if it is of size 1. |
## Plot
| Node | Description |
| --- | --- |
| [MPL Bar Chart](mpl_bar.md) |     Generates a bar chart from a Pandas DataFrame. |
| [MPL Line Plot](mpl_line.md) |     Generates a line plot from a pandas DataFrame. |
| [MPL Pie Chart](mpl_pie_chart.md) | Generates a pie chart from a pandas DataFrame. |
| [MPL Scatter Plot](mpl_scatter.md) |     Generates a scatter plot from a pandas DataFrame. |
| [SNS Bar Chart](sns_bar.md) | Generates a bar chart from a Pandas DataFrame using Seaborn. |
| [SNS Boxplot](sns_boxplot.md) | Generates a boxplot from a Pandas DataFrame using Seaborn. |
| [SNS Heatmap](sns_heatmap.md) | Generates a heatmap from a Pandas DataFrame using Seaborn. |
| [SNS Histogram](sns_histogram.md) | Generates a histogram from a Pandas DataFrame using Seaborn. |
| [SNS Line Plot](sns_line.md) | Generates a line plot from a pandas DataFrame using Seaborn. |
| [SNS Pairplot](sns_pairplot.md) | Generates a pairplot from a Pandas DataFrame using Seaborn. |
| [SNS Scatter Plot](sns_scatter.md) | Generates a scatter plot from a pandas DataFrame using Seaborn. |
## PyTorch wrapper - Arithmetic operations
| Node | Description |
| --- | --- |
| [Pt Add](pt_add.md) | Adds two PyTorch tensors. |
| [Pt Div](pt_div.md) | Divides one PyTorch tensor by another element-wise. |
| [Pt Floor Div](pt_floor_divide.md) | Performs element-wise floor division on two PyTorch tensors. |
| [Pt Mul](pt_mul.md) | Multiplies two PyTorch tensors element-wise. |
| [Pt Pow](pt_pow.md) | Raises one PyTorch tensor to the power of another element-wise. |
| [Pt Remainder](pt_remainder.md) | Computes the element-wise remainder of division between two PyTorch tensors. |
| [Pt Sub](pt_sub.md) | Subtracts one PyTorch tensor from another. |
## PyTorch wrapper - Bitwise operations
| Node | Description |
| --- | --- |
| [Pt Bitwise And](pt_bitwise_and.md) | Performs a bitwise AND operation on two PyTorch tensors element-wise. |
| [Pt Bitwise Left Shift](pt_bitwise_left_shift.md) | Performs a bitwise left shift operation on two PyTorch tensors element-wise. |
| [Pt Bitwise Not](pt_bitwise_not.md) | Performs a bitwise NOT operation on a PyTorch tensor element-wise. |
| [Pt Bitwise Or](pt_bitwise_or.md) | Performs a bitwise OR operation on two PyTorch tensors element-wise. |
| [Pt Bitwise Right Shift](pt_bitwise_right_shift.md) | Performs a bitwise right shift operation on two PyTorch tensors element-wise. |
| [Pt Bitwise Xor](pt_bitwise_xor.md) | Performs a bitwise XOR operation on two PyTorch tensors element-wise. |
## PyTorch wrapper - Comparison operations
| Node | Description |
| --- | --- |
| [Pt Eq](pt_eq.md) | Tests whether two PyTorch tensors are equal element-wise. |
| [Pt Ge](pt_ge.md) | Tests whether elements in the first PyTorch tensor are greater than or equal to the corresponding elements in the second tensor. |
| [Pt Gt](pt_gt.md) | Tests whether elements in the first PyTorch tensor are greater than the corresponding elements in the second tensor. |
| [Pt Le](pt_le.md) | Tests whether elements in the first PyTorch tensor are less than or equal to the corresponding elements in the second tensor. |
| [Pt Lt](pt_lt.md) | Tests whether elements in the first PyTorch tensor are less than the corresponding elements in the second tensor. |
| [Pt Ne](pt_ne.md) | Tests whether two PyTorch tensors are not equal element-wise. |
## PyTorch wrapper - Indexing and Slicing Operations
| Node | Description |
| --- | --- |
| [Pt Gather](pt_gather.md) | Generates a tensor based on the index tensor using PyTorch's `gather` function. |
| [Pt Index Select](pt_index_select.md) | Extracts elements from the input tensor along a specified dimension using an index tensor. |
| [Pt Masked Select](pt_masked_select.md) | Extracts elements from the input tensor whose corresponding value in `masked_tens` is `True`. |
| [Pt Scatter](pt_scatter.md) | Generates a new tensor by replacing values at specified positions using an index tensor. |
| [Pt Where](pt_where.md) | Generates a new tensor by selecting values based on a condition tensor. |
## PyTorch wrapper - Logical operations
| Node | Description |
| --- | --- |
| [Pt Logical And](pt_logical_and.md) | Performs a logical AND operation on two PyTorch tensors element-wise. |
| [Pt Logical Not](pt_logical_not.md) | Performs a logical NOT operation on a PyTorch tensor element-wise. |
| [Pt Logical Or](pt_logical_or.md) | Performs a logical OR operation on two PyTorch tensors element-wise. |
| [Pt Logical Xor](pt_logical_xor.md) | Performs a logical XOR operation on two PyTorch tensors element-wise. |
## PyTorch wrapper - Math operations
| Node | Description |
| --- | --- |
| [Pt Abs](pt_abs.md) | Computes the absolute value of each element in a PyTorch tensor. |
| [Pt Acos](pt_acos.md) | Computes the arccosine (inverse cosine) of a PyTorch tensor element-wise. |
| [Pt Asin](pt_asin.md) | Computes the arcsine (inverse sine) of a PyTorch tensor element-wise. |
| [Pt Atan](pt_atan.md) | Computes the arc tangent (inverse tangent) of a PyTorch tensor element-wise. |
| [Pt Cos](pt_cos.md) | Computes the cosine of a PyTorch tensor element-wise. |
| [Pt Cosh](pt_cosh.md) | Computes the hyperbolic cosine of a PyTorch tensor element-wise. |
| [Pt Exp](pt_exp.md) | Performs an exponential operation on a PyTorch tensor element-wise. |
| [Pt Log](pt_log.md) | Computes the natural logarithm (log base e) of a PyTorch tensor element-wise. |
| [Pt Neg](pt_neg.md) | Computes the negation of each element in a PyTorch tensor. |
| [Pt Sin](pt_sin.md) | Computes the sine of a PyTorch tensor element-wise. |
| [Pt Sinh](pt_sinh.md) | Computes the hyperbolic sine of a PyTorch tensor element-wise. |
| [Pt Sqrt](pt_sqrt.md) | Computes the square root of each element in a PyTorch tensor. |
| [Pt Tan](pt_tan.md) | Computes the tangent of a PyTorch tensor element-wise. |
| [Pt Tanh](pt_tanh.md) | Computes the hyperbolic tangent of a PyTorch tensor element-wise. |
## PyTorch wrapper - Matrix operations
| Node | Description |
| --- | --- |
| [Pt Bmm](pt_bmm.md) | Performs batched matrix multiplication on two 3D PyTorch tensors. |
| [Pt Einsum](pt_einsum.md) | Performs Tensor operations specified in the Einstein summation equation. |
| [Pt Mat Mul](pt_matmul.md) | Performs matrix multiplication on two PyTorch tensors. |
| [Pt Mm](pt_mm.md) | Performs 2D matrix multiplication on two PyTorch tensors. |
## PyTorch wrapper - Reduction operation & Summary statistics
| Node | Description |
| --- | --- |
| [Pt Argmax](pt_argmax.md) | Computes the indices of the maximum values of a PyTorch tensor along the specified dimension(s). |
| [Pt Argmin](pt_argmin.md) | Computes the indices of the minimum values of a PyTorch tensor along the specified dimension(s). |
| [Pt Max](pt_max.md) | Computes the maximum values of a PyTorch tensor along the specified dimension(s). |
| [Pt Mean](pt_mean.md) | Computes the mean of a PyTorch tensor along the specified dimension(s). |
| [Pt Median](pt_median.md) | Computes the median of a PyTorch tensor along the specified dimension(s). |
| [Pt Min](pt_min.md) | Computes the minimum values of a PyTorch tensor along the specified dimension(s). |
| [Pt Prod](pt_prod.md) | Computes the product of a PyTorch tensor along the specified dimension(s). |
| [Pt Std](pt_std.md) | Computes the standard deviation of a PyTorch tensor along the specified dimension(s). |
| [Pt Sum](pt_sum.md) | Computes the sum of a PyTorch tensor along the specified dimension(s). |
| [Pt Var](pt_var.md) | Computes the variance of a PyTorch tensor along the specified dimension(s). |
## PyTorch wrapper - Size object support
| Node | Description |
| --- | --- |
| [Pt Size](pt_size.md) | Extracts the PyTorch Size object of a PyTorch tensor using the size() method. |
| [Pt Size Create](pt_size_create.md) | Creates a PyTorch Size using values entered in the text field. |
| [Pt Size To Numpy](pt_size_to_numpy.md) | Converts PyTorch Size object to NumPy ndarray. |
| [Pt Size To String](pt_size_to_string.md) | Converts PyTorch Size object to a Python string. |
## PyTorch wrapper - Tensor creation
| Node | Description |
| --- | --- |
| [Pt Arange](pt_arange.md) | Creates a PyTorch tensor using `torch.arange` with the specified start, end, and step values. |
| [Pt Bool Create](pt_bool_create.md) | Creates a PyTorch tensor of dtype bool from True or False values entered as a list in the text field. |
| [Pt Float Create](pt_float_create.md) | Creates a PyTorch tensor with 32-bit floating point precision  |
| [Pt From Image](pt_from_image.md) | Casts an Image tensor as a PyTorch tensor. |
| [Pt From Latent](pt_from_latent.md) | Casts a latent tensor as a PyTorch tensor. |
| [Pt From Numpy](pt_from_numpy.md) | Converts a NumPy ndarray to a PyTorch tensor while preserving its data type. |
| [Pt Full](pt_full.md) | Creates a PyTorch tensor filled with a specified value using the size entered in the text field. |
| [Pt Int Create](pt_int_create.md) | Creates a PyTorch tensor with 32-bit integer  |
| [Pt Linspace](pt_linspace.md) | Creates a PyTorch tensor using `torch.linspace` with the specified start, end, and steps values. |
| [Pt Ones](pt_ones.md) | Creates a PyTorch tensor of ones using the size entered in the text field. |
| [Pt Rand](pt_rand.md) | Creates a PyTorch tensor with values sampled from a uniform distribution  |
| [Pt Rand Int](pt_rand_int.md) | Creates a PyTorch tensor filled with random integers within a specified range using the size entered in the text field. |
| [Pt Randn](pt_randn.md) | Creates a PyTorch tensor with values sampled from a standard normal distribution (mean=0, std=1)  |
| [Pt Zeros](pt_zeros.md) | Creates a PyTorch tensor of zeros using the size entered in the text field. |
## PyTorch wrapper - Tensor data conversion
| Node | Description |
| --- | --- |
| [Pt To Image](pt_to_image.md) | Casts a PyTorch tensor as an Image tensor. |
| [Pt To Latent](pt_to_latent.md) | Casts a PyTorch tensor as a latent tensor. |
| [Pt To Numpy](pt_to_numpy.md) | Converts PyTorch tensor to NumPy ndarray. |
| [Pt To Rgb Tensors](pt_to_rgb_tensors.md) | Splits a PyTorch tensor into R, G, and B tensors. |
## PyTorch wrapper - Transform
| Node | Description |
| --- | --- |
| [Pt Permute](pt_permute.md) | Permutes the dimensions of a PyTorch tensor according to the specified order. |
| [Pt Reshape](pt_reshape.md) | Reshapes a PyTorch tensor into a specified shape using `torch.reshape()`. |
| [Pt Squeeze](pt_squeeze.md) | Removes a dimension at the specified position in the input tensor if it is of size 1. |
| [Pt Unsqueeze](pt_unsqueeze.md) | Adds a singleton dimension at the specified position in the input tensor. |
| [Pt View](pt_view.md) | Reshapes a PyTorch tensor into a specified shape using `torch.view()`. |
## Python wrapper
| Node | Description |
| --- | --- |
| [Py Kv Float Create](py_kv_float_create.md) | Creates a Python dictionary with a string key and a float value. |
| [Py Kv Int Create](py_kv_int_create.md) |  Creates a Python dictionary with an string key and an integer value. |
| [Py Kv String Create](py_kv_string_create.md) | Creates a Python dictionary with a string key and a string value. |
## Summary statistics
| Node | Description |
| --- | --- |
| [Pandas Corr](pandas_corr.md) | Computes the correlation of the DataFrame. You can select from the Pearson, Kendall or Spearman methods. |
| [Pandas Count](pandas_count.md) | Computes the count of a pandas DataFrame. |
| [Pandas Cov](pandas_cov.md) | Computes the covariance of the DataFrame. |
| [Pandas Kurtosis](pandas_kurtosis.md) | Computes the unbiased kurtosis of the DataFrame. |
| [Pandas Max](pandas_max.md) | Computes the max of a pandas DataFrame. |
| [Pandas Mean](pandas_mean.md) | Computes the mean of a pandas DataFrame. |
| [Pandas Median](pandas_median.md) | Computes the median of a pandas DataFrame. |
| [Pandas Min](pandas_min.md) | Computes the min of a pandas DataFrame. |
| [Pandas Mode](pandas_mode.md) | Computes the mode of a pandas DataFrame. |
| [Pandas Skew](pandas_skew.md) | Computes the unbiased skewness of the DataFrame. |
| [Pandas Std](pandas_std.md) | Computes the standard deviation of a pandas DataFrame. |
| [Pandas Sum](pandas_sum.md) | Computes the sum of a pandas DataFrame. |
| [Pandas Summary](pandas_summary.md) | Analyzes and summarizes a pandas DataFrame. |
| [Pandas Var](pandas_var.md) | Computes the variance of a pandas DataFrame. |
## Transformation
| Node | Description |
| --- | --- |
| [Pandas Feature Split To Numpy](pandas_feature_split_to_numpy.md) | Splits a Pandas DataFrame into feature Numpy ndarray and label Numpy ndarray. |
| [Pandas Horizontal Concat](pandas_horizontal_concat.md) | Horizontally concatenates two pandas DataFrames. |
| [Pandas Horizontal Split](pandas_horizontal_split.md) | Horizontally splits a Pandas DataFrame into two pandas DataFrames. |
| [Pandas Join](pandas_join.md) | Merges two pandas DataFrames based on a common column. |
| [Pandas Melt](pandas_melt.md) | Performs an unpivot operation (melt) on a pandas DataFrame. |
| [Pandas Pivot](pandas_pivot.md) | Computes a pivot table from a pandas DataFrame. |
| [Pandas Rename](pandas_rename.md) | Renames an index (row label) or a column label. |
| [Pandas Rename Advanced](pandas_rename_advanced.md) | Renames one or more indices (row labels) or column labels to new labels. |
| [Pandas Series To Data Frame](pandas_series_to_dataframe.md) | Converts a Pandas Series to a DataFrame. |
| [Pandas Set Index](pandas_set_index.md) | Create index (row label) from existing column or columns. |
| [Pandas Sort](pandas_sort.md) | Sorts a pandas DataFrame by a specified column. |
| [Pandas Transpose](pandas_transpose.md) | Transposes a DataFrame. |
| [Pandas Vertical Concat](pandas_vertical_concat.md) | Vertically concatenates two pandas DataFrames. |
| [Pandas Vertical Split](pandas_vertical_split.md) | Vertically splits a Pandas DataFrame into two pandas DataFrames. |
