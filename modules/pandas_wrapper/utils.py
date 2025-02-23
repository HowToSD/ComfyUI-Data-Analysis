from typing import List, Union
import json
import numpy as np
import pandas as pd
import pandas as pd


def column_labels_string_to_list(dataframe: pd.DataFrame, s: str) -> List[Union[str, int]]:
    """
    Converts a comma-separated string of column labels into a list of valid column names for a Pandas DataFrame.

    This function ensures that each label in the input string corresponds to an existing column in the DataFrame.
    If a label is a numeric string and corresponds to an integer column name, it will be converted to an integer.
    If a column name does not exist in the DataFrame, a ValueError is raised.

    Args:
        dataframe (pd.DataFrame): The DataFrame to validate column names against.
        s (str): A comma-separated string representing column labels.

    Returns:
        List[Union[str, int]]: A list of valid column labels.

    Raises:
        ValueError: If any label in `s` does not match an existing column name.
    """
    columns = [col.strip() for col in s.split(",")]
    valid_columns = set(dataframe.columns)  # Use a set for faster lookups
    output_columns = []

    for c in columns:
        if c in valid_columns:
            output_columns.append(c)
        else:
            try:
                numeric_c = int(c)
                if numeric_c in valid_columns:
                    output_columns.append(numeric_c)
                else:
                    raise ValueError(f"Column '{c}' not found in the DataFrame.")
            except ValueError:
                raise ValueError(f"Column '{c}' not found in the DataFrame.")

    return output_columns


def series_to_jsons(series: pd.Series) -> str:
    """
    Converts a pandas Series to a JSON string.

    Args:
        series (pd.Series): The pandas Series to convert.

    Returns:
        str: A JSON string representing the Series, including its data, index, and name.
    """
    array = [x.item() if hasattr(x, "item") else x for x in series.array.tolist()]  # Convert NumPy types to Python types
    index = [x.item() if hasattr(x, "item") else x for x in series.index.tolist()]  # Convert index to Python types
    name = series.name

    d = {"array": array, "index": index, "name": name}

    return json.dumps(d, cls=NpEncoder)  # See license for NpEncoder(json.JSONEncoder) below

def jsons_to_series(s: str) -> pd.Series:
    """
    Convert a JSON string to a pandas Series.

    Args:
        s (str): The JSON string representing the Series.

    Returns:
        pd.Series: The reconstructed pandas Series.
    """
    d = json.loads(s)
    return pd.Series(data=d["array"], index=d["index"], name=d["name"])

def index_to_jsons(index: pd.Index) -> str:
    """
    Convert a pandas Index to a JSON string.

    Args:
        index (pd.Index): The pandas Index to convert.

    Returns:
        str: A JSON string representing the Index, including its values and name.
    """
    index_list = [x.item() if hasattr(x, "item") else x for x in index.tolist()]  # Convert NumPy types to Python types
    index_name = index.name  # Preserve index name

    d = {"index": index_list, "name": index_name}

    return json.dumps(d)

def jsons_to_index(s: str) -> pd.Index:
    """
    Convert a JSON string to a pandas Index.

    Args:
        s (str): The JSON string representing the Index.

    Returns:
        pd.Index: The reconstructed pandas Index.
    """
    d = json.loads(s)
    return pd.Index(d["index"], name=d.get("name"))  # Restore index with name


class NpEncoder(json.JSONEncoder):
    """
    Source: https://stackoverflow.com/questions/50916422/python-typeerror-object-of-type-int64-is-not-json-serializable
    Author: Jie Yang, Tommy
    Licensed under CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)

    pragma: skip_doc
    """
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.bool_):
            return bool(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)


