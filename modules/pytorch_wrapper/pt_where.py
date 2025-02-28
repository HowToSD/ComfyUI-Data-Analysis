from typing import Any, Dict
import torch

class PtWhere:
    """
    Generates a new tensor by selecting values based on a condition tensor.
    
    * `condition_tens` (torch.Tensor): Boolean tensor that determines which values are selected.
    * `true_tens` (torch.Tensor): Values to use where the condition is `True`.
    * `false_tens` (torch.Tensor): Values to use where the condition is `False`.
 
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
                "condition_tens": ("TENSOR", {}),
                "true_tens": ("TENSOR", {}),
                "false_tens": ("TENSOR", {}),
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self,
           condition_tens: torch.Tensor, 
           true_tens: torch.Tensor,
           false_tens: torch.Tensor) -> tuple:
        """
        Selects values from `true_tens` or `false_tens` based on `condition_tens`.

        Args:
            condition_tens (torch.Tensor): Boolean tensor indicating selection conditions.
            true_tens (torch.Tensor): Values used where condition is True.
            false_tens (torch.Tensor): Values used where condition is False.

        Returns:
            tuple: A tuple containing the modified tensor.
        """
        # Ensure condition_tens is a boolean tensor
        if condition_tens.dtype != torch.bool:
            raise TypeError(f"Expected `condition_tens` to be a boolean tensor, got {condition_tens.dtype}")

        # Ensure all tensors are compatible in shape
        if not torch.broadcast_shapes(condition_tens.shape, true_tens.shape, false_tens.shape):
            raise ValueError(f"Shape mismatch: condition {condition_tens.shape}, true {true_tens.shape}, false {false_tens.shape}")

        # Perform the conditional selection
        tens_out = torch.where(condition_tens, true_tens, false_tens)

        return (tens_out,)
