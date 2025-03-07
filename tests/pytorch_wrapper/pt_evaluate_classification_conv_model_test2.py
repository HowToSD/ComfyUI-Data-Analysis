import os
import sys
import unittest
import torch
import torch.nn as nn

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pytorch_wrapper.ptn_conv_model import PtnConvModel
from pytorch_wrapper.ptv_image_folder_dataset import PtvImageFolderDataset
from pytorch_wrapper.ptv_transforms_resize import PtvTransformsResize
from pytorch_wrapper.pt_data_loader import PtDataLoader
from pytorch_wrapper.pt_evaluate_classification_model import PtEvaluateClassificationModel
from pytorch_wrapper.pt_load_model import PtLoadModel
 
class TestPtEvaluate(unittest.TestCase):

    @unittest.skipIf(os.getenv("RUN_SKIPPED_TESTS") != "1", "Skipping unless explicitly enabled")
    def setUp(self):
        """Set up test instance."""
        # Transform
        compose_node = PtvTransformsResize()
        transform = compose_node.f(256, 256)[0]
        
        # Dataset
        self.node = PtvImageFolderDataset()
        dataset = self.node.f("dog_and_cat/val",
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
        self.model_node = PtnConvModel()
        self.model = self.model_node.f(
                 input_dim="(3, 256, 256)",
                 penultimate_dim=0,
                 output_dim=2,
                 channel_list="[32,64,128,256,512]", # To 128, 64, 32, 16, 8
                 kernel_size_list="[3,3,3,3,3]",
                 padding_list="[1,1,1,1,1]",
                 downsample_list="[True,True,True,True,True]"
        )[0]

        # Load weights
        self.load_model = PtLoadModel()
        epochs = 20
        self.loaded_model = self.load_model.f(self.model,f"dog_cat_{epochs}_epochs_conv.pt")

        # Instantiates evaluation node
        self.evaluate = PtEvaluateClassificationModel()

    @unittest.skipIf(os.getenv("RUN_SKIPPED_TESTS") != "1", "Skipping unless explicitly enabled")
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
        self.assertTrue(accuracy > 0.7)
        self.assertEqual(num_samples, 300)


if __name__ == "__main__":
    unittest.main()
