from typing import List, Dict, Any, Tuple
import torch
import torch.nn as nn


class ConvSingleLayer(nn.Module):
    """A single convolutional layer followed by an optional ReLU activation and optional downsampling.

    Shape is tensor of shape `(batch_size, in_channels, height, width)`.

    Args:
        in_channels (int): Number of input channels.
        out_channels (int): Number of output channels.
        kernel_size (int): Size of the convolutional kernel.
        padding (int): Padding size for convolution.
        downsample (bool): If True, applies a 2x2 MaxPooling layer.
        apply_activation (bool, optional): If True, applies ReLU activation. Defaults to True.

    pragma: skip_doc
    """

    @classmethod  # TODO: Dummy method to suppress ComfyUI warning. DO NOT REMOVE
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        return {}

    def __init__(self, 
                 in_channels: int,
                 out_channels: int,
                 kernel_size: int,
                 padding: int,
                 downsample: bool,
                 apply_activation: bool = True) -> None:
        super().__init__()
        self.conv = nn.Conv2d(in_channels=in_channels,
                              out_channels=out_channels,
                              kernel_size=kernel_size,
                              padding=padding)
        self.apply_activation = apply_activation
        self.activation = nn.ReLU()
        self.downsample = downsample
        self.maxpool = nn.MaxPool2d(kernel_size=2, stride=2)

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        """Forward pass of the convolutional layer.

        Args:
            inputs (torch.Tensor): Input tensor of shape `(batch_size, in_channels, height, width)`.

        Returns:
            torch.Tensor: Output tensor after convolution, optional activation, and optional pooling.
        """
        x = self.conv(inputs)
        if self.downsample:
            x = self.maxpool(x)
        if self.apply_activation:
            x = self.activation(x)
        return x


class ConvModel(nn.Module):
    """A multi-layer convolutional neural network with ReLU activation after each convolutional layer, except for the final dense layer.

    Args:
        input_dim (Tuple[int, int, int]): Shape of a single input sample (C, H, W).
        penultimate_dim (int): Number of features before the final dense layer. If 0 is specified, this value is automatically computed internally.
        output_dim (int): Number of output features.
        channel_list (List[int]): List of channel sizes for each layer. This should not include the inputs channel.
          Input channel is taken from the first element of input_dim.
        kernel_size_list (List[int]): List of kernel sizes for each convolutional layer.
        padding_list (List[int]): List of padding values for each convolutional layer.
        downsample_list (List[bool]): List indicating whether downsampling should be applied after each layer.

    pragma: skip_doc
    """
   
    @classmethod  # TODO: Dummy method to suppress ComfyUI warning
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        return {}

    def __init__(self,
                 input_dim: Tuple[int, int, int],
                 penultimate_dim: int,
                 output_dim: int,
                 channel_list: List[int],
                 kernel_size_list: List[int],
                 padding_list: List[int],
                 downsample_list: List[bool]) -> None:
        super().__init__()

        # Validate list lengths
        if (len(channel_list) != len(kernel_size_list) or
            len(kernel_size_list) != len(padding_list) or
            len(padding_list) != len(downsample_list)):
            raise ValueError("channel_list, kernel_size_list, padding_list, and downsample_list must have the same length.")

        self.channel_list = [input_dim[0]] + channel_list

        # Initialize convolutional layers
        layers = []
        for i in range(len(self.channel_list) - 1):
            layers.append(
                ConvSingleLayer(
                    in_channels=self.channel_list[i],  
                    out_channels=self.channel_list[i + 1],  
                    kernel_size=kernel_size_list[i],
                    padding=padding_list[i],
                    downsample=downsample_list[i]
                )
            )

        self.conv_layers = nn.ModuleList(layers)

        if penultimate_dim == 0:
            # Try to auto compute penultimate_dim by processing the dummy input
            with torch.no_grad():
                dummy_input = torch.randn(1, *input_dim)  # B, C, H, W
                x = dummy_input
                for layer in self.conv_layers:
                    x = layer(x)
                checked_penultimate_dim = x.numel()  # Number of elements
        else:
            checked_penultimate_dim = penultimate_dim

        self.final_dense = nn.Linear(checked_penultimate_dim, output_dim, bias=True)

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        """Forward pass of the model.

        Args:
            inputs (torch.Tensor): Input tensor of shape `(batch_size, C, H, W)`.

        Returns:
            torch.Tensor: Output tensor of shape `(batch_size, output_dim)`.

        Raises:
            ValueError: If inputs is not a rank 4 tensor.
        """
        if inputs.dim() not in [3, 4]:
            raise ValueError("Inputs is not a rank 3 or 4 tensor.")
        
        if inputs.dim() == 3:
            x = torch.unsqueeze(inputs, 1)
        else:
            x = inputs
        
        for layer in self.conv_layers:
            x = layer(x)

        x = torch.flatten(x, start_dim=1)  # Flatten except batch-axis
        x = self.final_dense(x)
        return x
