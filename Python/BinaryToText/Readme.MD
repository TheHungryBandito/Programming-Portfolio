# Binary To Text
*Created by Joshua Crews - 22/12/2022*

## Description
The **Binary To Text** program takes a single/multiple bytes as input from the user,
converts them to an integer, then finds the character associated with the value of each integer
and displays the characters to the user.

## Requirements
* Python (3.10) or compatible version

## How to use
This program can be run using cmd like so:

if you have already navigated to the folder in the command line.

``` commandline
python main.py
``` 

or if not.

``` commandline
python path/to/file/main.py
``` 

Alternatively, this **c**an be run using an IDE such as Pycharm.

Upon start, you will be prompt with a message ```Please enter a byte or 'Y' to start process:```
the byte must be **8 digits long**, consisting of **1's and 0's**. After typing a byte, **press enter to
confirm**, you will then be prompt to enter another byte. Once you have finished entering bytes,
**enter 'Y' or 'y' to begin** the conversion process. 

## Example

Prompt:
``` commandline
Current bytes: []
Please enter a byte or 'Y' to start process: 
```

'Current bytes: []' is used to display bytes you have already entered.

Let's enter the bytes: 01001000, 01101001, 00100001.
``` commandline
Current bytes: []
Please enter a byte or 'Y' to start process: 01001000

Current bytes: ['01001000']
Please enter a byte or 'Y' to start process: 01101000

Current bytes: ['01001000', '01101000']
Please enter a byte or 'Y' to start process: 00100001

Current bytes: ['01001000', '01101000', '00100001']
Please enter a byte or 'Y' to start process: 
```

Now if I enter 'y' or 'Y'.

``` commandline
Current bytes: ['01001000', '01101001', '00100001']
Please enter a byte or 'Y' to start process: Y

ASCII Codes: [72, 105, 33]

String Result: Hi!

Process finished with exit code 0
```

The ASCII Codes consists of each byte converted to an integer.

The String Result is the ASCII Codes converted to their corresponding letter.


## How it works

To convert a byte (8 bits) to an integer it uses this function.

``` python
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
```

If a bit in the byte sequence is equal to '1' then the operation 2^<sup>i</sup> where 'i' 
is the reverse index of the bit in the byte, is run and the result is added to the previous result. 
If the bit is equal to '0' then this bit is skipped. Once the all bits have been checked, the
result is returned.

To convert the list of results to a string using ASCII Codes the following function is used.

``` python
# Taking in a list of ASCII Codes, this function will convert and concatenate all of them into a string.

@staticmethod
def convert_ASCII_list_to_string(numberASCIIList):
    stringResult = ""
    for number in numberASCIIList:
        stringResult = stringResult + chr(number)
    return stringResult
```

This function takes in a list of ASCII Codes and converts them using the
inbuilt chr(__i) function and joins them together to create the end result
that is to  be displayed to the user.


