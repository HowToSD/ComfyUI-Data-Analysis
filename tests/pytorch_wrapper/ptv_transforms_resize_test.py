import os
import sys
import unittest
import torch
from PIL import Image
import numpy as np

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pytorch_wrapper.ptv_transforms_resize import PtvTransformsResize


class TestPtvTransformsResize(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.compose_node = PtvTransformsResize()
        self.height = 128
        self.width = 128

    def test_with_transform(self):
        """Tests the transformation output."""
        transform = self.compose_node.f(self.height, self.width)[0]
        self.assertTrue(callable(transform), "Transform should be callable.")

        # Create a dummy image
        img = Image.fromarray(np.random.randint(0, 256, (256, 256, 3), dtype=np.uint8))
        transformed_img = transform(img)

        # Check output type
        self.assertIsInstance(transformed_img, torch.Tensor, "Output should be a PyTorch tensor.")

        # Check output shape
        self.assertEqual(transformed_img.shape, (3, self.height, self.width), "Output shape should match target dimensions.")

    def test_default_parameters(self):
        """Tests default transform parameters."""
        transform = self.compose_node.f(256, 256)[0]
        self.assertTrue(callable(transform), "Default transform should be callable.")


if __name__ == "__main__":
    unittest.main()
