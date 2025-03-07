# Ptv Image Folder Dataset
A Torchvision ImageFolder Dataset class wrapper.

Parameters  

**root**  
  Specify the root directory that contains subdirectories which of which contains images for each class.
  The subdirectory name needs to be named after each class.

**transform**  
  Data transforms e.g. transform to PyTorch tensor, normalize image.  
  Plug in the PTV Transforms node that contains Torchvision Transforms functionality.

## Input
| Name | Data type |
|---|---|
| root | String |
| transform | Ptvtransform |

## Output
| Data type |
|---|
| Ptvdataset |

<HR>
Category: PyTorch wrapper - Training

ComfyUI Data Analysis Node Reference. © 2025 Hide Inada (HowToSD.com). All rights reserved.
