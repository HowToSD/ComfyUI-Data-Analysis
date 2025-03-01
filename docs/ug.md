# User's Guide

For a complete list of nodes, refer to [the Node reference](reference/node_reference.md).

## Note
This page was originally created using an older version of ComfyUI Data Analysis, so some screenshots and references may include deprecated node names and outdated socket data types. Additionally, it covers only a portion of the current node set. Refer to the Node Reference for specific functionality.

## Basic Concepts
### How to connect nodes for DataFrame
To connect the DataFrame output from one Pandas node to another, move the wire toward the top-left of the text field. You may need to hover around the corner to find the correct connection point.

### How to add a node
You can right-click, select **Add Node**, go to **Data Analysis**, and look for the following nodes:

A faster way is to double-click the canvas to open the node search dialog.

The examples directory contains workflows that load data from an example dataset included in this package. These workflows should give you a good idea about how to use these nodes.

## Loading data
Use **Pandas Load CSV** node to load a CSV, or **Pandas Load CSV With Index** node if the CSV contains an index column.  These nodes assume that the file is encoded in utf-8. If the file is not encoded in utf-8, use **Pandas Load CSV With Encoding** to specify the encoding of the file.  This is necessary if the data was collected before utf-8 encoding became popular.  For example, you can try "latin_1" for a file that contains accented characters in the US and Western Europe.
![Pandas Load CSV node](images/load.jpg)

Use **Pandas Load JSON** node to load a JSON file.

These nodes emit a DataFrame object.
CSV file path is relative to the ComfyUI installation directory unless you specify the absolute file path.

## Saving data
Use **Pandas Save CSV** node to save the DataFrame to a CSV file.
Use **Pandas Save JSON** node to save the DataFrame to a JSON file.

## Creating data on the UI
To construct a DataFrame on the UI, use **Pandas Create** or **Pandas Create with Index** nodes. These nodes display the multiline text area where you can enter the data in CSV format.
If the data contains an index column, use **Pandas Create with Index** and specify the index column.

![Pandas Columns and Pandas Index](images/columns_index.png)

Use **CDA JSON Create** to create JSON from a string entered in a text field.  For example, if you want to create a list for a node that requires the list of integers for input, this node is ideal.

## Extracting column and row labels
Use **Pandas Columns** and **Pandas Index** nodes.  As these nodes output JSON-serialized Index object, to display the value, use **Pandas Show Text** node as shown below:

![Pandas Create and Pandas Create With Index](images/create.png)

## Selecting columns and rows
Use **Pandas Select Columns** for selecting columns.
For rows, there are multiple options.
Use **Pandas Select Rows** to select rows by a filter condition.

![Pandas select subset](images/subset.jpg)

You can use **Pandas Loc Row Series** to select a row by row label (index).
You can use  **Pandas Iloc Row Series** to select a row by row integer position.
These nodes returns a JSON-serialized Series object.

You can use  **Pandas Iloc Rows DataFrame** to select rows by the list of row integer positions. This node returns a JSON-serialized DataFrame object.
You need to pass the list of integers to this node. This can be done by using the **CDA JSON Create** node.
![Pandas Iloc Rows DataFrame](images/iloc_rows_dataframe.png)

For  **Pandas Loc Row Series**, data type of the labels needs to be specified as shown below:
![Pandas Loc Row Series](images/loc_row_series.png)

For  **Pandas Iloc Row Series**, you only need to specify the row integer position:
![Pandas Iloc Row Series](images/iloc_row_series.png)

Note that in Pandas, integer position is an equivalent of an index in other software,
while "index" means a unique label assigned to each row. See [pandas.DataFrame.iloc.html](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html).

## Selecting a cell by row label (index) and column label
Use **Pandas Loc Cell Str**  for selecting a cell by row label (index) and column label. Data type of the labels needs to be specified as shown below:

![Pandas Loc Cell Str](images/loc_cell_str.png)

This node outputs the cell value as a string irrespective of the actual cell data type.

## Grouping Rows
Use **Pandas Group By** to group rows and apply aggregation functions.
Currently below aggregation functions are supported:
* sum
* mean
* count
* std
* min
* max

Below shows an example of using sum, mean, count functions:
![Group By](images/group_by1.png)

Below shows an example of using std, min, max functions:

![Group By](images/group_by2.png)

You can also have multiple columns to apply aggregation functions. In the below example, Qty and Price columns are aggregated for the Fruit column:
![Group By](images/group_by3.png)

## Joining DataFrames
Use **Pandas Join**.  You can select from inner, left, right, outer joins.
First, use two **Pandas Load CSV** nodes to load two CSVs for the left DataFrame and right DataFrame.

![Load two CSVs into DataFrames](images/join_data_load.png)

