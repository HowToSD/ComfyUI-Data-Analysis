"""
This unit test requires the dog_and_cat dataset to be set up under
project_root/datasets/.
"""
import os
import sys
import unittest

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pytorch_wrapper.ptv_image_folder_dataset import PtvImageFolderDataset
from pytorch_wrapper.ptv_transforms_to_tensor import PtvTransformsToTensor


class TestPtvImageDataset(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PtvImageFolderDataset()
        self.compose_node = PtvTransformsToTensor()

    def test_with_tensor_transform(self):
        """Tests downloading with transform"""
        transform = self.compose_node.f()[0]
        dc = self.node.f("dog_and_cat/train",
                    transform=transform)[0]
        expected_classes = ["cats", "dogs"]
        expected_dict = [("cats", 0), ("dogs", 1)]
        for i, c in enumerate(dc.classes):
            self.assertEqual(c, expected_classes[i])

        for i, (k, w) in enumerate(dc.class_to_idx.items()):
            self.assertEqual(k, expected_dict[i][0])
            self.assertEqual(w, expected_dict[i][1])

        # Read data
        data = next(iter(dc))

        # Check data shape
        self.assertEqual(data[0].size(), (3, 512, 512))

        # Check class
        self.assertTrue(data[1] == 0)  # cat


if __name__ == "__main__":
    unittest.main()
