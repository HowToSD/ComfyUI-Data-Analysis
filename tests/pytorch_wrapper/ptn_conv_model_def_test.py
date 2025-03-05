import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pytorch_wrapper.ptn_conv_model_def import ConvModel, ConvSingleLayer


class TestPtnConvModelDef(unittest.TestCase):
    def setUp(self):
        """Setup method for initializing test conditions."""
        pass
    
    def test_single_layer_1_with_padding(self):
        """Test ConvSingleLayer with padding=1, no downsampling."""
        model = ConvSingleLayer(
                 in_channels=4,
                 out_channels=32,
                 kernel_size=3,
                 padding=1,
                 downsample=False,
                 apply_activation=True)
        x = torch.ones(1, 4, 28, 28)
        out = model(x)
        self.assertEqual(out.size(), torch.Size([1, 32, 28, 28]))

    def test_single_layer_no_padding(self):
        """Test ConvSingleLayer with padding=0, no downsampling."""
        model = ConvSingleLayer(
                 in_channels=4,
                 out_channels=32,
                 kernel_size=3,
                 padding=0,
                 downsample=False,
                 apply_activation=True)
        x = torch.ones(1, 4, 28, 28)
        out = model(x)
        self.assertEqual(out.size(), torch.Size([1, 32, 26, 26]))

    def test_single_layer_3_no_padding_downsample(self):
        """Test ConvSingleLayer with padding=0 and downsampling enabled."""
        model = ConvSingleLayer(
                 in_channels=4,
                 out_channels=32,
                 kernel_size=3,
                 padding=0,
                 downsample=True,
                 apply_activation=True)
        x = torch.ones(1, 4, 28, 28)
        out = model(x)
        self.assertEqual(out.size(), torch.Size([1, 32, 13, 13]))

    def test_1(self):
        """Test ConvModel with a single convolutional layer, checking output size."""
        model = ConvModel(
                 input_dim=(4, 28, 28),
                 penultimate_dim=0,
                 output_dim=10,
                 channel_list=[32],
                 kernel_size_list=[3],
                 padding_list=[1],
                 downsample_list=[False])

        x = torch.ones(1, 4, 28, 28)
        out = model(x)
        self.assertEqual(out.size(), torch.Size([1, 10]))

    def test_2(self):
        """Test ConvModel intermediate convolution layers' output size."""
        model = ConvModel(
                 input_dim=(4, 28, 28),
                 penultimate_dim=0,
                 output_dim=10,
                 channel_list=[32],
                 kernel_size_list=[3],
                 padding_list=[1],
                 downsample_list=[False])

        x = torch.ones(1, 4, 28, 28)
        for c in model.conv_layers:
            x = c(x)
        out = x
        self.assertEqual(out.size(), torch.Size([1, 32, 28, 28]))

    def test_3(self):
        """Test ConvModel with two convolutional layers and downsampling enabled."""
        model = ConvModel(
                 input_dim=(4, 28, 28),
                 penultimate_dim=0,
                 output_dim=10,
                 channel_list=[32,64],
                 kernel_size_list=[3,3],
                 padding_list=[1,1],
                 downsample_list=[True,True])

        x = torch.ones(1, 4, 28, 28)
        for c in model.conv_layers:
            x = c(x)
        out = x
        self.assertEqual(out.size(), torch.Size([1, 64, 7, 7]))

    def test_4(self):
        """Test ConvModel with three convolutional layers and downsampling enabled."""
        model = ConvModel(
                 input_dim=(4, 28, 28),
                 penultimate_dim=0,
                 output_dim=10,
                 channel_list=[32,64,128],
                 kernel_size_list=[3,3,3],
                 padding_list=[1,1,1],
                 downsample_list=[True,True,True])

        x = torch.ones(1, 4, 28, 28)
        for c in model.conv_layers:
            x = c(x)
        out = x
        self.assertEqual(out.size(), torch.Size([1, 128, 3, 3]))

    def test_5(self):
        """Test ConvModel with four convolutional layers and downsampling enabled."""
        model = ConvModel(
                 input_dim=(4, 28, 28),
                 penultimate_dim=0,
                 output_dim=10,
                 channel_list=[32,64,128,256],
                 kernel_size_list=[3,3,3,3],
                 padding_list=[1,1,1,1],
                 downsample_list=[True,True,True,True])

        x = torch.ones(1, 4, 28, 28)
        for c in model.conv_layers:
            x = c(x)
        out = x
        self.assertEqual(out.size(), torch.Size([1, 256, 1, 1]))

    def test_6(self):
        """Test ConvModel with five convolutional layers, last layer without downsampling."""
        model = ConvModel(
                 input_dim=(4, 28, 28),
                 penultimate_dim=0,
                 output_dim=10,
                 channel_list=[32,64,128,256,512],
                 kernel_size_list=[3,3,3,3,1],
                 padding_list=[1,1,1,1,0],
                 downsample_list=[True,True,True,True,False])

        x = torch.ones(1, 4, 28, 28)
        for c in model.conv_layers:
            x = c(x)
        out = x
        self.assertEqual(out.size(), torch.Size([1, 512, 1, 1]))


if __name__ == "__main__":
    unittest.main()
