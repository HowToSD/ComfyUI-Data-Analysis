"""
Almost all of this code was taken from
https://github.com/pythongosssss/ComfyUI-Custom-Scripts/blob/main/py/show_text.py

See credit/credit.md for the full license.
"""
from typing import List
import torch


class PtShowSize:
    """
    Displays PyTorch Size object as a string.

    category: Display data
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "size": ("PTSIZE", {}),
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

    MAX_NUM_ELEMENTS_TO_DISPLAY = 100

    def notify(self, size: torch.Size, unique_id=None, extra_pnginfo=None):
        text = str(size[0])

        if unique_id is not None and extra_pnginfo is not None:
            if not isinstance(extra_pnginfo, list):
                print("Error: extra_pnginfo is not a list")
            elif (
                not isinstance(extra_pnginfo[0], dict)
                or "workflow" not in extra_pnginfo[0]
            ):
                print("Error: extra_pnginfo[0] is not a dict or missing 'workflow' key")
            else:
                workflow = extra_pnginfo[0]["workflow"]
                node = next(
                    (x for x in workflow["nodes"] if str(x["id"]) == str(unique_id[0])),
                    None,
                )
                if node:
                    node["widgets_values"] = [text]
        else:
            print("unique_id or extra_pnginfo is None.")
        return {"ui": {"text": [text]}, "result": ([text],)}
