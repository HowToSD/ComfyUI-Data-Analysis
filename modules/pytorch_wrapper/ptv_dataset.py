import inspect
from typing import Any, Dict, Optional, Callable, Tuple
import torch
import torchvision.datasets as datasets
import ast

from .utils import get_dataset_full_path

class PtvDataset:
    """
    A Torchvision Dataset class wrapper.
    
    Parameters  
    
    **name**  
      Specify a dataset class name such as MNIST, FashionMNIST in string.  
      This will be converted to a dataset class internally.  
    
    **download**  
      Set to True if you want to download.  
    
    **root**  
      Specify the root directory of the downloaded dataset relative to the  
      dataset directory of this extension, or specify the absolute path.
      If you leave as a blank, the dataset will be downloaded under the `datasets` directory  
      of this extension.
    
    **transform**  
      Data transforms e.g. transform to PyTorch tensor, normalize image.  
      Plug in the PTV Transforms node that contains Torchvision Transforms functionality.  
    
    **parameters**  
      Specify other parameters in Python dict format.  
      For example, if you want to set Train parameter to True to download the train set, specify:  
      ```  
      {"train": True}  
      ```  
      or if you want to download the test set, specify:  
      ```  
      {"train": False}  
      ```  
    
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
                "name": ("STRING", {"default": "", "multiline": False}),
                "download": ("BOOLEAN", {"default": True}),
                "root": ("STRING", {"default": "", "multiline": False}),
            },
            "optional": {
                "transform": ("PTVTRANSFORM", {}),
                "parameters": ("STRING", {"default": "", "multiline": True})
            }
        }

    RETURN_TYPES: Tuple[str] = ("PTVDATASET",)
    FUNCTION: str = "f"
    CATEGORY: str = "Training"

    @classmethod
    def IS_CHANGED(cls, **kw):
        return float("NaN")

    def f(self, 
          name: str,
          download: bool,
          root: str,
          parameters: str,
          transform: Optional[Callable] = None) -> Tuple:
        """
        Loads a dataset from Torchvision with specified parameters.  
        
        Args:  
            name (str): Name of the dataset class (e.g., MNIST, FashionMNIST).  
            download (bool): Whether to download the dataset.  
            root (str): Root directory for storing the dataset.  
            parameters (str): Additional dataset parameters in stringified dictionary format.  
            transform (Optional[Callable]): Transformations to apply to the dataset.  
        
        Returns:  
            Tuple: A tuple containing the dataset instance.  
        """
        
        with torch.inference_mode(False):
            param_dict = ast.literal_eval(parameters)

            # Converts the datasets class name to dataset class itself
            try:
                dataset_class = getattr(datasets, name)
            except AttributeError:
                raise ValueError(f"Dataset '{name}' is not available in torchvision.datasets")

            # Get valid parameters for the dataset class
            valid_params = inspect.signature(dataset_class).parameters

            # Filter only parameters that match the dataset's constructor
            filtered_params = {k: v for k, v in param_dict.items() if k in valid_params}

            if root:
                dataset_path = get_dataset_full_path(root)
            else:  # Use default directory
                dataset_path = get_dataset_full_path("")

            if transform:
                dc = dataset_class(download=download,
                                   root=dataset_path,
                                   transform=transform,
                                   **filtered_params)
            else:
                dc = dataset_class(download=download,
                                   root=dataset_path,
                                   **filtered_params)

            return (dc,)
