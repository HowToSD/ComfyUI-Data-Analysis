import re
from typing import Dict
import pandas as pd

def increment_count(d: Dict[str, int], category: str) -> None:
    """Increment the count of a category in the dictionary.

    Args:
        d (Dict[str, int]): Dictionary storing category counts.
        category (str): The category to increment.
    """
    d[category] = d.get(category, 0) + 1

def process_import_lines(file_path: str) -> Dict[str, int]:
    """Extract and categorize import lines from a Python file.

    Args:
        file_path (str): Path to the Python file.

    Returns:
        Dict[str, int]: Dictionary containing category counts.
    """
    category_counts = {}
    
    with open(file_path, "r") as f:
        for line in f:
            if "import" in line:
                module_name = re.sub(r"^.*import ", "", line).strip()
                if module_name.startswith("SNS"):
                    increment_count(category_counts, "Seaborn")
                elif module_name.startswith("MPL"):
                    increment_count(category_counts, "Matplotlib")
                elif module_name.startswith("Pt"):
                    increment_count(category_counts, "PyTorch")
                elif module_name.startswith("Pandas"):
                    increment_count(category_counts, "Pandas")
                elif module_name.startswith(("CDA", "Python")):
                    increment_count(category_counts, "Misc")
                elif module_name.startswith("Numpy"):
                    increment_count(category_counts, "NumPy")
                else:
                    increment_count(category_counts, "Misc")
    
    return category_counts

def save_category_counts_to_csv(category_counts: Dict[str, int], output_file: str) -> None:
    """Save category counts as a sorted CSV file.

    Args:
        category_counts (Dict[str, int]): Dictionary containing category counts.
        output_file (str): Path to the output CSV file.
    """
    df = pd.DataFrame(list(category_counts.items()), columns=["Category", "Count"])
    df = df.sort_values(by=["Count"], ascending=False)
    df.to_csv(output_file, index=False)

def main() -> None:
    """Main function to process the import categories and save results."""
    category_counts = process_import_lines("__init__.py")
    save_category_counts_to_csv(category_counts, "node_count_breakdown.csv")

if __name__ == "__main__":
    main()
