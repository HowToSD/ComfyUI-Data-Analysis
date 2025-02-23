from typing import Any, Dict
import pandas as pd
from .utils import column_labels_string_to_list

class PandasMelt:
    """
    Performs an unpivot operation (melt) on a pandas DataFrame.

    ## Understanding Melt (Unpivot)
    The melt operation converts a DataFrame from **wide format** (where multiple columns represent separate variables) into **long format** (where values are stacked under a single column).

    ### Example: Frozen Food Prices Table

    Given the following DataFrame:

    ```
    Frozen Food Prices

    Manufacturer                   Pizza        Burger
    ---------------------------------------------------
    Aimee Italian Foods               10            12
    Olivia Cuisine                    11             8
    Maddie Foods                      12             7
    ```

    To demonstrate **melting a single column**, we will **only transform the `"Pizza"` column** and **temporarily exclude `"Burger"`** from the output. `"Burger"` is not affected in this step because we are only selecting `"Pizza"` for melting.

    ```
    Frozen Food Prices

    Manufacturer                   X                Y
    ---------------------------------------------------
    Aimee Italian Foods            Pizza            10
    Olivia Cuisine                 Pizza            11
    Maddie Foods                   Pizza            12
    ```

    Here:

    - Column `X` is assigned to `"Item"` (`var_name`).
    - Column `Y` is assigned to `"Price"` (`value_name`).
    - `"Pizza"` is explicitly specified in `value_vars` as the column being unpivoted.
    - `"Manufacturer"` remains unchanged and is included in `id_vars` to preserve row identity.

    The final transformed DataFrame:

    ```
    Frozen Food Prices

    Manufacturer                   Item            Price
    ----------------------------------------------------
    Aimee Italian Foods            Pizza            10
    Olivia Cuisine                 Pizza            11
    Maddie Foods                   Pizza            12
    ```

    ### Expanding the Melt Operation

    If we want to **melt both `"Pizza"` and `"Burger"` together**, we specify both columns in `value_vars`:

    ```
    Frozen Food Prices

    Manufacturer                   Item           Price
    ----------------------------------------------------
    Aimee Italian Foods            Pizza            10
    Olivia Cuisine                 Pizza            11
    Maddie Foods                   Pizza            12
    Aimee Italian Foods            Burger           12
    Olivia Cuisine                 Burger            8
    Maddie Foods                   Burger            7
    ```

    Here, we explicitly define:

    - `"Pizza"` and `"Burger"` in `value_vars`.
    - A new `"Item"` column (`var_name`), which holds the original column names (`"Pizza"`, `"Burger"`).
    - A `"Price"` column, which stores the corresponding values.

    To specify both columns in this node, provide:

    ```
    Pizza,Burger
    ```

    This node automatically converts the string into a list and passes it to `pandas.DataFrame.melt()`.

    ![Melt example](../images/melt.png)


    Refer to the [Pandas documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.melt.html) for more information.

    ## Limitation
    MultiIndex columns are not supported.

    category: Transformation
    """

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        """
        Defines the input types for the `select_columns` function.

        Returns:
            Dict[str, Any]: A dictionary specifying required input types.
        """
        return {
            "required": {
                "dataframe": ("DATAFRAME", {}),
                "id_vars": ("STRING", {"default": ""}),
                "value_vars": ("STRING", {"default": ""}),
                "var_name": ("STRING", {"default": ""}),
                "value_name": ("STRING", {"default": ""}),
                "ignore_index": ("BOOLEAN", {"default": True})
            }
        }

    RETURN_TYPES: tuple = ("DATAFRAME",)
    FUNCTION: str = "f"
    CATEGORY: str = "Data Analysis"

    def f(self, dataframe: pd.DataFrame,
                id_vars: str,
                value_vars: str,
                var_name: str,
                value_name: str,
                ignore_index: bool) -> tuple:
        """
        Selects specific columns from a pandas DataFrame.

        Args:
            dataframe (DataFrame): The input DataFrame.
            id_vars (str): Comma-separated string to specify ID variable columns.
            value_vars (str): Comma-separated string to specify column(s) to be unpivoted.
            var_name (str): New column label for the column that contains original column labels as row values.
            value_name (str): Name of the new column that holds the values for columns specified in `value_vars`.
            ignore_index (bool): Flag that specifies whether to keep the original index.
                                 If ``True``, a new sequential index is generated.
                                 If ``False``, the original index is retained and repeated as needed.

        Returns:
            tuple: A tuple containing the DataFrame.
        """
        id_vars = column_labels_string_to_list(dataframe, id_vars)
        value_vars = column_labels_string_to_list(dataframe, value_vars)
        var_name = column_labels_string_to_list(dataframe, var_name, no_check=True)
        value_name = column_labels_string_to_list(dataframe, value_name, no_check=True)

        if len(id_vars) == 1:
            id_vars = id_vars[0]
        if len(value_vars) == 1:
            value_vars = value_vars[0]
        if len(var_name) == 0:
            var_name = None
        elif len(var_name) == 1:
            var_name = var_name[0]
        if len(value_name) == 0:
            value_name = None
        elif len(value_name) == 1:
            value_name = value_name[0]

        df2 = dataframe.melt(
            id_vars=id_vars,
            value_vars=value_vars,
            var_name=var_name,
            value_name=value_name,
            ignore_index=ignore_index)
        return (df2,)
