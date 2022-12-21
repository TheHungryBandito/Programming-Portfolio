# Created by Joshua Crews - 21/12/2022

from byte_converter import ByteConverter


def main():
    byteConverter = ByteConverter()
    byteList = byteConverter.get_bytes()
    resultASCIIList = []

    for byte in byteList:
        resultASCII = byteConverter.convert_byte_to_ASCII(byte)
        resultASCIIList.append(resultASCII)

    stringResult = byteConverter.convert_ASCII_list_to_string(resultASCIIList)

    print(f"ASCII Codes: {resultASCIIList}")
    print(f"String Result: {stringResult}")


if __name__ == '__main__':
    main()
