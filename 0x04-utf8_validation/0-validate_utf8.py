#!/usr/bin/python3
"""
A module that provides a method to determine if a given data
set represents a valid UTF-8 encoding.
"""


def validUTF8(data: list) -> bool:
    """
    A method that determines if given data set represents
    a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing the bytes
        of the data set.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Track the number of bytes remaining for a character
    # to determine if there is continuation bytes
    remainder_bytes = 0

    for i in data:
        # Is the current byte is a continuation byte?
        if remainder_bytes > 0:
            # If the current byte is not a continuation byte,
            # the UTF-8 encoding is invalid
            if (i >> 6) != 0b10:
                return False
            remainder_bytes -= 1
        else:
            # Calculate number of bytes that is left in the byte series
            # for this character
            if (i >> 7) == 0b0:
                # 1-byte character
                remainder_bytes = 0
            elif (i >> 5) == 0b110:
                # 2-byte character
                remainder_bytes = 1
            elif (i >> 4) == 0b1110:
                # 3-byte character
                remainder_bytes = 2
            elif (i >> 3) == 0b11110:
                # 4-byte character
                remainder_bytes = 3
            else:
                # Invalid starting byte
                return False

    # If there are remaining bytes, the UTF-8 encoding is invalid
    if remainder_bytes > 0:
        return False

    return True
