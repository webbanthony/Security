#/*=============================================================================
#| Assignment: pa02 - Calculating an 8, 16, or 32 bit
#| checksum on an ASCII input file
#|
#| Author: Anthony Webb
#| Language: Python
#|
#| To Compile: python pa02.py //Caution - expecting input parameters
#|
#| To Execute: python-> python pa02.py inputFile.txt 8
#| where inputFile.txt is an ASCII input file
#| and the number 8 could also be 16 or 32
#| which are the valid checksum sizes, all
#| other values are rejected with an error message
#| and program termination
#|
#| Note: All input files are simple 8 bit ASCII input
#|
#| Class: CIS3360 - Security in Computing - Fall 2022
#| Instructor: McAlpin
#| Due Date: per assignment
#|
#+=============================================================================*/

# to do:
# send output failed message to stderr


import sys
import textwrap

def eightbitChecksum (list):
    listSum = sum(list)
    csumVal = 2 **checksumVal

    res = listSum % csumVal

    hexVal = hex(res)[2:]

    return hexVal

def sixteenbitChecksum (list):
      if len(list) % 2 != 0:
        list.append(88)
        
    for i in range(len(list)):
        if i % 2 == 0:
            list[i] = (list[i] * 256)

    
    res = sum(list) % 2**16
    return hex(res)[2:]

def thirtytwobitChecksum (list):
    if len(list) > 4:
        for i in range(8-len(list)):
            list.append(88)
    
    if len(list) < 4:
        for i in range(4 - len(list)):
            list.append(88)

    for i in range(len(list)):

        if i == 0: list[i] = (list[i] * 2 ** 24)
        if i == 1: list[i] = (list[i] * 2 **16)
        if i == 2: list[i] = (list[i] * 2 **8)
        if i == 3: pass;
        if i == 4: list[i] = (list[i] * 2 ** 24)
        if i == 5: list[i] = (list[i] * 2 ** 16)
        if i == 6: list[i] = (list[i] * 2 ** 8)
        if i == 7: pass;

    res = sum(list) % 2 **32

    return hex(res)[2:]


inputFile = open(sys.argv[1],'r')
checksumVal = int(sys.argv[2])

#Check if valid checksum value was entered; if not, exit
if (checksumVal == 8 or checksumVal == 16 or checksumVal == 32):
    pass
else:
    sys.stderr.write('Valid checksum sizes are 8, 16, or 32\n')
    exit(0)

fileContent = list(inputFile.read())

convertedList = []
for ele in fileContent:
        convertedList.append(ord(ele))


print(''.join(fileContent))


if (checksumVal == 8):
    print(eightbitChecksum(convertedList))

if (checksumVal == 16):
    print(sixteenbitChecksum(convertedList))

if (checksumVal == 32):
    print(thirtytwobitChecksum(convertedList))
