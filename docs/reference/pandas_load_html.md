# Pandas Load HTML
Scans an HTML file or webpage for tables and returns the number of DataFrames 
found, followed by a list of up to 10 DataFrames. Each table is represented 
as a separate DataFrame. If fewer than 10 tables are found, empty DataFrames 
fill the remaining slots.

When loading from a URL, additional cleanup may be required.

## Input
| Name | Data type |
|---|---|
| file_path | String |

## Output
| Data type |
|---|
| Int |
| DataFrame |
| DataFrame |
| DataFrame |
| DataFrame |
| DataFrame |
| DataFrame |
| DataFrame |
| DataFrame |
| DataFrame |
| DataFrame |

<HR>
Category: IO

ComfyUI Data Analysis Node Reference. © 2025 Hide Inada (HowToSD.com). All rights reserved.
