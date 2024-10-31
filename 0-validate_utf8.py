#!/usr/bin/python3

def validUTF8(data):
    """Return True if data represents a valid UTF-8 encoding, else return False."""
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits in each byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Extract the 8 least significant bits
        byte = num & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            elif (byte >> 7):  # 1-byte character should start with 0 in MSB
                return False
        else:
            # Check that the next byte starts with 10
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1

    # If num_bytes is 0, all characters were properly validated
    return num_bytes == 0

