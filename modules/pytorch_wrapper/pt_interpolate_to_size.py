from typing import Any, Dict
import torch

class PtInterpolateToSize:
    """
    Resizes a PyTorch tensor using interpolation. The input tensor must have a shape of (c, h, w) or (b, c, h, w).

    In ComfyUI Analysis, the tensor data type is "TENSOR," while in ComfyUI, the type "IMAGE" is used. To pass image data from ComfyUI to a ComfyUI Analysis node (e.g., this interpolation node), first use the "Pt From Image" node to convert it to a tensor, then transpose the axes from (b, h, w, c) to (b, c, h, w) before passing it to this node.

    This transposition can be performed using the "Pt Permute" node with (0, 2, 3, 1). To convert the output back to an image, apply "Pt Permute" with (0, 3, 1, 2) and then use the "Pt To Image" node.

    category: PyTorch wrapper - Image processing
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
                "tens": ("TENSOR", {}),
                "height": ("INT", {"default":0, "min":1, "max": 16384}),
                "width": ("INT", {"default":0, "min":1, "max": 16384}),
                "mode": (("nearest-exact", "bilinear", "bicubic", "nearest"),)
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, tens: torch.Tensor, height: int, width: int, mode: str) -> tuple:
        """
        Resizes a PyTorch tensor using interpolation.

        Args:
            tens (torch.Tensor): A PyTorch tensor with the shape of (c, h, w) or (b, c, h, w).
            height (int): New image height.
            width (int): New image width.
            mode (string): Interpolation mode.

        Returns:
            tuple: A tuple containing a transformed tensor`.
        """
        if tens.dim() == 3:
            rank3 = True
            tens_adjusted = torch.unsqueeze(tens, 0)
        else:
            rank3 = False
            tens_adjusted = tens

        tens2 = torch.nn.functional.interpolate(tens_adjusted, size=(height, width), mode=mode)

        if rank3:
            tens2 = torch.squeeze(tens2, 0)
        return (tens2,)