from typing import Any, Dict
import torch


class PtEinsum:
    """
    Performs Tensor operations specified in the Einstein summation equation.
    
    Specify Einstein summation notation in the first socket.
    Specify two tensors in tens_a, tens_b. If you specify the third tensor, specify in tens_c.
    Otherwise, leave the socket unconnected.

    Sublist format is not supported.

    category: PyTorch wrapper - Matrix operations
    """

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the required input types.

        Returns:
            Dict[str, Any]: A dictionary of required input types.
        """
        return {
            "required": {
                "equation": ("STRING", {"default": ""}),
                "tens_a": ("TENSOR", {})
            },
            "optional":{
                "tens_b": ("TENSOR", {}),
                "tens_c": ("TENSOR", {})
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self,
          equation: str,
          tens_a: torch.Tensor,
          tens_b: torch.Tensor = None,
          tens_c: torch.Tensor = None) -> tuple:
        """
        Performs Tensor operations specified in the Einstein summation equation.

        Args:
            equation (str): Einstein summation equation.
            tens_a (torch.Tensor): A PyTorch tensor.
            tens_b (torch.Tensor): A PyTorch tensor.
            tens_c (torch.Tensor): A PyTorch tensor.

        Returns:
            tuple: A tuple containing the resultant tensor.
        """
        if tens_a is None:
            raise ValueError("tens_a is None")

        if tens_b is None and tens_c is None:
            tens_ret_val = torch.einsum(equation, tens_a)
        elif tens_c is None:
            tens_ret_val = torch.einsum(equation, tens_a, tens_b)
        else:
            tens_ret_val = torch.einsum(equation, tens_a, tens_b, tens_c)
        return (tens_ret_val,)
