# Pt Interpolate By Scale Factor
Resizes a PyTorch tensor using interpolation by scale factor. The input tensor must have a shape of (c, h, w) or (b, c, h, w).

In ComfyUI Analysis, the tensor data type is "TENSOR," while in ComfyUI, the type "IMAGE" is used. To pass image data from ComfyUI to a ComfyUI Analysis node (e.g., this interpolation node), first use the "Pt From Image" node to convert it to a tensor, then transpose the axes from (b, h, w, c) to (b, c, h, w) before passing it to this node.

This transposition can be performed using the "Pt Permute" node with (0, 2, 3, 1). To convert the output back to an image, apply "Pt Permute" with (0, 3, 1, 2) and then use the "Pt To Image" node.

## Input
| Name | Data type |
|---|---|
| tens | Tensor |
| scale_factor | Float |
| mode |  |

## Output
| Data type |
|---|
| Tensor |

<HR>
Category: PyTorch wrapper - Image processing

ComfyUI Data Analysis Node Reference. © 2025 Hide Inada (HowToSD.com). All rights reserved.
