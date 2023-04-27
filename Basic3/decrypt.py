import sys
import base64

def xor(key):
    with open("ch2.bmp", mode='rb') as file:
        encrypted = file.read()
        len_key = len(key)
        res = []

        for i in range(0, len(encrypted)):
            res.append((encrypted[i] ^ key[i % len_key]))
        return bytes(res)
  
def main():
    res = xor(b'gitgud')
    f = open('./res.bmp', 'wb')
    f.write(res)
    f.close()
  
if __name__ == '__main__':
    main()