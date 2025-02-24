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
