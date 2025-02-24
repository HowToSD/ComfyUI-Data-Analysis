def common_input_types():
    """
    Defines the input types for a plot function.

    Returns:
        Dict[str, Any]: A dictionary specifying required input types.
    """
    return {
        "required": {
            "dataframe": ("DATAFRAME", {}),
            "x_column_name": ("STRING", {"default": ""}),
            "y_column_name": ("STRING", {"default": ""}),
            "title": ("STRING", {"default": ""}),
            "x_axis_label": ("STRING", {"default": ""}),
            "y_axis_label": ("STRING", {"default": ""}),
            "legend_label": ("STRING", {"default": ""}),
            "x_tick_as_int": ("BOOLEAN", {"default": False}),  # To show 2002 instead of 2002.5 on x-axis
            "style": ("STRING", {"default": ""}),
            "palette": ("STRING", {"default": ""})
        }
    }

def common_input_types_y_only_bin():
    """
    Defines the input types for a plot function for types of charts that do
    not require x-series data as input, but takes bins.

    Returns:
        Dict[str, Any]: A dictionary specifying required input types.
    """
    return {
        "required": {
            "dataframe": ("DATAFRAME", {}),
            "y_column_name": ("STRING", {"default": ""}),
            "title": ("STRING", {"default": ""}),
            "y_axis_label": ("STRING", {"default": ""}),
            # "legend_label": ("STRING", {"default": ""}),
            "bins": ("INT", {"default": 10, "min": 2, "max": 200}),
            "style": ("STRING", {"default": ""}),
            "palette": ("STRING", {"default": ""})
        }
    }
