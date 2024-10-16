#!/usr/bin/python3
"""
Module to compute the minimum number of operations to get exactly n H's
using Copy All and Paste operations.
"""


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed to result in exactly
    n H characters in the file.

    Args:
        n (int): Target number of characters.

    Returns:
        int: Minimum number of operations to reach n characters, or 0 if n < 2.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
