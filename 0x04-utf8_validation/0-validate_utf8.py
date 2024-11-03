#!/usr/bin/python3
"""
Module for UTF-8 validation.
"""


def validUTF8(data):
    """Check if a given data set represents a valid UTF-8 encoding."""
    n_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        # Ensure the number is within the valid byte range
        if num > 255:
            return False

        bin_rep = bin(num).replace('0b', '').rjust(8, '0')

        if n_bytes == 0:
            for bit in bin_rep:
                if bit == '0':
                    break
                n_bytes += 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (num & mask1 and not (num & mask2)):
                return False

        n_bytes -= 1

    return n_bytes == 0
