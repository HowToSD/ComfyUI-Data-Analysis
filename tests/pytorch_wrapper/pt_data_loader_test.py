import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.ptv_dataset import PtvDataset
from pytorch_wrapper.ptv_transforms_to_tensor import PtvTransformsToTensor
from pytorch_wrapper.pt_data_loader import PtDataLoader

class TestPtDataLoader(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.dataset_node = PtvDataset()
        self.compose_node = PtvTransformsToTensor()
        self.data_loader_node = PtDataLoader()

    def test_with_transform(self):
        """Tests with transform"""
        bs = 2
        transform = self.compose_node.f()[0]
        dataset = self.dataset_node.f("MNIST",
                    True, # download
                    "", # root
                    '{"train": True}',
                    transform=transform)[0]
        train_data = self.data_loader_node.f(
            dataset=dataset,
            batch_size=bs,
            shuffle=True,
            parameters='{"num_workers":1}'
        )[0]

        x, y = next(iter(train_data))
        self.assertEqual(x.size(), torch.Size([bs, 1, 28, 28]))
        self.assertEqual(y.size(), torch.Size([bs]))


if __name__ == "__main__":
    unittest.main()
