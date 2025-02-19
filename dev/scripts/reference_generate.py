"""
Generate node reference documents.

Run this at the project root if you update a docstring of the node source file.

To skip the python file from included in the reference, put
```
pragma: skip_doc
```
in the docstring for the class.

To use a custom node name, put the node name on the first line of the docstring for the class with ":".
e.g.
```
    CDA JSON Create:
    Creates a serialized JSON object using values entered in the text field.
```
"""
import os
import re
import ast
from collections import defaultdict
from typing import Dict, List

# Mapping for data type conversion
data_type_mapping = {
    "DATAFRAME": "DataFrame",
    "PDSERIES": "Series",
    "PDINDEX": "Index"
}

def convert_data_type(data_type: str) -> str:
    """Convert type to the required format."""
    if data_type in data_type_mapping:
        return data_type_mapping[data_type]
    return data_type.lower().capitalize()

def extract_class_info(class_def: ast.ClassDef) -> Dict[str, str]:
    """Extract class name, title, category, and docstring."""
    class_name = class_def.name
    docstring = ast.get_docstring(class_def) or ""
    
    if "pragma: skip_doc" in docstring:
        return None
    
    lines = docstring.split("\n")
    
    title = None
    category = "Miscellaneous"
    
    if len(lines) > 1 and lines[0].strip().endswith(":") and lines[0].strip()[0].isupper():
        title = lines.pop(0).strip().rstrip(":")
    
    if not title:
        title = "# " + " ".join(re.findall(r'[A-Z][a-z]*', class_name))
    else:
        title = f"# {title}"
    
    description_lines = []
    for line in lines:
        if line.strip().startswith("category:"):
            category = line.split(":", 1)[-1].strip()
        else:
            description_lines.append(line)
    
    description = "\n".join(description_lines).strip()
    
    return {"title": title, "description": description, "class_name": class_name, "first_sentence": description_lines[0] if description_lines else "", "category": category}

def extract_input_types(class_def: ast.ClassDef) -> str:
    """Extract INPUT_TYPES definition."""
    input_table = ""
    for node in class_def.body:
        if isinstance(node, ast.FunctionDef) and node.name == "INPUT_TYPES":
            for stmt in ast.walk(node):
                if isinstance(stmt, ast.Dict):
                    for key, value in zip(stmt.keys, stmt.values):
                        if isinstance(key, ast.Constant) and isinstance(value, ast.Tuple) and len(value.elts) > 0:
                            param_name = key.value
                            data_type = value.elts[0].value if isinstance(value.elts[0], ast.Constant) else ""
                            input_table += f"| {param_name} | {convert_data_type(data_type)} |\n"
    return "## Input\n| Name | Data type |\n|---|---|\n" + input_table if input_table else ""

def extract_return_types(class_def: ast.ClassDef) -> str:
    """Extract RETURN_TYPES value."""
    for node in class_def.body:
        # Look for assignment or annotated assignment (type hint) statement.
        # Node target is the RHS.
        if (
            isinstance(node, ast.Assign) and 
            any(target.id == "RETURN_TYPES" for target in node.targets if isinstance(target, ast.Name))
        ) or (
            isinstance(node, ast.AnnAssign) and 
            isinstance(node.target, ast.Name) and 
            node.target.id == "RETURN_TYPES"
        ):
            if isinstance(node.value, ast.Tuple):
                return_types = [convert_data_type(elt.value) for elt in node.value.elts if isinstance(elt, ast.Constant)]
                return "## Output\n| Data type |\n|---|\n" + "".join(f"| {rtype} |\n" for rtype in return_types)
    return ""

def process_python_file(file_path: str, output_dir: str, node_list: Dict[str, List[str]]):
    """Process a single Python file and generate corresponding Markdown."""
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=file_path)
    
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            class_info = extract_class_info(node)
            if not class_info:
                return
            
            input_section = extract_input_types(node)
            output_section = extract_return_types(node)
            category = class_info["category"]
            
            file_name = os.path.splitext(os.path.basename(file_path))[0] + ".md"
            output_path = os.path.join(output_dir, file_name)
            
            with open(output_path, "w", encoding="utf-8") as md_file:
                md_file.write(f"{class_info['title']}\n{class_info['description']}\n\n")
                if input_section:
                    md_file.write(input_section + "\n")
                if output_section:
                    md_file.write(output_section + "\n")
                md_file.write("<HR>\n")
                md_file.write(f"Category: {category}\n\n")
                md_file.write(f"ComfyUI Data Analysis Node Reference. © 2025 Hide Inada (HowToSD.com). All rights reserved.\n")
            
            node_list[category].append((class_info['title'][2:], file_name, class_info['first_sentence']))

def generate_node_list(output_dir: str, node_list: Dict[str, List[str]]):
    """Generate node_reference.md file."""
    node_list_path = os.path.join(output_dir, "node_reference.md")
    with open(node_list_path, "w", encoding="utf-8") as md_file:
        md_file.write("# Node Reference\n")
        for category in sorted(node_list.keys()):
            md_file.write(f"## {category}\n| Node | Description |\n| --- | --- |\n")
            for title, file_name, description in sorted(node_list[category]):
                md_file.write(f"| [{title}]({file_name}) | {description} |\n")

def main():
    """Main function to process all Python files under modules/**.py."""
    source_dir = "modules"
    output_dir = "docs/reference"
    os.makedirs(output_dir, exist_ok=True)
    
    node_list = defaultdict(list)
    
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                process_python_file(file_path, output_dir, node_list)
    
    generate_node_list(output_dir, node_list)

if __name__ == "__main__":
    main()
