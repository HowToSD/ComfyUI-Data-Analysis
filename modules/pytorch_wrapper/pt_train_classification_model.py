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
            train_loss = list()
            val_loss = list()

            loss_function = nn.CrossEntropyLoss(reduction="sum")

            # Train the model
            for epoch in range(epochs):
                if use_gpu:
                    model.to("cuda")
                model.train()
                total_loss = 0

                for images, labels in train_loader:
                    if use_gpu:
                        images = images.to("cuda")
                        labels = labels.to("cuda")
                    optimizer.zero_grad()
                    outputs = model(images)
                    loss = loss_function(outputs, labels)
                    loss.backward()
                    optimizer.step()
                    total_loss += loss.item()
                epoch_loss = total_loss / len(train_loader)
                print(f"Epoch (train) {epoch+1}/{epochs}, Loss: {epoch_loss:.4f}")
                train_loss.append(epoch_loss)
                
                if val_loader:
                    pass
                    with torch.no_grad():
                        model.eval()
                        total_loss = 0
                        for images, labels in val_loader:
                            if use_gpu:
                                images = images.to("cuda")
                                labels = labels.to("cuda")
                            outputs = model(images)
                            loss = loss_function(outputs, labels)
                            total_loss += loss.item()
                        epoch_loss = total_loss / len(val_loader)
                        print(f"Epoch (val) {epoch+1}/{epochs}, Loss: {epoch_loss:.4f}")
                        val_loss.append(epoch_loss)

            return (model, 
                    torch.Tensor(np.asarray(train_loss)), 
                    torch.Tensor(np.asarray(val_loss)))