import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pytorch_wrapper.ptn_linear_model import PtnLinearModel  # Updated import to PtnLinear


class TestPtnLinearModel(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.model_node = PtnLinearModel()
        self.model = self.model_node.f(
            "784,180,42,10",  # input dim for first layer, output dim for each layer
            "True,True,True", # bias
            3  # num layers
        )[0]  # HINADA note: Using roughly 0.23x ratio for reduction

    def test_forward(self):
        x = torch.ones(4, 28, 28)
        out = self.model(x)
        self.assertEqual(out.size(), torch.Size([4, 10]))


if __name__ == "__main__":
    unittest.main()
