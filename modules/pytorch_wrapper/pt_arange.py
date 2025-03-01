import os
import sys
from typing import Any, Dict, Tuple
import torch
from .utils import DTYPE_MAPPING

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from cda.utils import str_to_number, str_to_number_with_default


class PtArange:
    """
    Creates a PyTorch tensor using `torch.arange` with the specified start, end, and step values.
    
    The values are parsed from string inputs and converted to numeric types. This allows users to specify
    tensor range values in text fields. The function also ensures proper dtype selection.

    category: PyTorch wrapper - Tensor creation
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
                "start": ("STRING", {"default":"", "multiline": False}),
                "end": ("STRING", {"default":"", "multiline": False}),
                "step": ("STRING", {"default":"", "multiline": False}),
                "data_type": (("float32", "float16", "bfloat16", "float64", "uint8", "int8", "int16", "int32", "int64"),)
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"


    def f(self, start: str, end: str, step: str, data_type: str) -> Tuple[torch.Tensor]:
        """
        Creates a PyTorch tensor using `torch.arange` with the given start, stop, and step values.

        Args:
            start (str): The starting value of the sequence. If empty, defaults to 0.
            end (str): The end value of the sequence (exclusive).
            step (str): The step size for generating the sequence. If empty, defaults to 1.
            data_type (str): The desired PyTorch dtype for the resulting tensor.

        Returns:
            Tuple[torch.Tensor]: A tuple containing the generated PyTorch tensor.
        """
        start_value = str_to_number_with_default(start, 0)
        end_value = str_to_number(end)
        step_value = str_to_number_with_default(step, 1)
        tens = torch.arange(start_value, end_value, step_value, dtype=DTYPE_MAPPING[data_type])
        return (tens,)
