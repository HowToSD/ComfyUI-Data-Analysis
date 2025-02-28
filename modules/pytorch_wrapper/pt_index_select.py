from typing import Any, Dict
import torch
import ast


class PtIndexSelect:
    """
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
        Extracts elements from the input tensor along the specified dimension.

        Args:
            tens (torch.Tensor): The input tensor.
            dim (int): The dimension along which elements are selected.
            index (str): A string representation of a list of indices, e.g., "[0, 2]".

        Returns:
            tuple: A tuple containing the selected tensor.
        """
        # Convert the string index to a Python list
        index_list = ast.literal_eval(index)
        if not isinstance(index_list, list):
            raise ValueError("Index must be a list of integers.")

        # Convert the index list to a tensor
        index_tensor = torch.tensor(index_list, dtype=torch.long)

        # Perform index selection
        result = torch.index_select(tens, dim=dim, index=index_tensor)

        return (result,)
