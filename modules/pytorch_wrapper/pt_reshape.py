from typing import Any, Dict
import torch
import ast


class PtReshape:
    """
    Reshapes a PyTorch tensor into a specified shape using `torch.reshape()`.
    The total number of elements must remain unchanged.

    For example, if a tensor has shape (2, 3, 4), and `new_shape="[6, 4]"`,
    the output will have shape (6, 4).

    Use -1 to automatically infer a dimension, e.g.:
    ```
    [2, -1]
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
                "new_shape": ("STRING", {"multiline": True})
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, tens: torch.Tensor, new_shape: str) -> tuple:
        """
        Reshapes the input tensor based on the specified shape.

        Args:
            tens (torch.Tensor): The input tensor.
            new_shape (str): A string representation of the desired shape,
                             e.g., "[2, -1]" or "(6, 4)".

        Returns:
            tuple: A tuple containing the reshaped PyTorch tensor.
        """
        # Convert string to a tuple of integers
        shape_order = tuple(ast.literal_eval(new_shape))

        # Ensure the parsed shape is valid
        if not isinstance(shape_order, tuple) or not all(isinstance(i, int) for i in shape_order):
            raise ValueError(f"Invalid format for new_shape: {new_shape}. Must be a tuple or list of integers.")

        # Apply reshape operation
        tens = tens.reshape(*shape_order)

        return (tens,)
