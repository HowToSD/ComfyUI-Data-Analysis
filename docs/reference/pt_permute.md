# Pt Permute
Permutes the dimensions of a PyTorch tensor according to the specified order.
For example, if a tensor has shape (2, 3, 96, 32) and `new_axes="[0, 3, 1, 2]"`,
the output will have shape (2, 32, 3, 96).

Specify the new axis order in the `new_axes` field using brackets, as shown below:
```
[0, 3, 1, 2]
```

## Input
| Name | Data type |
|---|---|
| tens | Tensor |
| new_axes | String |

## Output
| Data type |
|---|
| Tensor |

<HR>
Category: PyTorch wrapper - Transform

ComfyUI Data Analysis Node Reference. © 2025 Hide Inada (HowToSD.com). All rights reserved.
