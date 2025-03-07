from typing import Any, Dict
import torchvision.transforms as transforms


class PtvTransformsResize:
    """
    Resizes and transforms elements of dataset to PyTorch tensors.

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
            "required": {
                "height": ("INT", {"default": 256, "min": 1, "max": 32768}),
                "width": ("INT", {"default": 256, "min": 1, "max": 32768})
            },
        }

    RETURN_TYPES: tuple = ("PTVTRANSFORM",)
    FUNCTION: str = "f"
    CATEGORY: str = "Training"

    def f(self, height: int, width: int) -> tuple:
        """
        Resizes and transforms elements of dataset to PyTorch tensors.

        Args:
            height (int): Target height of the input image after transform
            width (int): Target width of the inpt image after transform

        Returns:
            tuple: A tuple containing the transform callable.
        """
        c = transforms.Compose([
            transforms.Resize((height, width)),
            transforms.ToTensor()
        ])
        return(c,)


