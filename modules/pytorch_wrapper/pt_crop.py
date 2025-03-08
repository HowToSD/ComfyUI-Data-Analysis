from typing import Any, Dict
import torch

class PtCrop:
    """
    Crops a PyTorch tensor to the specified size. The input tensor must have a shape of (c, h, w) or (b, c, h, w).

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
                "width": ("INT", {"default":0, "min":1, "max": 16384})
            }
        }

    RETURN_TYPES: tuple = ("TENSOR",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, tens: torch.Tensor, height: int, width: int) -> tuple:
        """
        Crops a PyTorch tensor.

        Args:
            tens (torch.Tensor): A PyTorch tensor with the shape of (c, h, w) or (b, c, h, w).
            height (int): New image height.
            width (int): New image width.

        Returns:
            tuple: A tuple containing a transformed tensor`.
        """
        dim = tens.dim()
        if dim == 3:  # c, h, w
            image_height = tens.size(1)
            image_width = tens.size(2)
        elif dim == 4:  # b, c, h, w
            image_height = tens.size(2)
            image_width = tens.size(3)
        else:
            raise ValueError("Only rank 3 or 4 tensors are supported for crop.")
        
        if height > image_height or width > image_width:
            raise ValueError("Specified crop size exceeds tensor dimensions.")

        # Compute starting position for cropping
        top = max(int((height - image_height) / 2), 0)
        left = max(int((width - image_width) / 2), 0)
    
        tens2 = tens[..., top:top+height, left:left+width]
        return (tens2,)