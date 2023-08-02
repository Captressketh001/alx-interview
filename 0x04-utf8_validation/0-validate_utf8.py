#!/usr/bin/python3
"""method that determines if a given data set
represents a valid UTF-8 encoding"""


def validUTF8(data):
    def is_start_byte(byte):
        byte_1 = (byte >> 7) == 0b0
        byte_2 = (byte >> 5) == 0b110
        byte_3 = (byte >> 4) == 0b1110
        byte_4 = (byte >> 3) == 0b11110
        return byte_1 or byte_2 or byte_3 or byte_4

    def is_continuation_byte(byte):
        return (byte >> 6) == 0b10

    i = 0
    while i < len(data):
        # Get the current byte and its most significant bit (MSB)
        byte = data[i] & 0xFF

        # Check if it's a valid start byte for a UTF-8 character
        if not is_start_byte(byte):
            return False

        # Determine the number of bytes the character occupies
        # based on the MSB of the start byte
        num_bytes = 1
        if (byte >> 7) == 0b0:
            num_bytes = 1
        elif (byte >> 5) == 0b110:
            num_bytes = 2
        elif (byte >> 4) == 0b1110:
            num_bytes = 3
        elif (byte >> 3) == 0b11110:
            num_bytes = 4

        # Check if the data has enough bytes to represent the character
        if i + num_bytes > len(data):
            return False

        # Check if the subsequent bytes are valid continuation bytes
        for j in range(1, num_bytes):
            if not is_continuation_byte(data[i + j] & 0xFF):
                return False

        # Move the index to the next character
        i += num_bytes
    return True
