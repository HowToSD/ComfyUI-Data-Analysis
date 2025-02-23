# Pandas To Datetime
Converts one or more string columns in a DataFrame to datetime columns.

Note: When only the time portion is provided, the date defaults to 1900-01-01.
Refer to [https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior](the Python documentation) for valid date/time format strings.

## Input
| Name | Data type |
|---|---|
| dataframe | DataFrame |
| column_names | String |
| date_format | String |

## Output
| Data type |
|---|
| DataFrame |

<HR>
Category: Date and time processing

ComfyUI Data Analysis Node Reference. © 2025 Hide Inada (HowToSD.com). All rights reserved.
