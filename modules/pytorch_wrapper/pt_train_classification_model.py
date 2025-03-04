from typing import Any, Dict, Optional, Tuple
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

class PtTrainClassificationModel:
    """
    Trains a classification model using a given dataset, optimizer, and number of epochs.

    category: PyTorch wrapper - Training
    """

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types required for training the model.

        Returns:
            Dict[str, Any]: A dictionary specifying required and optional input types.
        """
        return {
            "required": {
                "model": ("PTMODEL", {}),
                "train_loader": ("PTDATALOADER", {}),
                "optimizer": ("PTOPTIMIZER", {}),
                "epochs": ("INT", {"default":1, "min":1, "max":1e6}),
                "use_gpu": ("BOOLEAN", {"default":False})
            },
            "optional": {
                "val_loader": ("PTDATALOADER", {}),
            }
        }

    RETURN_NAMES: tuple = ("Model", "train loss", "val loss")
    RETURN_TYPES: tuple = ("PTMODEL","TENSOR","TENSOR")
    FUNCTION: str = "f"
    CATEGORY: str = "Training"

    @classmethod
    def IS_CHANGED(cls, **kw):
        return float("NaN")

    def f(self, model: nn.Module, 
          train_loader: torch.utils.data.DataLoader, 
          optimizer: torch.optim.Optimizer, 
          epochs: int, 
          use_gpu: bool, 
          val_loader: Optional[torch.utils.data.DataLoader] = None) -> Tuple[nn.Module, torch.Tensor, torch.Tensor]:
        """
        Trains a classification model.

        Args:
            model (torch.nn.Module): The PyTorch model to be trained.
            train_loader (torch.utils.data.DataLoader): DataLoader containing the training dataset.
            optimizer (torch.optim.Optimizer): Optimizer used for training.
            epochs (int): Number of training epochs.
            use_gpu (bool): Whether to use GPU for training.
            val_loader (Optional[torch.utils.data.DataLoader]): DataLoader for validation dataset (optional).

        Returns:
            Tuple[torch.nn.Module, torch.Tensor, torch.Tensor]: A tuple containing the trained model, 
            training loss history, and validation loss history.
        """

        with torch.inference_mode(False):
            train_loss = []
            val_loss = []
            if use_gpu:
                model.to("cuda")

            loss_function = nn.CrossEntropyLoss()  # mean loss

            # Train the model
            for epoch in range(epochs):
                model.train()
                total_loss = 0
                total_samples = len(train_loader.dataset)
                for images, labels in train_loader:
                    if use_gpu:
                        images = images.to("cuda")
                        labels = labels.to("cuda")
                    optimizer.zero_grad()
                    outputs = model(images)
                    loss = loss_function(outputs, labels)
                    loss.backward()
                    optimizer.step()
 
                    batch_size = labels.size(0)
                    batch_loss = loss.item() * batch_size
                    total_loss += batch_loss

                epoch_loss = total_loss / total_samples
                
                print(f"Epoch (train) {epoch+1}/{epochs}, Loss: {epoch_loss:.4f}")
                train_loss.append(epoch_loss)
                
                if val_loader:
                    with torch.no_grad():
                        model.train(False)  # TODO: Change to model.*e*v*a*l() once Comfy's security checker is fixed.
                        total_loss = 0
                        total_samples = len(val_loader.dataset)
                        for images, labels in val_loader:
                            if use_gpu:
                                images = images.to("cuda")
                                labels = labels.to("cuda")
                            outputs = model(images)
                            loss = loss_function(outputs, labels)
                            batch_size = labels.size(0)
                            batch_loss = loss.item() * batch_size
                            total_loss += batch_loss

                        epoch_loss = total_loss / total_samples
                        print(f"Epoch (val) {epoch+1}/{epochs}, Loss: {epoch_loss:.4f}")
                        val_loss.append(epoch_loss)

            if use_gpu:
                model.to("cpu")

            return (model, 
                    torch.tensor(train_loss, dtype=torch.float32), 
                    torch.tensor(val_loss, dtype=torch.float32))