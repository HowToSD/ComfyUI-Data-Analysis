from typing import Any, Dict
import torch
import ast


class PtPermute:
    """
    Permutes the dimensions of a PyTorch tensor according to the specified order.
    For example, if a tensor has shape (2, 3, 96, 32) and `new_axes="[0, 3, 1, 2]"`,
    the output will have shape (2, 32, 3, 96).

    Specify the new axis order in the `new_axes` field using brackets, as shown below:
    ```
    [0, 3, 1, 2]
    ```
    category: PyTorch wrapper - Transform
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
                "new_axes": ("STRING", {"multiline": True})
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, tens: torch.Tensor, new_axes: str) -> tuple:
        """
        Permutes the dimensions of the input tensor based on the specified order.

        Args:
            tens (torch.Tensor): The input tensor.
            new_axes (str): A string representation of the desired dimension order,
                            e.g., "[0, 3, 1, 2]" or "(0, 3, 1, 2)".

        Returns:
            tuple: A tuple containing the permuted PyTorch tensor.
        """
        # Convert string to a tuple of integers
        permute_order = tuple(ast.literal_eval(new_axes))

        # Ensure the parsed order is valid
        if not isinstance(permute_order, tuple) or not all(isinstance(i, int) for i in permute_order):
            raise ValueError(f"Invalid format for new_axes: {new_axes}. Must be a tuple or list of integers.")

        # Apply permutation
        tens = tens.permute(*permute_order)

        return (tens,)
