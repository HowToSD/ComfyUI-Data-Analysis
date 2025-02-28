# Pt Std
Computes the standard deviation of a PyTorch tensor along the specified dimension(s).

Specify 1 to use Bessel's correction (N-1) for sample standard deviation.
Specify 0 to compute population standard deviation.

Specify the dimension(s) in the `dim` field using an integer, a list, or a tuple, as shown below:
```
0, [0], or (1, 2)
```

## Input
| Name | Data type |
|---|---|
| tens | Tensor |
| correction | Int |
| dim | String |
| keepdim | Boolean |

## Output
| Data type |
|---|
| Tensor |

<HR>
Category: PyTorch wrapper - Reduction operation & Summary statistics

ComfyUI Data Analysis Node Reference. © 2025 Hide Inada (HowToSD.com). All rights reserved.
