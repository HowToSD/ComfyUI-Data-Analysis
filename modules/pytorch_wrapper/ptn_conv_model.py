from typing import Any, Dict, Tuple
import ast
import torch
from .ptn_conv_model_def import ConvModel


class PtnConvModel:
    """
    A convolutional model consisting of multiple convolutional layers.  

    ### Fields:  
    - `input_dim`: A string representing the input dimensions in the format "(C,H,W)".  
      Example: `"(3,28,28)"` for a 3-channel 28x28 image.  

    - `penultimate_dim`: An integer specifying the number of features before the output layer. If you specify 0, the number is computed internally.
      Default: `0`

    - `output_dim`: An integer specifying the number of output features, which should match the number of target classes in classification.
      Default: `10`, Min: `1`, Max: `1e6`.  

    - `channel_list`: A string representing a Python list of integers specifying the number of channels per layer excluding the channel for the input (e.g. 3 for the color image).
      Example: `"[32,64,128,256,512]"`.  

    - `kernel_size_list`: A string representing a Python list of kernel sizes per layer.  
      Example: `"[3,3,3,3,1]"`.  

    - `padding_list`: A string representing a Python list of padding values per layer.  
      Example: `"[1,1,1,1,0]"`.  

    - `downsample_list`: A string representing a Python list of boolean values indicating whether to downsample at each layer.  
      Example: `"[True,True,True,True,False]"`.  

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
                "input_dim": ("STRING", {"default": "(3,28,28)"}),
                "penultimate_dim": ("INT", {"default": 0, "min": 0, "max": 1e6}),
                "output_dim": ("INT", {"default": 10, "min": 1, "max": 1e6}),
                "channel_list": ("STRING", {"default": "[32,64,128,256,512]"}),
                "kernel_size_list": ("STRING", {"default": "[3,3,3,3,1]"}),
                "padding_list": ("STRING", {"default": "[1,1,1,1,0]"}),
                "downsample_list": ("STRING", {"default": "[True,True,True,True,False]"})
            }
        }

    RETURN_TYPES: Tuple[str] = ("PTMODEL",)
    FUNCTION: str = "f"
    CATEGORY: str = "Training"

    @classmethod
    def IS_CHANGED(cls, **kw):
        return float("NaN")

    def f(self, 
          input_dim:str,
          penultimate_dim: int,
          output_dim: int,
          channel_list: str,
          kernel_size_list: str,
          padding_list: str,
          downsample_list: str) -> None:
        """
        Constructs a convolutional neural network model.

        Args:
            TODO:Update

        Returns:
            Tuple[nn.Module]: A tuple containing the instantiated PyTorch model.
        
        Raises:
            TODO:Update
        """
        input_dim_parsed = tuple(ast.literal_eval(input_dim))
        channel_list_parsed = ast.literal_eval(channel_list)
        kernel_size_list_parsed = ast.literal_eval(kernel_size_list)
        padding_list_parsed = ast.literal_eval(padding_list)
        downsample_list_parsed = ast.literal_eval(downsample_list)

        with torch.inference_mode(False):
            model = ConvModel(
                        input_dim_parsed,
                        penultimate_dim,
                        output_dim,
                        channel_list_parsed,
                        kernel_size_list_parsed,
                        padding_list_parsed,
                        downsample_list_parsed)
        return (model,)
