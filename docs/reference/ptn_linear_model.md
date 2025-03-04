# Ptn Linear Model
A linear model consisting of dense layers.  

### Fields:  
- `dim_list`: A comma-separated string representing layer dimensions.  
  It should contain the input dimension for the first layer and the output dimensions 
  for all layers. 
  
  Example for a two-layer network:  
  - Input data: 784  
  - Layer 1: 784 → 128  
  - Layer 2: 128 → 10  
  - Specify `"784, 128, 10"`  

- `bias_list`: A comma-separated string representing bias usage (True/False) per layer.  

- `num_layers`: The number of layers in the model.

## Input
| Name | Data type |
|---|---|
| dim_list | String |
| bias_list | String |
| num_layers | Int |

## Output
| Data type |
|---|
| Ptmodel |

<HR>
Category: PyTorch wrapper - Training

ComfyUI Data Analysis Node Reference. © 2025 Hide Inada (HowToSD.com). All rights reserved.
