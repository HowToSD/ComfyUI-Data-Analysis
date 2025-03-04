from typing import List, Dict, Any
import torch
import torch.nn as nn


class DenseSingleLayer(nn.Module):
    """A single dense layer followed by a ReLU activation.

    Args:
        in_features (int): Number of input features.
        out_features (int): Number of output features.
        bias (bool): If True, adds a learnable bias to the layer.

    pragma: skip_doc
    """

    @classmethod  # TODO: Dummy method to suppress ComfyUI warning
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        return {
        }

    def __init__(self, in_features: int, out_features: int, bias: bool) -> None:
        super().__init__()
        self.fc = nn.Linear(in_features, out_features, bias)
        self.activation = nn.ReLU()

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        """Forward pass of the dense layer with ReLU activation.

        Args:
            inputs (torch.Tensor): Input tensor of shape `(batch_size, in_features)`.

        Returns:
            torch.Tensor: Output tensor of shape `(batch_size, out_features)`.
        """
        x = self.fc(inputs)
        x = self.activation(x)
        return x


class DenseModel(nn.Module):
    """A multi-layer dense neural network with ReLU activation after each dense layer, except for the final layer.

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

    pragma: skip_doc
    """

    @classmethod  # TODO: Dummy method to suppress ComfyUI warning
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        return {
        }

    def __init__(self, dim_list: List[int], bias_list: List[bool], num_layers: int) -> None:
        super().__init__()

        self.no_activation_layers = nn.ModuleList([
            DenseSingleLayer(dim_list[i], dim_list[i + 1], bias_list[i])
            for i in range(num_layers - 1)
        ])

        self.dim_list = dim_list
        self.bias_list = bias_list
        self.num_layers = num_layers

        self.final_dense = nn.Linear(
            dim_list[num_layers - 1],  # in_features
            dim_list[num_layers],  # out_features
            bias_list[num_layers - 1]
        )
    
    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        """Forward pass of the dense model.

        Args:
            inputs (torch.Tensor): Input tensor of shape `(batch_size, dim_list[0])`.

        Returns:
            torch.Tensor: Output tensor of shape `(batch_size, dim_list[-1])`.
        """
        x = inputs.view(-1, self.dim_list[0])  # Ensure correct input shape

        for i in range(self.num_layers - 1):
            x = self.no_activation_layers[i](x)

        x = self.final_dense(x)

        return x
