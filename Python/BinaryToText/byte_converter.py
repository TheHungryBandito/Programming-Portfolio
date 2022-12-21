# Created by Joshua Crews - 22/12/2022

import math


# ByteConverter is used for handling bytes that are to be converted into other values.
class ByteConverter:

    # Taking in a list of ASCII Codes, this function will convert and concatenate all of them into a string.
    @staticmethod
    def convert_ASCII_list_to_string(numberASCIIList):
        stringResult = ""
        for number in numberASCIIList:
            stringResult = stringResult + chr(number)
        return stringResult

    # Converts a byte into an integer.
    @staticmethod
    def convert_byte_to_integer(byte):
        i = len(byte) - 1
        result = 0
        for bit in byte:
            if bit == '1':
                result += int(math.pow(2, i))
            i -= 1
        return result

    # Attempts to parse an int from a string (Default base is 10) Returns int if success or False if failed.
    @staticmethod
    def try_parse_int(strNumber, base=10):
        try:
            return int(strNumber, base)
        except ValueError:
            return False

    # Validates a byte. Returns False if validation failed or True if success.
    def validate_byte(self, byte):
        # Does byte have enough bits?
        if not len(byte) == 8:
            return False

        # Is byte made of numbers?
        if not self.try_parse_int(byte, 10):
            return False

        # Is byte made of 1's and 0's?
        for bit in byte:
            if bit == '1' or bit == '0':
                continue
            return False

        # If we made it this far then we succeed.
        return True
