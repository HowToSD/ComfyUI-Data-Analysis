# ComfyUI-Data-Analysis

ComfyUI-Data-Analysis is a custom module for analyzing data using Pandas and Matplotlib within ComfyUI.

Currently, it supports the following nodes:

- Loading CSV as a DataFrame
- Selecting a subset of columns from a DataFrame
- Selecting a subset of rows from a DataFrame by specifying a filter condition
- Sorting a DataFrame by a column
- Displaying the content of a DataFrame
- Extracting the first part of a DataFrame
- Joining two DataFrames (inner, left, right, outer joins)
- Outputting statistics of a DataFrame (e.g., standard deviation)
- Line plot
- Scatter plot
- Bar chart

You can connect these nodes to conduct complex analysis in an intuitive graphical way.  
You can also use other Comfy custom nodes to fit your needs (e.g., combining images).

These custom nodes aim to make data exploration and analysis more efficient and enjoyable.

## Installation

Installation via ComfyUI Manager is not supported yet, so please follow these steps:

1. Navigate to the `custom_nodes` directory within your ComfyUI installation.
2. Run the following command:

    ```bash
    git clone https://github.com/HowToSD/ComfyUI-Data-Analysis.git
    ```
    This will create a new subdirectory ComfyUI-Data-Analysis.

3. Restart ComfyUI.

## How to Use

You can right-click, select **Add Node**, go to **Data Analysis**, and look for the following nodes:

| Node Name               | Functionality                        |
|-------------------------|-------------------------------------|
| **Pandas Load CSV**     | Load a CSV file                    |
| **Pandas Select Columns** | Select specific columns from a DataFrame |
| **Pandas Select Rows**  | Filter rows based on conditions    |
| **Pandas Join**         | Join two DataFrames                |
| **Pandas Head**         | Extract the first few rows         |
| **Pandas Show DataFrame** | Display DataFrame contents        |
| **Pandas Summary**      | Show DataFrame statistics          |
| **Pandas Sort**         | Sort DataFrame by a column         |
| **Pandas To String**    | Convert DataFrame to a string      |
| **MPL Bar Chart**       | Generate a bar chart               |
| **MPL Line Plot**       | Generate a line plot               |
| **MPL Scatter Plot**    | Generate a scatter plot            |

A faster way is to double-click the canvas to open the node search dialog.

The examples directory contains workflows that load data from an example dataset included in this package. These workflows should give you a good idea about how to use these nodes.

# Notes
* To connect the output from a previous Pandas node to another Pandas node, move the wire toward the top-left of the text field.
* CSV file path is relative to the ComfyUI installation directory unless you specify the absolute file path.