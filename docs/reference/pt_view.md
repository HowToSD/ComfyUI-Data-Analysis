# Pt View
Reshapes a PyTorch tensor into a specified shape using `torch.view()`.
The total number of elements must remain unchanged.

For example, if a tensor has shape (2, 3, 4), and `new_shape="[6, 4]"`,
the output will have shape (6, 4).

Use -1 to automatically infer a dimension, e.g.:
```
[2, -1]
```

## Input
| Name | Data type |
|---|---|
| tens | Tensor |
| new_shape | String |

## Output
| Data type |
|---|
| Tensor |

<HR>
Category: PyTorch wrapper - Transform

ComfyUI Data Analysis Node Reference. © 2025 Hide Inada (HowToSD.com). All rights reserved.
