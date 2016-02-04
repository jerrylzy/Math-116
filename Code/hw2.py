from collections import Counter

FREQ_LETTER = 'E'
ASCII_A = ord('A')
NUM_OF_LETTERS = 26
MAX_NUM_OF_VERIFICATION = 6

LETTER_FREQUENCY = { "A": 0.082, "B": 0.015, "C": 0.028, "D": 0.043, "E": 0.127,
                     "F": 0.022, "G": 0.020, "H": 0.061, "I": 0.070, "J": 0.002,
                     "K": 0.008, "L": 0.040, "M": 0.024, "N": 0.067, "O": 0.075,
                     "P": 0.019, "Q": 0.001, "R": 0.060, "S": 0.063, "T": 0.091,
                     "U": 0.028, "V": 0.010, "W": 0.023, "X": 0.001, "Y": 0.020, "Z": 0.001 }

def tochar(num):
    return chr(num + ASCII_A)

def calcMod(lhs, rhs):
    return (ord(lhs) - ord(rhs)) % NUM_OF_LETTERS

def calcLetter(lhs, rhs):
    return tochar(calcMod(lhs, rhs))

def dotProduct(v1, v2):
    result = 0
    for i in range(NUM_OF_LETTERS):
        ch = tochar(i)
        result += v1[ch] * v2[ch]
    return result

def decrypt(ciphertext, key):
    plaintext = ""
    counter = 0
    for c in ciphertext:
        if counter == len(key):
            counter = 0
        plaintext += calcLetter(c, key[counter])
        counter += 1
    return plaintext

def decryptVigenere(ciphertext, keyLength):
    key = ""
    keyRaw = ""
    for i in range(keyLength):
        maxDotProduct = 0.0
        freqDict = Counter(ciphertext[i::keyLength])
        sortedLetter = sorted(freqDict, key = freqDict.get, reverse = True)
        ch = ""
        translatedChar = ""
        counter = 0
        for letter in sortedLetter:
            if counter >= MAX_NUM_OF_VERIFICATION:
                break
            keyTemp = ""
            calcChar = calcLetter(letter, FREQ_LETTER)
            for j in range(keyLength):
                keyTemp += calcChar
            text = decrypt(ciphertext, keyTemp)
            freqText = Counter(text[i::keyLength])
            dotProdResult = dotProduct(freqText, LETTER_FREQUENCY)
            if dotProdResult > maxDotProduct:
                maxDotProduct = dotProdResult
                ch = letter
                translatedChar = calcChar
            counter += 1
        keyRaw += ch
        key += translatedChar

    print("Selected Most Frequent Letters:", keyRaw)
    print("Vigenere Key is:", key)
    return decrypt(ciphertext, key)

def findKeyLength(ciphertext):
    keyLength = 0
    maxCoincidence = 0

    for shift in range(len(ciphertext)):
        shiftedtext = "#"
        for i in range(shift):
            shiftedtext += "#"
        shiftedtext += ciphertext
        coincidence = 0
        for i in range(len(ciphertext)):
            if ciphertext[i] == shiftedtext[i]:
                coincidence += 1

        if coincidence >= maxCoincidence:
            maxCoincidence = coincidence
            keyLength = shift + 1

    return keyLength

def q1():
    print("Question 1:")
    ciphertext = "ZDVOGZIMKGYZFVDDVXUBPA"
    key = "VIRGO"

    print("Decrypted Message: " + decrypt(ciphertext, key) + "\n")

def q2():
    print("Question 2:")
    ciphertext = "FEWCNWQBMSNSTEJYWOTMXDGVXYCVCYYODSGDQEUOFOTNBAUDQEDKLKDYWEQP" \
                 "JLKPNSROWTFOOEPNRNICXMGDQIPQHOWEBEVRNMCCJPWXLHNSWEKRJVGXNIVR" \
                 "NRVRNTKWNNQBCHGSWCNSWAVSXNVYNXRVJIPWHSGVOTQKVAPGQOTSBEUKWDUV" \
                 "NERCDNFOATJOKLCXTEVYOTJOEETIORGOMOODQAVSYRQFRDGKWDVRNNSENSVS" \
                 "XNUDQEOKWNGBRNYRRCJSYRQFRDGSC"

    print("Decrypted Message: " + decryptVigenere(ciphertext, 4) + "\n")

def q3():
    print("Question 3:")
    ciphertext = "DOEESFDAWTSRJSXSHRZFHJGBIEAGIEOIGKWYANVWKVPHAAGYKNZLVVJBTUYP" \
                 "QROWRBREKSQUAMBUOYRELKSYENPZWPDHXOOFXRXOWACAISFGECNDOEHYFSZB" \
                 "ZOKGIFLRHVIPPHBKVRWDPSGFQNDMDBJHBKPEAALLOAZHXDCBGEWXFBIMRHCV" \
                 "JTHXJVAWEAYRWSMJOACEESBXXIKVKVPHWMZYCRXQDYQMTYSNJDTTZNYKMGDX" \
                 "JOMKCJWTLGBFWIWZSFQDWWBYUYHMRBJOMHFBLOLWHBENOWGGENLGIGDAYJWP" \
                 "WNLWQHNIMASF"

    keyLength = findKeyLength(ciphertext)
    print("Decrypted Message: " + decryptVigenere(ciphertext, keyLength) + "\n")

def main():
    q1()
    q2()
    q3()

if __name__ == "__main__":
    main()

