import os
import sys
import unittest
import torch
import torch.nn as nn

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.ptn_conv_model import PtnConvModel
from pytorch_wrapper.pto_adam import PtoAdam
from pytorch_wrapper.ptv_image_folder_dataset import PtvImageFolderDataset
from pytorch_wrapper.ptv_transforms_resize import PtvTransformsResize
from pytorch_wrapper.pt_data_loader import PtDataLoader
from pytorch_wrapper.pt_train_classification_model import PtTrainClassificationModel
from pytorch_wrapper.pt_save_model import PtSaveModel

 
class TestPtTrainConvModel2(unittest.TestCase):

    @unittest.skipIf(os.getenv("RUN_SKIPPED_TESTS") != "1", "Skipping unless explicitly enabled")
    def setUp(self):
        """Set up test instance."""
        compose_node = PtvTransformsResize()
        transform = compose_node.f(256, 256)[0]
        self.node = PtvImageFolderDataset()
        train_dataset = self.node.f("dog_and_cat/train",
                    transform=transform)[0]
        train_data_loader_node = PtDataLoader()
        val_dataset = self.node.f("dog_and_cat/val",
                    transform=transform)[0]
        val_data_loader_node = PtDataLoader()
        self.train_loader = train_data_loader_node.f(
            dataset=train_dataset,
            batch_size=32,
            shuffle=True,
            parameters='{"num_workers":1}'
        )[0]
        self.val_loader = val_data_loader_node.f(
            dataset=val_dataset,
            batch_size=32,
            shuffle=True,
            parameters='{"num_workers":1}'
        )[0]

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

        self.optimizer = PtoAdam().f(self.model, 0.0001, 0.9, 0.999)[0]
        self.trainer = PtTrainClassificationModel()
        self.save_model = PtSaveModel()

    @unittest.skipIf(os.getenv("RUN_SKIPPED_TESTS") != "1", "Skipping unless explicitly enabled")
    def test_1(self):
        epochs = 20
        trained_model = self.trainer.f(self.model, self.train_loader, self.optimizer,
                       epochs, # epochs
                       use_gpu=True,
                       val_loader=self.val_loader)[0]
        self.save_model.f(trained_model, f"dog_cat_{epochs}_epochs_conv.pt")


if __name__ == "__main__":
    unittest.main()
