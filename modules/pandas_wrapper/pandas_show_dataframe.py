"""
This code is based on
https://github.com/pythongosssss/ComfyUI-Custom-Scripts/blob/main/py/show_text.py

See credit/credit.md for the full license.
"""
from io import StringIO
import pandas as pd

class PandasShowDataFrame:
    """
    Displays a Pandas DataFrame as text.

    category: Display data
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "dataframe": ("DATAFRAME", {})
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",
                "extra_pnginfo": "EXTRA_PNGINFO",
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    FUNCTION = "notify"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)

    CATEGORY = "Data Analysis"

    def notify(self, dataframe, unique_id=None, extra_pnginfo=None):
        text = None
        if unique_id is not None and extra_pnginfo is not None:
            if not isinstance(extra_pnginfo, list):
                print("Error: extra_pnginfo is not a list")
            elif (
                not isinstance(extra_pnginfo[0], dict)
                or "workflow" not in extra_pnginfo[0]
            ):
                print("Error: extra_pnginfo[0] is not a dict or missing 'workflow' key")
            else:
                df = dataframe[0]
                text = [str(df)]  # wrap in list
                workflow = extra_pnginfo[0]["workflow"]
                node = next(
                    (x for x in workflow["nodes"] if str(x["id"]) == str(unique_id[0])),
                    None,
                )
                if node:
                    node["widgets_values"] = text  # [text]
        else:
            print("unique_id or extra_pnginfo is None.")

        # "ui" value is the one that is shown on the node UI.
        # Note that "ui" return value needs to a list of strings.
        return {"ui": {"text": text},
                "result": (text,)}
