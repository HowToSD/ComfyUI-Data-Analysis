# Pt Einsum
Performs Tensor operations specified in the Einstein summation equation.

Specify Einstein summation notation in the first socket.
Specify two tensors in tens_a, tens_b. If you specify the third tensor, specify in tens_c.
Otherwise, leave the socket unconnected.

Sublist format is not supported.

## Input
| Name | Data type |
|---|---|
| equation | String |
| tens_a | Tensor |
| tens_b | Tensor |
| tens_c | Tensor |

## Output
| Data type |
|---|
| Tensor |

<HR>
Category: PyTorch wrapper - Matrix operations

ComfyUI Data Analysis Node Reference. © 2025 Hide Inada (HowToSD.com). All rights reserved.