### Inner join
Specify the common column in the "on column name" field, and set the join method to **inner** in the **Pandas Join** node.
![Inner join](images/inner_join.png)

### Left join
Specify the common column in the "on column name" field, and set the join method to **left** in the **Pandas Join** node.
![Left join](images/left_join.png)

### Right join
Specify the common column in the "on column name" field, and set the join method to **right** in the **Pandas Join** node.
![Right join](images/right_join.png)

### Outer join
Specify the common column in the "on column name" field, and set the join method to **outer** in the **Pandas Join** node.
![Outer join](images/outer_join.png)

The workflow file examples/workflows/join.json contains all of the above cases.

## Extract the first few rows
Use **Pandas Head**.

## Missing value processing
Use **Pandas Is NA** for checking DataFrame for missing values, and **Pandas Drop NA** for dropping missing values from DataFrame.

![Pandas Is NA](images/isna.png)

## Display text ##
Use **Pandas Show Text** node.

Currently this node is using the code taken from ComfyUI-Custom-Scripts's Show Text custom node (
https://github.com/pythongosssss/ComfyUI-Custom-Scripts/blob/main/py/show_text.py).
This node has been copied to display text without requiring the user to install the above custom nodes package. However, if you already have ComfyUI-Custom-Scripts, you can also use the Show Text node from the package.

## Displaying DataFrame contents
Use **Pandas Show DataFrame** node. When the number of rows is large, This node automatically hides middle rows during string conversion, so the display size should be always manageable.

## Displaying Series contents
Use **Pandas Show Series** node.

## Extracting DataFrame statistics
Use **Pandas Summary** to extract statistics then connect the output to **Pandas Show Text** for display.
![Pandas Summary](images/summary.png)

## Sorting DataFrame by a column
Use **Pandas Sort**.

![Pandas Sort](images/sort.jpg)

## Summary statistics
You can compute summary statistics for each column in a DataFrame using below nodes:
* **Pandas Count** to get the number of rows for the column.
* **Pandas Min** to get the minimum row value within a column.
* **Pandas Max** to get the maximum value of row values within a column.
* **Pandas Mean** to get the mean of row values within a column.
* **Pandas Median** to get the median of row values within a column.
* **Pandas Mode** to get the mode of row values within a column.
* **Pandas Sum** to get the sum of row values within a column.
* **Pandas Std** to get the standard deviation of row values within a column.
* **Pandas Var** to get the variance of row values within a column.

All nodes return a Series except for Pandas Mode, which returns a DataFrame. This is necessary because multiple values may occur with the highest frequency. For example:
```
apple
apple
apple
banana
donut
coconut
coconut
coconut
```
In this case, both apple and coconut are the mode.

## Binary operators for DataFrames and Series
For binary operation for two DataFrames, you can use below operators:
| Node Name               | Functionality                        |
|-------------------------|-------------------------------------|
| **Pandas Add**  | Add two DataFrames     |
| **Pandas Div**  | Divide a DataFrame by another DataFrame     |
| **Pandas Mul**  | Multiply two DataFrames    |
| **Pandas Pow**  | Raise a DataFrame to the power of another DataFrame      |
| **Pandas Sub**  | Subtract a DataFrame from another DataFrame     |
| **Pandas Horizontal Concat**  | Concatenate two DataFrames horizontally (axis=1)    |
| **Pandas Vertical Concat**  | Concatenate two DataFrames vertically (axis=0)    |

![Pandas Vertical Concat & Horizontal Concat](images/concat.png)

For binary operation for a DataFrame and a Series, you can use below operators:
| Node Name               | Functionality                        |
|-------------------------|-------------------------------------|
| **Pandas Add Series**  | Add a DataFrame and a Series     |
| **Pandas Div Series**  | Divide a DataFrame by a Series     |
| **Pandas Mul Series**  | Multiply a DataFrame by a Series    |
| **Pandas Pow Series**  | Raise a DataFrame to the power of a Series      |
| **Pandas Sub Series**  | Subtract a Series from another DataFrame     |

## Convert DataFrame to a string
Use **Pandas To String**. This node is to convert the DataFrame to a displayable string, and this truncates the data when the data is large.  This can be used to display the data content in a text display node (e.g. Show Text node). However, you can use Show DataFrame nodes to display the DataFrame content, so you do not normally need to use this.

## Convert Series to a string
Use **Pandas Series To String**. This node converts a Pandas Series to a displayable string. You can use this as an input to the **Pandas Show Text** node.

## Displaying charts or plots
Use one of the below:
| Node | Purpose |
|---|---|
| **MPL Bar Chart**       | Generate a bar chart               |
| **MPL Line Plot**       | Generate a line plot               |
| **MPL Scatter Plot**    | Generate a scatter plot            |

![Plots](images/plots.png)