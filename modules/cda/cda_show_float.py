"""
This code is based on
https://github.com/pythongosssss/ComfyUI-Custom-Scripts/blob/main/py/show_text.py

See credit/credit.md for the full license.
"""
import sys


class CDAShowFloat:
    """
    CDAShowFloat:
    Displays a floating-point number as text.

    category: Display data
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "float_scalar": ("FLOAT", {"default": 0.0, "min": sys.float_info.min, "max": sys.float_info.max})
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

    def notify(self, float_scalar, unique_id=None, extra_pnginfo=None):
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
                float_val = float_scalar[0]
                text = [str(float_val)]  # wrap in list
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
