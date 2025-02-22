# Pandas Xs
Selects a subset of a Pandas DataFrame using specified index labels or positions.

This function extracts a portion of a DataFrame based on MultiIndex labels (row indices or column labels).

Users must specify:
* The labels to select (comma-separated for multiple labels).
* The level(s) within the MultiIndex (integer positions).
* The axis (whether selecting from rows or columns).

**Understanding "Level":**
In a MultiIndex DataFrame, a level refers to the hierarchical position of an index within the MultiIndex, which can be referenced using a 0-based integer position or an assigned level name.
Selecting the level using an integer position is similar to integer-based selection in `iloc`.

When specifying a label, Pandas needs to know which level of the MultiIndex to search. 
For example, if selecting "dog" as a row label and the DataFrame has multiple index levels, 
you must indicate whether to look in the first index (level 0) or the second index (level 1). 

If selecting multiple labels, their corresponding levels should be provided as a comma-separated list.

Example:
    Given a DataFrame with a 3-level MultiIndex, the first index is at level 0, the second at level 1, and the third at level 2. Selecting "dog" and "brown" at levels 1 and 2 requires specifying 1, 2 in the Level field of the node. These values are internally converted into a list and passed to Pandas.

The `axis` field specifies whether selection applies to row indices (`axis=0`) or column labels (`axis=1`).

## Input
| Name | Data type |
|---|---|
| dataframe | DataFrame |
| row_or_column_label | String |
| label_type |  |
| level | String |
| level_type |  |
| axis |  |

## Output
| Data type |
|---|
| DataFrame |

<HR>
Category: Data subset selection

ComfyUI Data Analysis Node Reference. © 2025 Hide Inada (HowToSD.com). All rights reserved.
