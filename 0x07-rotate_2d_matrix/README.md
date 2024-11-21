# 0x07. Rotate 2D Matrix

## Description
This project focuses on implementing an in-place algorithm to rotate an `n x n` 2D matrix by 90 degrees clockwise. The challenge is to achieve this without using additional data structures, thereby minimizing space complexity.

The matrix is represented as a list of lists in Python. The algorithm involves transposing the matrix and then reversing each row to perform the rotation.

## Learning Objectives
- Understand matrix manipulation using Python lists.
- Perform in-place operations to minimize space complexity.
- Use nested loops for matrix traversal and modification.
- Apply the concept of transposing and reversing rows to achieve a rotation.

---

## Requirements
- **Editors Allowed**: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using `python3` (version `3.8.10`).
- Code must follow **pycodestyle** style (version `2.8.0`).
- You are not allowed to import any Python module.
- All files must be executable.
- All functions must be documented.

---

## Usage
### Prototype
```python
def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.
    Args:
        matrix (list of lists): The matrix to rotate.
    Returns:
        None
    """
