import sys
import base64

def getKey():
    with open("basic4.webp", mode='rb') as bmp:
        cipher = bmp.read()
        plain = b'\x52\x49\x46\x46\x5c\xe2\x00\x00\x57\x45\x42\x50\x56\x50\x38' #first 15 bytes

        for i, byte in enumerate(cipher):
            if i == 15:
                return
            key = byte ^ plain[i] #xor 1 by 1
            print(chr(key))
  
def main():
    getKey()
  
if __name__ == '__main__':
    main()