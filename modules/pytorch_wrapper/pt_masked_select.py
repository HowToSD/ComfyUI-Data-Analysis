from typing import Any, Dict
import torch


class PtMaskedSelect:
    """
    Extracts elements from the input tensor whose corresponding value in `masked_tens` is `True`.

    Example:
    ```
    Input Tensor:
    [[1, 2, 3],
     [40, 50, 60],
     [700, 800, 900]]

    Masked Tensor:
    [[True, False, False],
     [False, True, False],
     [False, False, True]]

    Output Tensor:
    [1, 50, 900]
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
                "masked_tens": ("TENSOR", {})
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, tens: torch.Tensor, masked_tens: torch.Tensor) -> tuple:
        """
        Extracts elements from `tens` where `masked_tens` is `True`.

        Args:
            tens (torch.Tensor): The input tensor.
            masked_tens (torch.Tensor): A boolean tensor specifying which elements to select.

        Returns:
            tuple: A tuple containing the selected tensor.
        """
        if masked_tens.dtype != torch.bool:
            raise ValueError("masked_tens must be a boolean tensor (dtype=torch.bool)")

        result = torch.masked_select(tens, masked_tens)
        return (result,)
