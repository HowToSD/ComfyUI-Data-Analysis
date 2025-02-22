# Pandas Kurtosis
Computes the unbiased kurtosis of the DataFrame.

This method returns the excess kurtosis rather than the raw kurtosis. 
Excess kurtosis is calculated by subtracting 3 from the raw kurtosis, 
which offsets it relative to the kurtosis of a normal distribution.

## Input
| Name | Data type |
|---|---|
| dataframe | DataFrame |
| axis |  |

## Output
| Data type |
|---|
| Series |

<HR>
Category: Summary statistics

ComfyUI Data Analysis Node Reference. © 2025 Hide Inada (HowToSD.com). All rights reserved.
