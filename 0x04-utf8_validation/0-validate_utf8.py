#!/usr/bin/python3
"""
Module to validate UTF-8 encoding
"""


def validUTF8(data):
    """
    Checks if a given list of integers is a valid UTF-8 encoding.

    Parameters:
    - data: List[int] - List of integers where each integer represents a byte

    Returns:
    - bool: True if data is a valid UTF-8 encoding, otherwise False.
    """
    n_bytes = 0  # Number of continuation bytes expected

    # Masks to check the most significant bits of each byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Extract only the 8 least significant bits
        byte = num & 0xFF

        if n_bytes == 0:
            # Count leading 1's to determine the number of bytes
            if (byte & mask1) == 0:
                continue  # 1-byte character
            elif (byte & (mask1 >> 1)) == mask1:
                n_bytes = 1  # 2-byte character
            elif (byte & (mask1 >> 2)) == mask1:
                n_bytes = 2  # 3-byte character
            elif (byte & (mask1 >> 3)) == mask1:
                n_bytes = 3  # 4-byte character
            else:
                return False  # Invalid UTF-8 start byte
        else:
            # Check continuation byte starts with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False
            n_bytes -= 1

    return n_bytes == 0
