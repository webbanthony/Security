
import re
import sys
import textwrap

file = open(sys.argv[1],'r')
fileContent = file.read()

checksumVal = int(sys.argv[2])

#Check if valid checksum value was entered; if not, exit
if (checksumVal == 8 or checksumVal == 16 or checksumVal == 32):
    pass
else:
    print('Invalid checksum value. Exiting now.')
    exit(0)

print('##########################')
print('Filename:',sys.argv[1])
print('Checksum Value:',checksumVal)
print('File Content:',textwrap.fill(fileContent, width = 80))
print('##########################')
print()

listFile = [fileContent.strip()]

print('File contents in a list:',listFile)

listfileAscii = []
for ele in listFile:
    listfileAscii.append(ord(ele))

print('Ascii values:',listfileAscii)

# Based on checksum value, need to convert it to certain # of bits. (8,16,32)
listfileBinary = []
for ele in listfileAscii:
    listfileBinary.append((format(ele,'b')))

for ele in listfileBinary:
    count = 0;
    while (int(ele) > 0):
        count = count + 1
        ele = int(ele)//10

print('Ascii values in binary (not padded):',listfileBinary)
print('Value needs to be padded by:',checksumVal - count)
print()
print('##################')

for i, s in enumerate(listfileBinary):
    listfileBinary[i] = s.ljust(checksumVal,'0')

    # if the list has only one element, add zero to properly get result from function later on
    if (len(listfileBinary) == 1):
        listfileBinary.append('0'.ljust(checksumVal,'0'))


print('len of list',len(listfileBinary))
print('List after padding and adding 0 if needed:',listfileBinary)
print('##################\n')

# adds two binary numbers using carry rules
def binaryadd (a,b,maxlen):
    carry = 0
    res = ''

    for i in range (maxlen -1,-1,-1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        res = ('1' if r % 2 == 1 else '0') + res

        carry = 0 if r < 2 else 1

        if carry != 0:
            result = '1' + res

    return(res.zfill(maxlen))



# loop to add all numbers until end is reached then return final sum
for i in range(len(listfileBinary)):
    sum = binaryadd(listfileBinary[i],listfileBinary[i - 1],checksumVal)

res = [sum]


# print out resulting sum to check
print(res[0])



# helper function to twosComp that flips binary bits
def flip(c):
    return '1' if (c == 0) else '0'

# function that takes binary sum as a string and returns twos compliment result into a list
def twosComp(bin):
    n = len(bin)
    ones = ""
    twos = ""

    for i in range(n):
        ones += flip(bin[i])

    ones = list(ones.strip(""))
    twos = list(ones)

    for i in range (n-1,-1,-1):
        
        if (ones[i] == '1'):
            twos[i] = '0'
        else:
            twos[i] = '1'
            break
    
    i -= 1

    if (i == -1):
        twos.insert(0,'1')
    
    return twos

twos = twosComp(res[0])

print(twos)
