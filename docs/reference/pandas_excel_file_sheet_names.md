# Pandas Excel File Sheet Names
Returns the string list of sheet names contained in the Excel file.

This node uses ExcelFile method using the openpyxl package.
The openpyxl package is specified as a dependency in requirements.txt, so you should not need to manually install it.
See [Pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.html) for details.

To display the list, connect output to PyListToString node to convert the list to a string, then connect the output to Pandas Show Text node to display the string.

## Input
| Name | Data type |
|---|---|
| file_path | String |

## Output
| Data type |
|---|
| Pylist |

<HR>
Category: IO

ComfyUI Data Analysis Node Reference. © 2025 Hide Inada (HowToSD.com). All rights reserved.
