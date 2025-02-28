from typing import Any, Dict
import torch
import ast

class PtScatter:
    """
    Generates a new tensor by replacing values at specified positions using an index tensor.
    
    * Target tensor (tens): Some of whose values are replaced.
    * Source tensor (src): Values from this tensor replace a part or whole of the target tensor.
    * Index tensor (index): Specifies the positions in the target tensor for replacement.
  
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
                "index": ("STRING", {"multiline": True}),
                "src": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self,
           tens: torch.Tensor, 
           dim: int,
           index: str,
           src: str) -> tuple:
        """
        Replaces elements in the target tensor along the specified dimension using an index tensor.

        Args:
            tens (torch.Tensor): The target tensor whose values will be replaced.
            dim (int): The dimension along which values are replaced.
            index (str): A string representation of the index tensor (list format).
            src (str): A string representation of the source tensor (list format).

        Returns:
            tuple: A tuple containing the modified tensor.
        """
        # Parse the input index and source tensors from string representations
        index_list = ast.literal_eval(index)
        src_list = ast.literal_eval(src)

        # Convert to tensors
        index_tensor = torch.tensor(index_list, dtype=torch.long, device=tens.device)
        src_tensor = torch.tensor(src_list, dtype=tens.dtype, device=tens.device)

        # Ensure index and src shapes match
        if index_tensor.shape != src_tensor.shape:
            raise ValueError(f"Shape mismatch: index tensor {index_tensor.shape} and src tensor {src_tensor.shape} must match.")

        # Perform the scatter operation
        updated_tens = torch.scatter(tens.clone(), dim=dim, index=index_tensor, src=src_tensor)
        
        return (updated_tens,)
