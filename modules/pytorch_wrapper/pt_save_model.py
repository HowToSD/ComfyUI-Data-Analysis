import os
from typing import Any, Dict
import torch
from .utils import get_model_full_path

class PtSaveModel:
    """
    A wrapper class for saving a PyTorch model.

    category: IO
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
                "model": ("PTMODEL", {}),
                "model_path": ("STRING", {"default": "model.pkl"})
            }
        }

    RETURN_NAMES: tuple = ("model full path",)
    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, model:Any, model_path: str):
        model_full_path = get_model_full_path(model_path)
        torch.save(model.state_dict(), model_full_path)
        return (os.path.realpath(model_full_path),)