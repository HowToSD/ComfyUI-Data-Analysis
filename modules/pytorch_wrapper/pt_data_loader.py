import inspect
from typing import Any, Dict
import ast
import torch
from torch.utils.data import DataLoader


class PtDataLoader:
    """
    Loads data from a dataset node and creates a PyTorch DataLoader.  

    **dataset**  
    Connect a PtvDataset node that provides the dataset.  

    **batch size**  
    Specifies the number of samples per batch.  

    **shuffle**  
    If True, shuffles the dataset before each epoch.  

    category: PyTorch wrapper - Training
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types required for data loading.

        Returns:
            Dict[str, Any]: A dictionary specifying required and optional input types.
        """
        return {
            "required": {
                "dataset": ("PTVDATASET", {}),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 1e6}),
                "shuffle": ("BOOLEAN", {"default": False}),
            },
            "optional": {
                "parameters": ("STRING", {"default": "", "multiline": True})
            }
        }

    RETURN_TYPES: tuple = ("PTDATALOADER",)
    FUNCTION: str = "f"
    CATEGORY: str = "Training"

    @classmethod
    def IS_CHANGED(cls, **kw):
        return float("NaN")

    def f(self, 
          dataset: Any,  # One of the classes defined in torchvision.datasets
          batch_size: int,
          shuffle: bool,
          parameters: str) -> tuple:
        """
        Creates a PyTorch DataLoader for the given dataset.

        Args:
            dataset (torchvision.datasets.{MNIST, ...}): An instance of a dataset from torchvision.datasets.
            batch_size (int): The number of samples per batch.
            shuffle (bool): If True, shuffles the dataset before each epoch.
            parameters (str): Additional parameters in Python dictionary format.

        Returns:
            tuple: A tuple containing the created DataLoader instance.
        """
        with torch.inference_mode(False):
            param_dict = ast.literal_eval(parameters)

            # Get valid parameters for the DataLoader class
            valid_params = inspect.signature(DataLoader).parameters

            # Filter only parameters that match the dataset's constructor
            filtered_params = {k: v for k, v in param_dict.items() if k in valid_params}

            dl = DataLoader(dataset=dataset,
                            batch_size=batch_size,
                            shuffle=shuffle,
                            **filtered_params)
            return (dl,)
