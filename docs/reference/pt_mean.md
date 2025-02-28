# Pt Mean
Computes the mean of a PyTorch tensor along the specified dimension(s).

This node supports only floating-point or complex tensors as input.

Specify the dimension(s) in the `dim` field using an integer, a list, or a tuple, as shown below:
```
0, [0], or (1, 2)
```

## Input
| Name | Data type |
|---|---|
| tens | Tensor |
| dim | String |
| keepdim | Boolean |

## Output
| Data type |
|---|
| Tensor |

<HR>
Category: PyTorch wrapper - Reduction operation & Summary statistics

ComfyUI Data Analysis Node Reference. © 2025 Hide Inada (HowToSD.com). All rights reserved.
