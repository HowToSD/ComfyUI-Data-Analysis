from typing import Any, Dict
import json

class CDAJSONCreate:
    """
    CDA JSON Create:
    Creates a serialized JSON object using values entered in the text field.

    category: IO
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `create` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "data": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES: tuple = ("STRING",)
    FUNCTION: str = "create"
    CATEGORY: str = "Data Analysis"

    def create(self, data: str) -> tuple:
        """
        creating a serialized JSON object using values entered in the text field.
        
        Args:
            data (str): String value in the text field.

        Returns:
            tuple: A tuple containing a JSON string representation of the DataFrame.
        """
        # Convert to JSON
        json_obj = json.loads(data)

        # Serialize to a string
        result_jsons = json.dumps(json_obj)

        return (result_jsons,)

