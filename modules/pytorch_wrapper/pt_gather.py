from typing import Any, Dict
import torch
import ast


class PtGather:
    """
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

    category: PyTorch wrapper - Indexing and Slicing Operations
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "tens": ("TENSOR", {}),
                "dim": ("INT", {"default": 0, "min": -10, "max": 10}),
                "index": ("STRING", {"multiline": True})
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, tens: torch.Tensor, dim: int, index: str) -> tuple:
        """
        Gathers elements along the specified dimension using an index tensor.

        Args:
            tens (torch.Tensor): The input tensor.
            dim (int): The dimension along which to gather values.
            index (str): A string representation of the index tensor, provided in list format.

        Returns:
            tuple: A tuple containing the gathered tensor.
        """
        # Parse the index string to a Python list
        index = ast.literal_eval(index)
        
        # Convert the parsed list to a tensor
        index_tensor = torch.tensor(index, dtype=torch.long, device=tens.device)
        
        # Perform the gather operation
        gathered_tens = torch.gather(tens, dim=dim, index=index_tensor)
        
        return (gathered_tens,)
