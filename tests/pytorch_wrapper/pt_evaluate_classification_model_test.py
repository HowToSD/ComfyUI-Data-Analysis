import os
import sys
import unittest
import torch
import torch.nn as nn

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pytorch_wrapper.ptn_linear_model import PtnLinearModel
from pytorch_wrapper.ptv_dataset import PtvDataset
from pytorch_wrapper.ptv_transforms_to_tensor import PtvTransformsToTensor
from pytorch_wrapper.pt_data_loader import PtDataLoader
from pytorch_wrapper.pt_evaluate_classification_model import PtEvaluateClassificationModel
from pytorch_wrapper.pt_load_model import PtLoadModel
 
class TestPtEvaluate(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        # Transform
        compose_node = PtvTransformsToTensor()
        transform = compose_node.f()[0]
        
        # Dataset
        dataset_node = PtvDataset()
        dataset = dataset_node.f("FashionMNIST",
                    True, # download
                    "", # root
                    '{"train": False}',
                    transform=transform)[0]

        # Data loader
        data_loader_node = PtDataLoader()
        self.data_loader = data_loader_node.f(
            dataset=dataset,
            batch_size=32,
            shuffle=True,
            parameters='{"num_workers":1}'
        )[0]

        # Model
        self.model_node = PtnLinearModel()
        self.model = self.model_node.f(
            "784,180,42,10",  # input dim for first layer, output dim for each layer
            "True,True,True", # bias
            3  # num layers
        )[0]

        # Load weights
        self.load_model = PtLoadModel()
        epochs = 1
        self.loaded_model = self.load_model.f(self.model, f"fashion_mnist_{epochs}_epochs.pt")

        # Instntiates evaluation node
        self.evaluate = PtEvaluateClassificationModel()

    def test_evaluation(self):
        """
        Tests evaluation.  

        Note that this test requires a trained model file on the file system.
        Unit test will fail if you run this for the first time.
        Run the unit test for training to generate the weight, and re-run this unit test.
        """
        accuracy, precision, recall, f1, num_samples = \
            self.evaluate.f(self.model, self.data_loader, use_gpu=True)
        print(f"""
            accuracy: {accuracy}
            precision: {precision}
            recall: {recall}
            f1: {f1}
            Number of samples: {num_samples}
        """)
        self.assertTrue(accuracy > 0.8)
        self.assertEqual(num_samples, 10000)


if __name__ == "__main__":
    unittest.main()
