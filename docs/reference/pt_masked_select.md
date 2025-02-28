# Pt Masked Select
Extracts elements from the input tensor whose corresponding value in `masked_tens` is `True`.

Example:
```
Input Tensor:
[[1, 2, 3],
 [40, 50, 60],
 [700, 800, 900]]

Masked Tensor:
[[True, False, False],
 [False, True, False],
 [False, False, True]]

Output Tensor:
[1, 50, 900]
```

## Input
| Name | Data type |
|---|---|
| tens | Tensor |
| masked_tens | Tensor |

## Output
| Data type |
|---|
| Tensor |

<HR>
Category: PyTorch wrapper - Indexing and Slicing Operations

ComfyUI Data Analysis Node Reference. © 2025 Hide Inada (HowToSD.com). All rights reserved.
