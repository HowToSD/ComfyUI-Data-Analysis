from typing import Any, Dict, Optional, Callable
import torchvision.transforms as transforms


class PtvTransformsToTensor:
    """
    Transforms elements of dataset to PyTorch tensors.

    category: PyTorch wrapper - Training
    """

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the required input types.

        Returns:
            Dict[str, Any]: An empty dictionary.
        """
        return {
        }

    RETURN_TYPES: tuple = ("PTVTRANSFORM",)
    FUNCTION: str = "f"
    CATEGORY: str = "Training"

    def f(self) -> tuple:
        """
        Transforms elements of dataset to PyTorch tensors.

        Returns:
            tuple: A tuple containing the transform callable.
        """
        c = transforms.Compose([transforms.ToTensor()])
        return(c,)


