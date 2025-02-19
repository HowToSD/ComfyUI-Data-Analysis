"""
This code is based on
https://github.com/pythongosssss/ComfyUI-Custom-Scripts/blob/main/py/show_text.py

See credit/credit.md for the full license.
"""
from typing import Any, Dict
from io import StringIO
import pandas as pd

class PandasSaveCSV:
    """
    Pandas Save CSV:
    Saves a PandasDataFrame to a CSV file.

    category: IO
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "dataframe": ("DATAFRAME", {}),
                "file_path": ("STRING", {"multiline": False})
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",
                "extra_pnginfo": "EXTRA_PNGINFO",
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    FUNCTION = "save_csv"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)

    CATEGORY = "Data Analysis"

    def save_csv(self, dataframe, file_path=None, unique_id=None, extra_pnginfo=None):
        text = None
        if unique_id is not None and extra_pnginfo is not None:
            if not isinstance(extra_pnginfo, list):
                print("Error: extra_pnginfo is not a list")
            elif (
                not isinstance(extra_pnginfo[0], dict)
                or "workflow" not in extra_pnginfo[0]
            ):
                print("Error: extra_pnginfo[0] is not a dict or missing 'workflow' key")
            elif file_path is None or len(file_path) == 0:
                print("Error: file path is not specified")
            else:
                df = dataframe[0]
                df.to_csv(path_or_buf=file_path[0])  # Save as CSV
                text = [str(df)]  # wrap in list
                workflow = extra_pnginfo[0]["workflow"]
                node = next(
                    (x for x in workflow["nodes"] if str(x["id"]) == str(unique_id[0])),
                    None,
                )
                if node:
                    node["widgets_values"] = [text]
        else:
            print("unique_id or extra_pnginfo is None.")
        return {"ui": {"text": text}, "result": (text,)}
