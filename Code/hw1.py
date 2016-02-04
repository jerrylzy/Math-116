def findPrivateKey(pubKey, mod):
    for i in range(1000):
        if (pubKey * i) % mod == 1:
            print("Private Key:", i)
            return i
    return -1

def decrypt(pubKey, mod, ciphertext):
    plaintext = ""
    privKey = findPrivateKey(pubKey, mod)
    if privKey == -1:
        print("[!] Private Key note found. [!]")
        return
    for c in ciphertext:
        plaintext += chr((c * privKey) % mod)

    print("Decrypted Message:", plaintext)

def decryptMessage():
    pubKey = int(input("Please input the public key: "))
    mod = int(input("Please input the modulo: "))
    ciphertext = [ 84, 107, 38, 3, 68, 32, 68, 58, 9, 127, 68, 32, 25, 78, 57 ]
    decrypt(pubKey, mod, ciphertext)

def main():
    decryptMessage()

if __name__ == "__main__":
    main()
