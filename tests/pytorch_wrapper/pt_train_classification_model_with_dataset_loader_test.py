import os
import sys
import unittest
import torch
import torch.nn as nn

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.ptn_linear_model import PtnLinearModel
from pytorch_wrapper.pto_adam import PtoAdam
from pytorch_wrapper.ptv_dataset_loader import PtvDatasetLoader
from pytorch_wrapper.pt_train_classification_model import PtTrainClassificationModel
from pytorch_wrapper.pt_save_model import PtSaveModel

 
class TestPtTrainModelWithDatasetLoader(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.dataset_loader_node = PtvDatasetLoader()
        self.train_loader = self.dataset_loader_node.f(
                    "MNIST",
                    True, # download
                    "", # root
                    batch_size=128,
                    shuffle=True,
                    dataset_parameters='{"train": True}',
                    load_parameters='{"num_workers":1}'
        )[0]
        self.model_node = PtnLinearModel()
        self.model = self.model_node.f(
            "784,180,42,10",  # input dim for first layer, output dim for each layer
            "True,True,True", # bias
            3  # num layers
        )[0]

        self.optimizer = PtoAdam().f(self.model, 0.001, 0.9, 0.999)[0]
        self.trainer = PtTrainClassificationModel()
        self.save_model = PtSaveModel()

    def test_1(self):
        epochs = 2
        trained_model = self.trainer.f(self.model, self.train_loader, self.optimizer,
                       epochs, # epochs
                       use_gpu=True)[0]
        self.save_model.f(trained_model, f"mnist_{epochs}_epochs.pt")


if __name__ == "__main__":
    unittest.main()
