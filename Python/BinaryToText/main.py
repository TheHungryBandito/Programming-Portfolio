# Created by Joshua Crews - 22/12/2022

from byte_converter import ByteConverter


# Gets bytes from user input.
def get_bytes(byteConverter):
    byteList = []
    inputNeeded = True

    # Repeats until user specifies there is no more.
    while inputNeeded:

        # Show current bytes.
        print(f"\nCurrent bytes: {byteList}")
        userInput = input("Please enter a byte or 'Y' to start process: ")

        # If user wants to begin the process.
        if userInput.lower() == 'y':
            inputNeeded = False
            break

        # Ensure input is a byte.
        if not byteConverter.validate_byte(userInput):
            print(f"{userInput} is not a valid byte.")
            continue

        # Add byte to list.
        byteList.append(userInput)

    return byteList


def main():
    byteConverter = ByteConverter()
    byteList = get_bytes(byteConverter)
    resultASCIIList = []

    for byte in byteList:
        resultASCII = byteConverter.convert_byte_to_integer(byte)
        resultASCIIList.append(resultASCII)

    stringResult = byteConverter.convert_ASCII_list_to_string(resultASCIIList)

    print(f"\nASCII Codes: {resultASCIIList}")
    print(f"\nString Result: {stringResult}")


if __name__ == '__main__':
    main()

