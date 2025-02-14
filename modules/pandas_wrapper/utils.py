import json
import pandas as pd

def series_to_jsons(series: pd.Series) -> str:
    """
    Convert a pandas Series to a JSON string.

    Args:
        series (pd.Series): The pandas Series to convert.

    Returns:
        str: A JSON string representing the Series, including its data, index, and name.
    """
    array = [x.item() if hasattr(x, "item") else x for x in series.tolist()]  # Convert NumPy types to Python types
    index = [x.item() if hasattr(x, "item") else x for x in series.index.tolist()]  # Convert index to Python types
    name = series.name

    d = {"array": array, "index": index, "name": name}

    return json.dumps(d)

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
