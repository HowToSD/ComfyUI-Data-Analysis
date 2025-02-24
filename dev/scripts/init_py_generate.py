"""
Generate top level __init__.py.

Run this at the project root if you add a new .py file.

To skip the python file from included, put
```
pragma: skip_doc
```
in the docstring for the class. This pragma is used for both node reference as well as __init__.py.
```
"""
import os
import ast
import pathlib
from typing import TypeVar

T = TypeVar("T")
MODULES_DIR = "modules"


def extract_classes_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=file_path)
    
    classes = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            docstring = ast.get_docstring(node)
            if docstring and "pragma: skip_doc" in docstring:
                continue
            classes.append(node.name)
    return classes


def format_display_name(class_name):
    result = []
    first_lower_encountered = False

    i = 0
    while i < len(class_name):
        if i > 0 and class_name[i].isupper():
            if first_lower_encountered or (i + 1 < len(class_name) and class_name[i + 1].islower()):
                result.append(" ")
            elif not first_lower_encountered and (i + 1 < len(class_name) and class_name[i + 1].isupper()):
                if i + 2 < len(class_name) and class_name[i + 2].islower():
                    result.append(" ")

        if class_name[i].islower():
            first_lower_encountered = True

        # Special case for JSON and CSV
        if class_name[i:i+4] == "JSON":
            if result and result[-1] != " ":
                result.append(" ")
            result.append("JSON")
            if i + 4 < len(class_name) and class_name[i + 4].isupper():
                result.append(" ")
            i += 3  # Skip processed letters
        elif class_name[i:i+3] == "CSV":
            if result and result[-1] != " ":
                result.append(" ")
            result.append("CSV")
            if i + 3 < len(class_name) and class_name[i + 3].isupper():
                result.append(" ")
            i += 2  # Skip processed letters
        else:
            result.append(class_name[i])
        i += 1

    # Ensure acronyms at the start are not incorrectly split (like "CD A" instead of "CDA")
    final_result = "".join(result)

    # TODO: Reduce hack below
    replace_pairs = [
        ("CD A", "CDA"),
        ("H T M L", "HTML"),
        ("MP L", "MPL"),
        ("SN S", "SNS"),
        (" N A", " NA"),
        ("Data Frame", "DataFrame"),
        ("Multi Index", "MultiIndex"),
        ("MPL Bar", "MPL Bar Chart"),
        ("MPL Line", "MPL Line Plot"),
        ("MPL Scatter", "MPL Scatter Plot"),
        ("SNS Bar", "SNS Bar Chart"),
        ("SNS Line", "SNS Line Plot"),
        ("SNS Scatter", "SNS Scatter Plot")
    ]
    for p in replace_pairs:
        final_result = final_result.replace(p[0], p[1])

    return " ".join(final_result.split())  # Remove unintended extra spaces


def discover_modules():
    module_entries = []
    for py_file in pathlib.Path(MODULES_DIR).rglob("*.py"):
        relative_path = py_file.relative_to(MODULES_DIR).with_suffix("")
        module_import_path = ".modules." + str(relative_path).replace(os.sep, ".")
        class_names = extract_classes_from_file(py_file)
        
        for class_name in class_names:
            display_name = format_display_name(class_name)
            module_entries.append((module_import_path, class_name, display_name))
    
    return module_entries


def get_class_mappings_doc():
    return """
\"\"\"
NODE_CLASS_MAPPINGS (Dict[str, Type[T]]):
    A dictionary mapping node names to their corresponding class implementations.
\"\"\"
"""


def get_display_name_mappings_doc():
    return """
\"\"\"
NODE_DISPLAY_NAME_MAPPINGS (Dict[str, str]):
    A dictionary mapping node names to user-friendly display names.
\"\"\"
"""


def get_license_doc():
    return """
\"\"\"
Below two lines were taken from:
https://github.com/pythongosssss/ComfyUI-Custom-Scripts/blob/main/__init__.py
See credit/credit.md for the full license.
\"\"\"
"""


def generate_init_content(import_statements, node_class_mappings, node_display_name_mappings):
    return f"""# This file is auto-generated. Do not edit manually.
from typing import Dict, Type, TypeVar
{os.linesep.join(import_statements)}
T = TypeVar("T")

{get_class_mappings_doc()}
NODE_CLASS_MAPPINGS: Dict[str, Type[T]] = {{
{os.linesep.join(node_class_mappings)}
}}

{get_display_name_mappings_doc()}
NODE_DISPLAY_NAME_MAPPINGS: Dict[str, str] = {{
{os.linesep.join(node_display_name_mappings)}
}}

{get_license_doc()}
WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
"""


def generate_init():
    module_entries = discover_modules()
    
    import_statements = sorted([f"from {entry[0]} import {entry[1]}" for entry in module_entries])
    node_class_mappings = sorted([f'    "{entry[1]}": {entry[1]},' for entry in module_entries])
    node_display_name_mappings = sorted([f'    "{entry[1]}": "{entry[2]}",' for entry in module_entries])
    
    template = generate_init_content(import_statements, node_class_mappings, node_display_name_mappings)
    
    with open("__init__.py", "w", encoding="utf-8") as f:
        f.write(template)


if __name__ == "__main__":
    generate_init()
