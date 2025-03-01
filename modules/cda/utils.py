from typing import Dict, Any
from typing import Optional, Tuple, Union

def str_to_number(s: str) -> Union[int, float]:
    """
    Converts a string representation of a number to an integer or float.

    Args:
        s (str): The string to convert.

    Returns:
        Union[int, float]: The converted number, either as an `int` if no decimal point is present or as a `float` otherwise.

    Raises:
        ValueError: If the input string is empty.
    """
    if s:
        if "." in s:
            return float(s)
        return int(s)
    raise ValueError("Input string cannot be empty.")


def str_to_number_with_default(s: str, n: Union[int, float]) -> Union[int, float]:
    """
    Converts a string representation of a number to an integer or float, with a fallback default value.

    Args:
        s (str): The string to convert.
        n (Union[int, float]): The default value to return if `s` is empty.

    Returns:
        Union[int, float]: The converted number if `s` is non-empty, otherwise `n`.
    """
    return str_to_number(s) if s else n


def python_dict_first_value_len(d: Dict[Any, Any]) -> int:
    r"""
    Computes the length of the first value in a dictionary.

    - If the first value is a `list`, returns its length.
    - If the first value is a `dict`, returns the number of keys in the dictionary.
    - Otherwise, returns `1` for scalar values.

    Args:
        d (Dict[Any, Any]): A dictionary where the first value's length will be computed.

    Returns:
        int: The computed length based on the type of the first value.

    Raises:
        ValueError: If `d` is `None` or empty.
    """
    if not d:
        raise ValueError("Input dictionary is None or empty.")

    first_value = next(iter(d.values()))  # Get the first value

    if isinstance(first_value, list):
        return len(first_value)
    elif isinstance(first_value, dict):
        return len(first_value.keys())  # Return the number of keys in the dictionary
    else:
        return 1  # Scalar case (int, float, str, etc.)
