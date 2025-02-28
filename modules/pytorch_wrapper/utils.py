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

