# Ptv Dataset
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

## Input
| Name | Data type |
|---|---|
| name | String |
| download | Boolean |
| root | String |
| transform | Ptvtransform |
| parameters | String |

## Output
| Data type |
|---|
| Ptvdataset |

<HR>
Category: PyTorch wrapper - Training

ComfyUI Data Analysis Node Reference. © 2025 Hide Inada (HowToSD.com). All rights reserved.
