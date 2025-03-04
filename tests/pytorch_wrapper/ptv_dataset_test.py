import os
import sys
import unittest

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pytorch_wrapper.ptv_dataset import PtvDataset
from pytorch_wrapper.ptv_transforms_to_tensor import PtvTransformsToTensor

class TestPtvDataset(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PtvDataset()
        self.compose_node = PtvTransformsToTensor()

    def test_no_transform(self):
        """Tests downloading without transform"""
        self.node.f("MNIST",
                    True, # download
                    "", # root
                    '{"train": True}',
                    transform=None)

    def test_with_transform(self):
        """Tests downloading with transform"""
        transform = self.compose_node.f()[0]
        self.node.f("MNIST",
                    True, # download
                    "", # root
                    '{"train": False}',
                    transform=transform)


if __name__ == "__main__":
    unittest.main()
