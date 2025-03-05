# Ptn Conv Model
A convolutional model consisting of multiple convolutional layers.  

### Fields:  
- `input_dim`: A string representing the input dimensions in the format "(C,H,W)".  
  Example: `"(3,28,28)"` for a 3-channel 28x28 image.  

- `penultimate_dim`: An integer specifying the number of features before the output layer. If you specify 0, the number is computed internally.
  Default: `0`

- `output_dim`: An integer specifying the number of output features, which should match the number of target classes in classification.
  Default: `10`, Min: `1`, Max: `1e6`.  

- `channel_list`: A string representing a Python list of integers specifying the number of channels per layer excluding the channel for the input (e.g. 3 for the color image).
  Example: `"[32,64,128,256,512]"`.  

- `kernel_size_list`: A string representing a Python list of kernel sizes per layer.  
  Example: `"[3,3,3,3,1]"`.  

- `padding_list`: A string representing a Python list of padding values per layer.  
  Example: `"[1,1,1,1,0]"`.  

- `downsample_list`: A string representing a Python list of boolean values indicating whether to downsample at each layer.  
  Example: `"[True,True,True,True,False]"`.

## Input
| Name | Data type |
|---|---|
| input_dim | String |
| penultimate_dim | Int |
| output_dim | Int |
| channel_list | String |
| kernel_size_list | String |
| padding_list | String |
| downsample_list | String |

## Output
| Data type |
|---|
| Ptmodel |

<HR>
Category: PyTorch wrapper - Training

ComfyUI Data Analysis Node Reference. © 2025 Hide Inada (HowToSD.com). All rights reserved.
