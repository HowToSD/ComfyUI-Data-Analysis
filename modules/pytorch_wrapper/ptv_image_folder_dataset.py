from typing import Any, Dict, Optional, Callable, Tuple
import torch
from torchvision.datasets import ImageFolder

from .utils import get_dataset_full_path

class PtvImageFolderDataset:
    """
    A Torchvision ImageFolder Dataset class wrapper.
    
    Parameters  
    
    **root**  
      Specify the root directory that contains subdirectories which of which contains images for each class.
      The subdirectory name needs to be named after each class.

    **transform**  
      Data transforms e.g. transform to PyTorch tensor, normalize image.  
      Plug in the PTV Transforms node that contains Torchvision Transforms functionality.  

    category: PyTorch wrapper - Training
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
                "root": ("STRING", {"default": "", "multiline": False})
            },
            "optional": {
                "transform": ("PTVTRANSFORM", {})
            }
        }

    RETURN_TYPES: Tuple[str] = ("PTVDATASET",)
    FUNCTION: str = "f"
    CATEGORY: str = "Training"

    @classmethod
    def IS_CHANGED(cls, **kw):
        return float("NaN")

    def f(self, 
          root: str,
          transform: Optional[Callable] = None) -> Tuple:
        """
        Loads a dataset from Torchvision with specified parameters.  
        
        Args:  
            root (str): Root directory for storing the dataset.  
            transform (Optional[Callable]): Transformations to apply to the dataset.  
        
        Returns:  
            Tuple: A tuple containing the dataset instance.  
        """
        
        with torch.inference_mode(False):

            if root:
                dataset_path = get_dataset_full_path(root)
            else:  # Use default directory
                dataset_path = get_dataset_full_path("")

            dc = ImageFolder(root=dataset_path,
                                  transform=transform
                            )
            return (dc,)
