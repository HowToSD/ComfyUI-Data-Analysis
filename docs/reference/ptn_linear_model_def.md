# Dense Model
A multi-layer dense neural network with ReLU activation after each dense layer, except for the final layer.

Args:
    dim_list (List[int]): List of feature dimensions. Should be of length `num_layers + 1`.
    bias_list (List[bool]): List indicating whether each layer should have a bias.
    num_layers (int): Number of layers in the model.

Example:
    For a three-layer network:
    - Layer 1: input -> output1
    - Layer 2: output1 -> output2
    - Layer 3: output2 -> output3
    
    `dim_list = [input_dim, output1_dim, output2_dim, output3_dim]`

<HR>
Category: Miscellaneous

ComfyUI Data Analysis Node Reference. © 2025 Hide Inada (HowToSD.com). All rights reserved.
