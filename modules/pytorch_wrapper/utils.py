import os
import ast
from typing import Optional, Tuple, Union
import torch

DTYPE_MAPPING = {
    "float32": torch.float32,
    "float16": torch.float16,
    "bfloat16": torch.bfloat16,
    "float64": torch.float64,
    "uint8": torch.uint8,
    "int8": torch.int8,
    "int16": torch.int16,
    "int32": torch.int32,
    "int64": torch.int64,
    "bool": torch.bool
}


def get_resource_full_path(resource_name: str, resource_path: str) -> str:
    """
    Resolves the absolute path to a resource file within the "resources" directory and 
    ensures that the directory exists.

    Args:
        resource_path (str): The path to the resource file. If the path is a relative path,
        the path is considered relative to the `resource` directory of this extension.

    Returns:
        str: The absolute path to the resource file.
    """
    if os.path.isabs(resource_path):
        resource_full_path = resource_path
    else:
        resource_full_path = os.path.realpath(
            os.path.join(os.path.dirname(__file__), "..", "..", resource_name, resource_path))
        resource_dir = os.path.dirname(resource_full_path)
        if os.path.exists(resource_dir) is False:
            os.makedirs(resource_dir)
    return resource_full_path


def get_model_full_path(model_path: str) -> str:
    """
    Resolves the absolute path to a model file within the "models" directory and 
    ensures that the directory exists.

    Args:
        model_path (str): The path to the model file. If the path is a relative path,
        the path is considered relative to the `models` directory of this extension.

    Returns:
        str: The absolute path to the model file.
    """
    return get_resource_full_path("models", model_path)


def get_dataset_full_path(dataset_path: str) -> str:
    """
    Resolves the absolute path to the datasete within the "datasets" directory and 
    ensures that the directory exists.

    Args:
        dataset_path (str): The path to the dataset file. If the path is a relative path,
        the path is considered relative to the `datasets` directory of this extension.

    Returns:
        str: The absolute path to the dataset file.
    """
    return get_resource_full_path("datasets", dataset_path)


def str_to_dim(dim: str) -> Optional[Union[int, Tuple[int, ...]]]:
    """
    Converts a string representation of a dimension into an integer or a tuple of integers.

    Args:
        dim (str): A string representing an integer or a tuple of integers.

    Returns:
        Optional[Union[int, Tuple[int, ...]]]: 
            - An integer if the input represents a single integer.
            - A tuple of integers if the input represents a list or tuple.
            - None if the input is empty.

    Raises:
        ValueError: If the parsed value is not an integer or a tuple of integers.
    """
    if dim:
        # Convert string to an integer, list, or tuple of integers
        parsed_dim = ast.literal_eval(dim)

        # Convert list to tuple
        if isinstance(parsed_dim, list):
            parsed_dim = tuple(parsed_dim)

        # Ensure the parsed dim is valid
        if not isinstance(parsed_dim, (int, tuple)) or (
            isinstance(parsed_dim, tuple) and not all(isinstance(i, int) for i in parsed_dim)
        ):
            raise ValueError(f"Invalid format for dim: {parsed_dim}. Must be an integer or a tuple of integers.")
        
        return parsed_dim

    return None

