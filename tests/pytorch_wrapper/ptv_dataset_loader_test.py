import os
import sys
import unittest
import torch
PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pytorch_wrapper.ptv_dataset_loader import PtvDatasetLoader

class TestPtDataLoader(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.dataset_loader_node = PtvDatasetLoader()

    def test1(self):
        """Tests downloading data and checks dimension"""
        bs = 2
        train_data = self.dataset_loader_node.f(
                    "MNIST",
                    True, # download
                    "", # root
                    batch_size=bs,
                    shuffle=True,
                    dataset_parameters='{"train": True}',
                    load_parameters='{"num_workers":1}'
        )[0]

        x, y = next(iter(train_data))
        self.assertEqual(x.size(), torch.Size([bs, 1, 28, 28]))
        self.assertEqual(y.size(), torch.Size([bs]))


if __name__ == "__main__":
    unittest.main()
