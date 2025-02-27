# Pt Rand Int
Creates a PyTorch tensor filled with random integers within a specified range using the size entered in the text field.
For example, if you want to create a 4D tensor of batch size=2, channel=3, height=96, width=32 with random integers in the range [0, 10),
enter [2,3,96,32] for size, 0 for min_value, and 10 for max_value.

## Input
| Name | Data type |
|---|---|
| min_value | Int |
| max_value | Int |
| size | String |
| data_type |  |

## Output
| Data type |
|---|
| Tensor |

<HR>
Category: PyTorch wrapper - Tensor creation

ComfyUI Data Analysis Node Reference. © 2025 Hide Inada (HowToSD.com). All rights reserved.
