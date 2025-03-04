import ast
import inspect
from typing import Any, Dict, Tuple
import torch
import torchvision.datasets as datasets
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
from .utils import get_dataset_full_path


class PtvDatasetLoader:
    """
    A node to combine the dataset and data loader into a single node.
    
    Transform is internally called to convert input data to PyTorch tensors.

    Parameters  
    
    **name**  
      Specify the dataset class name such as MNIST, FashionMNIST in string.  
      This will be converted to a dataset class internally.  
    
    **download**  
      Set to True if you want to download.  
    
    **root**  
      Specify the root directory of the downloaded dataset relative to the  
      dataset directory of this extension, or specify the absolute path.
      If you leave as a blank, the dataset will be downloaded under the `datasets` directory  
      of this extension.

    **batch_size**  
      The number of samples per batch.  
    
    **shuffle**  
      If True, shuffles the dataset before each epoch.
   
    **dataset parameters**  
      Specify other parameters in Python dict format.  
      For example, if you want to set Train parameter to True to download the train set, specify:  
      ```  
      {"train": True}  
      ```  
      or if you want to download the test set, specify:  
      ```  
      {"train": False}  
      ```  

    **load parameters**
      Additional parameters in Python dictionary format.

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
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 1e6}),
                "shuffle": ("BOOLEAN", {"default": False}),
            },
            "optional": {
                "dataset_parameters": ("STRING", {"default": '{"train":True}', "multiline": True}),
                "load_parameters": ("STRING", {"default": '{"num_workers:1}', "multiline": True})
            }
        }

    RETURN_TYPES: Tuple[str] = ("PTDATALOADER",)
    FUNCTION: str = "f"
    CATEGORY: str = "Training"

    @classmethod
    def IS_CHANGED(cls, **kw):
        return float("NaN")

    def f(self, 
          name: str,
          download: bool,
          root: str,
          batch_size: int,
          shuffle: bool,
          dataset_parameters: str,
          load_parameters: str) -> Tuple:
        """
        Loads a dataset from Torchvision with specified parameters.  
        
        Args:  
            name (str): Name of the dataset class (e.g., MNIST, FashionMNIST).  
            download (bool): Whether to download the dataset.  
            root (str): Root directory for storing the dataset.  
            batch_size (int): The number of samples per batch.
            shuffle (bool): If True, shuffles the dataset before each epoch.
            dataset_parameters (str): Additional dataset parameters in stringified dictionary format.  
            load_parameters (str): Additional parameters for data load in Python dictionary format.
        
        Returns:  
            Tuple: A tuple containing the dataset instance.  
        """
        
        with torch.inference_mode(False):
            dataset_param_dict = ast.literal_eval(dataset_parameters)

            # Converts the datasets class name to dataset class itself
            try:
                dataset_class = getattr(datasets, name)
            except AttributeError:
                raise ValueError(f"Dataset '{name}' is not available in torchvision.datasets")

            # Get valid parameters for the dataset class
            valid_params = inspect.signature(dataset_class).parameters

            # Filter only parameters that match the dataset's constructor
            filtered_params = {k: v for k, v in dataset_param_dict.items() if k in valid_params}

            if root:
                dataset_path = get_dataset_full_path(root)
            else:  # Use default directory
                dataset_path = get_dataset_full_path("")

            transform = transforms.Compose([transforms.ToTensor()])
            dc = dataset_class(download=download,
                               root=dataset_path,
                               transform=transform,
                               **filtered_params)


            load_param_dict = ast.literal_eval(load_parameters)

            # Get valid parameters for the DataLoader class
            valid_params = inspect.signature(DataLoader).parameters

            # Filter only parameters that match the dataset's constructor
            filtered_params = {k: v for k, v in load_param_dict.items() if k in valid_params}

            dl = DataLoader(dataset=dc,
                            batch_size=batch_size,
                            shuffle=shuffle,
                            **filtered_params)
            return (dl,)