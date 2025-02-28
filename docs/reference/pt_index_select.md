# Pt Index Select
Extracts elements from the input tensor along a specified dimension using an index tensor.

`dim` specifies the dimension along which the selection occurs.
* For example, for 2D tensors:
** If `dim=0`, `index` selects rows.
** If `dim=1`, `index` selects columns (for 2D tensors).

`index` is a list of indices that will be converted into a tensor.

Example:
```
Input Tensor:
[[1, 2, 3],
 [40, 50, 60],
 [700, 800, 900]]

index = "[0, 2]"
dim = 0

Output Tensor:
[[1, 2, 3],
 [700, 800, 900]]
```

## Input
| Name | Data type |
|---|---|
| tens | Tensor |
| dim | Int |
| index | String |

## Output
| Data type |
|---|
| Tensor |

<HR>
Category: PyTorch wrapper - Indexing and Slicing Operations

ComfyUI Data Analysis Node Reference. © 2025 Hide Inada (HowToSD.com). All rights reserved.
