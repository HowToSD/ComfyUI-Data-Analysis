# Pt Where
Generates a new tensor by selecting values based on a condition tensor.

* `condition_tens` (torch.Tensor): Boolean tensor that determines which values are selected.
* `true_tens` (torch.Tensor): Values to use where the condition is `True`.
* `false_tens` (torch.Tensor): Values to use where the condition is `False`.

## Input
| Name | Data type |
|---|---|
| condition_tens | Tensor |
| true_tens | Tensor |
| false_tens | Tensor |

## Output
| Data type |
|---|
| Tensor |

<HR>
Category: PyTorch wrapper - Indexing and Slicing Operations

ComfyUI Data Analysis Node Reference. © 2025 Hide Inada (HowToSD.com). All rights reserved.
