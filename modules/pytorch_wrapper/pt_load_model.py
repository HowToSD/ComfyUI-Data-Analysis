import os
from typing import Any, Dict
import torch
from .utils import get_model_full_path

class PtLoadModel:
    """
    A wrapper class for saving a PyTorch model.

    category: PyTorch wrapper - Training
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

    RETURN_NAMES: tuple = ("model",)
    RETURN_TYPES: tuple = ("PTMODEL",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    @classmethod
    def IS_CHANGED(cls, **kw):
        return float("NaN")

    def f(self, model:Any, model_path: str):
        model_full_path = get_model_full_path(model_path)
        sd = torch.load(model_full_path, weights_only=True)
        model.load_state_dict(sd)
        return (model,)