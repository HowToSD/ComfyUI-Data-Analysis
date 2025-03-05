from typing import Any, Dict, Tuple
import ast
import torch
import torch.nn as nn
from .ptn_linear_model_def import DenseModel


class PtnLinearModel:
    """
    A linear model consisting of dense layers.  

    ### Fields:  
    - `dim_list`: A string representing a Python list of layer dimensions.  
      It should contain the input dimension for the first layer and the output dimensions 
      for all layers. 
      
      Example for a two-layer network:  
      - Input data: 784  
      - Layer 1: 784 → 128  
      - Layer 2: 128 → 10  
      - Specify `"[784,128,10]"`  

    - `bias_list`: A string representing a Python list of bias usage (True/False) per layer.  
       Example: "[True,False]"

    - `num_layers`: The number of layers in the model.  

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
                "dim_list": ("STRING", {"default": "784,10"}),
                "bias_list": ("STRING", {"default": "{True}"}),
                "num_layers": ("INT", {"default": 1, "min": 1, "max": 2000}),
            }
        }

    RETURN_TYPES: Tuple[str] = ("PTMODEL",)
    FUNCTION: str = "f"
    CATEGORY: str = "Training"

    @classmethod
    def IS_CHANGED(cls, **kw):
        return float("NaN")

    def f(self, dim_list: str, bias_list: str, num_layers: int) -> Tuple[nn.Module]:
        """
        Constructs a dense neural network model.

        Args:
            dim_list (str): A comma-separated string representing layer dimensions.
            bias_list (str): A comma-separated string representing bias usage (True/False) per layer.
            num_layers (int): The number of layers in the model.

        Returns:
            Tuple[nn.Module]: A tuple containing the instantiated PyTorch model.
        
        Raises:
            ValueError: If `dim_list` length does not match `num_layers + 1`.
            ValueError: If `bias_list` length does not match `num_layers`.
        """
        dims = ast.literal_eval(dim_list)
        biases = ast.literal_eval(bias_list)

        if len(dims) - 1 != num_layers:
            raise ValueError(
                "dim_list and num_layers do not match. dim_list should contain "
                "the input dimension for the first layer and output dimensions for all layers. "
                "This list should be one element longer than the number of layers."
            )

        if len(biases) != num_layers:
            raise ValueError("bias_list and num_layers do not match.")

        with torch.inference_mode(False):
            model = DenseModel(dims, biases, num_layers)

        return (model,)
