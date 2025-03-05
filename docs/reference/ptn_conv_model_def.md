# Conv Single Layer
A single convolutional layer followed by an optional ReLU activation and optional downsampling.

Shape is tensor of shape `(batch_size, in_channels, height, width)`.

Args:
    in_channels (int): Number of input channels.
    out_channels (int): Number of output channels.
    kernel_size (int): Size of the convolutional kernel.
    padding (int): Padding size for convolution.
    downsample (bool): If True, applies a 2x2 MaxPooling layer.
    apply_activation (bool, optional): If True, applies ReLU activation. Defaults to True.

<HR>
Category: Miscellaneous

ComfyUI Data Analysis Node Reference. © 2025 Hide Inada (HowToSD.com). All rights reserved.
