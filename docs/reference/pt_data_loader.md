# Pt Data Loader
Loads data from a dataset node and creates a PyTorch DataLoader.  

**dataset**  
Connect a PtvDataset node that provides the dataset.  

**batch size**  
Specifies the number of samples per batch.  

**shuffle**  
If True, shuffles the dataset before each epoch.

## Input
| Name | Data type |
|---|---|
| dataset | Ptvdataset |
| batch_size | Int |
| shuffle | Boolean |
| parameters | String |

## Output
| Data type |
|---|
| Ptdataloader |

<HR>
Category: PyTorch wrapper - Training

ComfyUI Data Analysis Node Reference. © 2025 Hide Inada (HowToSD.com). All rights reserved.
