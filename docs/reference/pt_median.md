# Pt Median
Computes the median of a PyTorch tensor along the specified dimension(s).

Specify the dimension(s) in the `dim` field using an integer as shown below:
```
0
```
or
```
1
```    
Note that PtMedian calls torch.median(), which returns the lower of the two numbers when the true median falls between them.

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
