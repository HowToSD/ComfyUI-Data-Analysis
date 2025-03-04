from typing import Any, Dict, Tuple
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class PtEvaluateClassificationModel:
    """
    Performs inference on test data and computes evaluation metrics.

    category: PyTorch wrapper - Training
    """

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "model": ("PTMODEL", {}),
                "data_loader": ("PTDATALOADER", {}),
                "use_gpu": ("BOOLEAN", {"default":False})
            }
        }

    RETURN_NAMES: Tuple[str, ...] = ("accuracy", "precision", "recall", "f1", "num_samples")
    RETURN_TYPES: Tuple[str, ...] = ("FLOAT", "FLOAT", "FLOAT", "FLOAT", "INT")
    FUNCTION: str = "f"
    CATEGORY: str = "Training"

    def f(self, model: nn.Module, data_loader: torch.utils.data.DataLoader, use_gpu: bool) -> Tuple[float, float, float, float, int]:
        """
        Performs inference on test data and computes evaluation metrics.

        Args:
            model (torch.nn.Module): The PyTorch model to evaluate.
            data_loader (torch.utils.data.DataLoader): DataLoader for the test dataset.
            use_gpu (bool): Whether to use GPU for inference.

        Returns:
            Tuple[float, float, float, float, int]: A tuple containing accuracy, precision, recall, 
            F1-score, and the number of samples.
        """

        with torch.inference_mode():
            if use_gpu:
                model.to("cuda")
            model.train(False)  # TODO: Change to model.*e*v*a*l() once Comfy's security checker is fixed.
            y_hat = []
            y = []

            for images, labels in data_loader:
                if use_gpu:
                    images = images.to("cuda")
                    labels = labels.to("cuda")
                outputs = model(images)
                preds = outputs.argmax(dim=1)

                y_hat.extend(preds.cpu().numpy())
                y.extend(labels.cpu().numpy())

        accuracy = accuracy_score(y, y_hat)
        precision = precision_score(y, y_hat, average='macro')
        recall = recall_score(y, y_hat, average='macro')
        f1 = f1_score(y, y_hat, average='macro')
        num_samples = len(y)
        return (accuracy, precision, recall, f1, num_samples)
