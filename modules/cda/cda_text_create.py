from typing import Any, Dict


class CDATextCreate:
    """
    CDA Text Create:
    Creates a Python String using a value entered in a multi-line text field.

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
        creating a Python String for the text entered in the text field.
        
        Args:
            data (str): String value in the text field.

        Returns:
            tuple: A tuple containing the string converted from the text.
        """
        return (data,)

