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
from pytorch_wrapper.pt_predict_classification_model import PtPredictClassificationModel
from pytorch_wrapper.pt_load_model import PtLoadModel
 
class TestPtPrediction(unittest.TestCase):

    def setUp(self):
        """Set up test instance."""
        # Transform
        compose_node = PtvTransformsResize()
        transform = compose_node.f(256, 256)[0]
        
        # Dataset
        self.node = PtvImageFolderDataset()
        self.dataset = self.node.f("dog_and_cat/val",
                    transform=transform)[0]


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
        epochs = 20
        self.load_model = PtLoadModel()
        self.loaded_model = self.load_model.f(self.model,f"dog_cat_{epochs}_epochs_conv.pt")

        # Instantiates evaluation node
        self.predict = PtPredictClassificationModel()

    def test_prediction(self):
        """
        Tests prediction.  

        Note that this test requires a trained model file on the file system.
        Unit test will fail if you run this for the first time.
        Run the unit test for training to generate the weight, and re-run this unit test.
        """
        inputs, y = next(iter(self.dataset))
        class_id_to_name_map = {0:"cat", 1:"dog"}
        class_name, class_id, prob = \
            self.predict.f(self.model, inputs, class_id_to_name_map, use_gpu=True)
        self.assertTrue(prob > 0.8)
        self.assertEqual(class_id, 0)
        self.assertEqual(class_name, "cat")

if __name__ == "__main__":
    unittest.main()
