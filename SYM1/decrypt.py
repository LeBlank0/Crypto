from Crypto.Cipher import AES
import hashlib
import itertools

def xor(plaintext, payload):
    len_PT = len(plaintext)
    res = []

    for i in range(0, len(payload)):
        res.append(payload[i] ^ plaintext[i % len_PT])
    return bytes(res)

def bruteForce():
    plaintext = b"I was lost, but "
    combinations = itertools.product('0123456789abcdef', repeat=7)

    for combination in combinations:
        cipherText = bytes.fromhex(f"{combination[0] + combination[1]}f374a82db50b23{combination[2] + combination[3] + combination[4] + combination[5] + combination[6]}b88f1d976dd")
        cipher = AES.new(hashlib.sha256("omgwtfbbq".encode()).digest(), AES.MODE_ECB) #mode ECB car CBC donne un IV random
        payload = cipher.decrypt(cipherText)
        try:
            iv = xor(plaintext, payload).decode("utf-8")
            if iv.isprintable() and len(iv) == 16:
                print(iv)
        except Exception as ex:
            pass #without try except crash when wrong iv

def main():
    bruteForce()
  
if __name__ == '__main__':
    main()