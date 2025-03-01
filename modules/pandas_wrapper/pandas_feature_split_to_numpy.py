from typing import Any, Dict
import pandas as pd
import numpy as np

class PandasFeatureSplitToNumpy:
    """
    Splits a Pandas DataFrame into feature Numpy ndarray and label Numpy ndarray.
    If output_1d_label is set, label will be output as a 1d array instead of a 2d array.

    As shown in the below screenshot, this node can replace multiple nodes that are used to split Pandas DataFrame into two DataFrames, convert to NumPy, then squeeze the label data. 
    ![Pandas Feature Split To Numpy](../images/pandas_feature_split.png)

    category: Transformation
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
                "dataframe": ("DATAFRAME", {}),
                "label_integer_position": ("INT", {"default": -1, "min": -10, "max": 1024}),
                "output_1d_label": ("BOOLEAN", {"default": True})
            }
        }

    RETURN_TYPES: tuple = ("NDARRAY", "NDARRAY")
    RETURN_NAMES: tuple = ("feature", "label")

    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame,
        label_integer_position: int,
        output_1d_label: bool) -> tuple:
        """
        Splits a Pandas DataFrame into feature Numpy ndarray and label Numpy ndarray.

        Args:
            dataframe (pd.DataFrame): The DataFrame to split.
            label_integer_position (int): The column integer position of the label.
            output_1d_label (bool): If output_1d_label is set, label will be output as a 1d array instead of a 2d array.

        Returns:
            tuple: A tuple containing the feature and label arrays.
        """
        num_columns = dataframe.shape[1]

        if label_integer_position < 0:
            label_integer_position += num_columns

        # Validate label_integer_position
        if label_integer_position >= num_columns:
            raise ValueError(f"label_integer_position {label_integer_position} is out of range for dataframe with {num_columns} columns.")

        # Extract features
        np_left = dataframe.iloc[:, :label_integer_position].to_numpy()
        np_right = dataframe.iloc[:, label_integer_position + 1:].to_numpy() if label_integer_position < num_columns - 1 else np.empty((len(dataframe), 0))
        np_features = np.hstack([np_left, np_right]) if np_right.shape[1] > 0 else np_left

        # Extract label
        np_label = dataframe.iloc[:, label_integer_position].to_numpy()
        if output_1d_label:
            np_label = np_label.ravel()

        return (np_features, np_label)
