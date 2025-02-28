# Pt Gather
Generates a tensor based on the index tensor using PyTorch's `gather` function.

Specify the `dim` field using an integer to indicate the axis along which to gather elements.
Each input tensor element is selected based on the index tensor.

For example, consider the following input tensor:
```
[ [10, 20, 30, 40, 50],
  [100, 200, 300, 400, 500]]
```

and the corresponding index tensor:

```
[ [0, 4, 3, 2, 0],
  [4, 3, 0, 0, 0]]
```

If `dim = 0`, the function scans row-wise, treating each index value as a row index.
If `dim = 1`, it scans column-wise, interpreting each index value as a column index.

Let's analyze the case where `dim = 1`:

* Start at row 0, column 0.
* The index at this position is `index[0, 0] = 0`.
* PyTorch selects the value at position 0 from the array `[10, 20, 30, 40, 50]`, which is `10`.
* The result at this stage is:
  ```
  [[10, ?, ?, ?, ?]
   [?, ?, ?, ?, ?]]
  ```

* Moving to column 1: `index[0, 1] = 4`.
* The value at index 4 in `[10, 20, 30, 40, 50]` is `50`.
* The updated result is:
  ```
  [[10, 50, ?, ?, ?]
   [?, ?, ?, ?, ?]]
  ```

* Repeating this process for all elements constructs the final gathered tensor.

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
