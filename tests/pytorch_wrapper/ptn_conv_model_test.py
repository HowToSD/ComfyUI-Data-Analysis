import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pytorch_wrapper.ptn_conv_model import PtnConvModel


class TestPtnConvModel(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.model_node = PtnConvModel()

    def test_forward(self):
        model = self.model_node.f(
                 input_dim="(4, 28, 28)",
                 penultimate_dim=0,
                 output_dim=10,
                 channel_list="[32,64,128,256]",
                 kernel_size_list="[3,3,3,3]",
                 padding_list="[1,1,1,1]",
                 downsample_list="[True,True,True,True]"
        )[0]
        bs = 2
        x = torch.ones(bs, 4, 28, 28)
        out = model(x)
        self.assertEqual(out.size(), torch.Size([bs, 10]))

    def test_rank3_input(self):
        model = self.model_node.f(
                 input_dim="(1, 28, 28)",
                 penultimate_dim=0,
                 output_dim=10,
                 channel_list="[32,64,128,256]",
                 kernel_size_list="[3,3,3,3]",
                 padding_list="[1,1,1,1]",
                 downsample_list="[True,True,True,True]"
        )[0]
        bs = 2
        x = torch.ones(bs, 28, 28)
        out = model(x)
        self.assertEqual(out.size(), torch.Size([bs, 10]))

    def test_rank2_input(self):
        model = self.model_node.f(
                 input_dim="(1, 28, 28)",
                 penultimate_dim=0,
                 output_dim=10,
                 channel_list="[32,64,128,256]",
                 kernel_size_list="[3,3,3,3]",
                 padding_list="[1,1,1,1]",
                 downsample_list="[True,True,True,True]"
        )[0]
        bs = 2
        x = torch.ones(bs, 28)
        with self.assertRaises(ValueError) as context:
            model(x)


if __name__ == "__main__":
    unittest.main()
