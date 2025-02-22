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
## DataFrame information
| Node | Description |
| --- | --- |
| [Pandas Columns](pandas_columns.md) | Retrieves the column labels of a pandas DataFrame. |
| [Pandas Index](pandas_index.md) | Retrieves the row labels (index) of a pandas DataFrame. |
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
## IO
| Node | Description |
| --- | --- |
| [CDA Float Create](cda_float_create.md) | Creates a Python float using a value entered in the text field. |
| [CDA Int Create](cda_int_create.md) | Creates a Python int using a value entered in the text field. |
| [CDA JSON Create](cda_json_create.md) | Creates a serialized JSON object using values entered in the text field. |
| [CDA String Create](cda_string_create.md) | Creates a Python String using a value entered in a single-line text field. |
| [CDA Text Create](cda_text_create.md) | Creates a Python String using a value entered in a multi-line text field. |
| [Pandas Create](pandas_create.md) | Creates a pandas DataFrame using values entered in the text field. |
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
## Plot
| Node | Description |
| --- | --- |
| [MPL Bar Chart](mpl_bar.md) |     Generates a bar chart from a Pandas DataFrame. |
| [MPL Line Plot](mpl_line.md) |     Generates a line plot from a pandas DataFrame. |
| [MPL Scatter Plot](mpl_scatter.md) |     Generates a scatter plot from a pandas DataFrame. |
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
| [Pandas Horizontal Concat](pandas_horizontal_concat.md) | Horizontally concatenates two pandas DataFrames. |
| [Pandas Horizontal Split](pandas_horizontal_split.md) | Horizontally splits a Pandas DataFrame into two pandas DataFrames. |
| [Pandas Join](pandas_join.md) | Merges two pandas DataFrames based on a common column. |
| [Pandas Rename](pandas_rename.md) | Renames an index (row label) or a column label. |
| [Pandas Series To Data Frame](pandas_series_to_dataframe.md) | Converts a Pandas Series to a DataFrame. |
| [Pandas Set Index](pandas_set_index.md) | Create index (row label) from existing column or columns. |
| [Pandas Sort](pandas_sort.md) | Sorts a pandas DataFrame by a specified column. |
| [Pandas Transpose](pandas_transpose.md) | Transposes a DataFrame. |
| [Pandas Vertical Concat](pandas_vertical_concat.md) | Vertically concatenates two pandas DataFrames. |
| [Pandas Vertical Split](pandas_vertical_split.md) | Vertically splits a Pandas DataFrame into two pandas DataFrames. |
