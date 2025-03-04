# Ptv Dataset Loader
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

## Input
| Name | Data type |
|---|---|
| name | String |
| download | Boolean |
| root | String |
| batch_size | Int |
| shuffle | Boolean |
| dataset_parameters | String |
| load_parameters | String |

## Output
| Data type |
|---|
| Ptdataloader |

<HR>
Category: PyTorch wrapper - Training

ComfyUI Data Analysis Node Reference. © 2025 Hide Inada (HowToSD.com). All rights reserved.
