# /*=============================================================================
# \Assignment: pa01 - Encrypting a plaintext file using the Vigenere cipher
# \
# \Author: Anthony Webb
# \Language: python
# \
# \To Compile: javac pa01.java
# \gcc -o pa01 pa01.c
# \g++ -o pa01 pa01.cpp
# \go build pa01.go
# \python pa01.py
# \
# \To Execute: java -> java pa01 kX.txt pX.txt
# \or c++ -> ./pa01 kX.txt pX.txt
# \or c -> ./pa01 kX.txt pX.txt
# \or go -> ./pa01 kX.txt pX.txt
# |or python -> python pa01.py kX.txt pX.txt
# | where kX.txt is the keytext file
# | and pX.txt is plaintext file
# |
# | Note: All input files are simple 8 bit ASCII input
#| 
# | Class: CIS3360 - Security in Computing - Fall 2022
# | Instructor: McAlpin
# | Due Date: per assignment
# |
#+=============================================================================*/

import re
import sys
import textwrap

key = open(sys.argv[1],'r')
keyContent = key.read()

plaintext = open(sys.argv[2],'r')
plaintextContent = plaintext.read()

lowerKey = [x.lower() for x in keyContent]
lowerPlain = [x.lower() for x in plaintextContent]

lowerKey = [re.sub(r'[^a-zA-Z0-9]','',string) for string in lowerKey]
lowerPlain = [re.sub(r'[^a-zA-Z0-9]','',string) for string in lowerPlain]

cleanKey = []
for ele in lowerKey:
    if ele.strip():
        cleanKey.append(ele)

cleanPlain = []
for ele in lowerPlain:
    if ele.strip():
        cleanPlain.append(ele)

if len(cleanPlain) > len(cleanKey):
    rLen = len(cleanPlain) - len(cleanKey)
    for i in range(rLen):
        cleanKey.append('x')

alphaKey = []
for chars in cleanKey:
    alpha = ord(chars) - 97
    alphaKey.append(alpha)

alphaPlain = []
for chars in cleanPlain:
    alpha = ord(chars) - 97
    alphaPlain.append(alpha)

alphaCipher = []
for i in range(len(alphaKey)):
    cipher = (alphaKey[i] + alphaPlain[i]) % 26
    alphaCipher.append(cipher)



ciphertext = []
for i in range (len(alphaKey)):
    if (alphaCipher[i] == 0):
        ciphertext.append('a')
    if (alphaCipher[i] == 1):
        ciphertext.append('b')
    if (alphaCipher[i] == 2):
        ciphertext.append('c')
    if (alphaCipher[i] == 3):
        ciphertext.append('d')
    if (alphaCipher[i] == 4):
        ciphertext.append('e')
    if (alphaCipher[i] == 5):
        ciphertext.append('f')
    if (alphaCipher[i] == 6):
        ciphertext.append('g')
    if (alphaCipher[i] == 7):
        ciphertext.append('h')
    if (alphaCipher[i] == 8):
        ciphertext.append('i')
    if (alphaCipher[i] == 9):
        ciphertext.append('j')
    if (alphaCipher[i] == 10):
        ciphertext.append('k')
    if (alphaCipher[i] == 11):
        ciphertext.append('l')
    if (alphaCipher[i] == 12):
        ciphertext.append('m')
    if (alphaCipher[i] == 13):
        ciphertext.append('n')
    if (alphaCipher[i] == 14):
        ciphertext.append('o')
    if (alphaCipher[i] == 15):
        ciphertext.append('p')
    if (alphaCipher[i] == 16):
        ciphertext.append('q')
    if (alphaCipher[i] == 17):
        ciphertext.append('r')
    if (alphaCipher[i] == 18):
        ciphertext.append('s')
    if (alphaCipher[i] == 19):
        ciphertext.append('t')
    if (alphaCipher[i] == 20):
        ciphertext.append('u')
    if (alphaCipher[i] == 21):
        ciphertext.append('v')
    if (alphaCipher[i] == 22):
        ciphertext.append('w')
    if (alphaCipher[i] == 23):
        ciphertext.append('x')
    if (alphaCipher[i] == 24):
        ciphertext.append('y')
    if (alphaCipher[i] == 25):
        ciphertext.append('z')

    
cipherstring = ''.join(ciphertext)
cleankeyString = ''.join(cleanKey)
cleanplainString = ''.join(cleanPlain)

print (textwrap.fill(cleanplainString.lower(), width=80))
print('\n')
print (textwrap.fill(cleankeyString.lower(), width=80))
print('\n')
print (textwrap.fill(cipherstring, width=80))


#/*=============================================================================
#| I Anthony Webb an385571 affirm that this program is
#| entirely my own work and that I have neither developed my code together with
#| any another person, nor copied any code from any other person, nor permitted
#| my code to be copied or otherwise used by any other person, nor have I
#| copied, modified, or otherwise used programs created by others. I acknowledge
#| that any violation of the above terms will be treated as academic dishonesty.
#+=============================================================================*/