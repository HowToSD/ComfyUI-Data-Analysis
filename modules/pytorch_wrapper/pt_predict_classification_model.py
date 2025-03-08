from typing import Any, Dict, Tuple
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class PtPredictClassificationModel:
    """
    Performs inference on input data.

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
                "inputs": ("TENSOR", {}),
                "class_id_to_name_map": ("PYDICT", {}),
                "use_gpu": ("BOOLEAN", {"default":False})
            }
        }

    RETURN_NAMES: Tuple[str, ...] = ("class_name", "class_id", "probability")
    RETURN_TYPES: Tuple[str, ...] = ("STRING", "INT", "FLOAT")
    FUNCTION: str = "f"
    CATEGORY: str = "Training"

    def f(self, model: nn.Module,
          inputs: torch.Tensor,
          class_id_to_name_map: Dict,
          use_gpu: bool) -> Tuple[str, int, float]:
        """
        Performs inference on test data and computes evaluation metrics.

        Args:
            model (torch.nn.Module): The PyTorch model to evaluate.
            inputs (torch.Tensor): Input image to predict the class for.
            class_id_to_name_map (Dict): A Python dictionary contains the mapping of
                class ID to class name.
            use_gpu (bool): Whether to use GPU for inference.

        Returns:
            Tuple[str, int, float]: A tuple containing "class_name", "class_id", "probability".
        """

        with torch.inference_mode():
            if use_gpu:
                model.to("cuda")
            model.train(False)  # TODO: Change to model.*e*v*a*l() once Comfy's security checker is fixed.
            x = torch.unsqueeze(inputs, 0)
            if use_gpu:
               x = x.to("cuda")
            outputs = model(x)
            class_id = outputs.argmax(dim=1)[0].detach().cpu().item()
            prob = F.softmax(outputs, dim=1)[0][class_id].detach().cpu().item()
            class_name = class_id_to_name_map[class_id]

        return (class_name, class_id, prob)
