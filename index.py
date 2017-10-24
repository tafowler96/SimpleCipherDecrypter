import json
import re
# Tests indices of coincidence of substrings with lengths up to 10
# returns the length with the highest index of coincidence
def getKeyLen(cipherText):
    maxIndex = 0
    keyLen = 1
    for m in range(1, 11):
        frequencies=[0 for i in range(26)]
        numChars = 0
        index = 0
        # Counts the frequencies of each letter in the first substring based on key size
        for i in range(len(cipherText)):
            # This condition makes sure the character being tested will be in the string
            # with key length m
            if (i % m == 0):
                # counts each letter
                frequencies[ord(cipherText[i]) - 65] += 1
                numChars += 1
        for num in frequencies:
            # Computes expected index of coincidence
            index += (num/numChars) ** 2

        # if this index of coincidence is the greatest, remember the index
        # and the m. The split length with the greatest index of coincidence will
        # most likely correspond to the English language.
        if index > maxIndex:
            maxIndex = index
            keyLen = m
    return keyLen

# Given a ciphertext and the length of the key,
# Look at frequencies to find the key
def getKey(cipherText, keyLen):
    numLetters = len(cipherText)
    # Frequencies of letters in the English language
    standardFreq = [.082, .015, .028, .043, .127, .022, .020, .061, .070, .002, .008, .040, .024, .067, .075, .019, .001, .060, .063, .091, .028, .010, .023, .001, .020, .001]

    # Gets characters that are affected by one specific key character
    # eg. Keylength is "2" and cipher text is "abcdefghijkl"
    # this will get either                    "a c e g i k"
    # or                                      "b d f h j l"
    split = [cipherText[i:i+keyLen] for i in range(0, len(cipherText), keyLen)]
    frequencies=[0 for i in range(26)]
    key = ""
    for n in range(0, keyLen):
        # Count the number of occurences of each letter
        frequencies=[0 for i in range(26)]
        for i in split:
            if (n < len(i)):
                frequencies[ord(i[n]) - 65] += 1

        maxMG = 0
        maxMGindex = 0
        # Try shifting the characters by each amount: 0 to 25
        for g in range(26):
            mg = 0


            for freq in range(len(frequencies)):
                mg += standardFreq[freq] * frequencies[(freq + g) % 26]/numLetters
            if mg > maxMG:
                maxMG = mg
                maxMGindex = g
        key = key + chr(maxMGindex+65)
    return key

# Decodes vigenere ciphertext given a key
def decodeVig(cipherText, key):
    plainText = ""
    keyLen = len(key)
    split = [cipherText[i:i+keyLen] for i in range(0, len(cipherText), keyLen)]
    for i in split:
        for j in range(keyLen):
            if (j < len(i)):
                # converts to int, mods to wrap around the alphabet, then converts back to character
                plainText = plainText + chr((ord(i[j]) - 65 - (ord(key[j])-65)) % 26 + 65)
    return plainText

def stripNonAlphabet(text):
    return ''.join([i for i in text if i.isalpha()])

def lambda_handler(event, context):
    C = event["body"]["cipherText"]
    C = stripNonAlphabet(C).upper()
    keyLen = getKeyLen(C)
    key = getKey(C, keyLen)
    plainText = decodeVig(C, key)

    resp = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": {
            "key": key,
            "plainText": plainText
        }
    }

    return resp
