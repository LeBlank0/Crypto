import sys
import base64

def xor(key):
    with open("basic4.webp", mode='rb') as file:
        encrypted = file.read()
        len_key = len(key)
        res = []

        for i in range(0, len(encrypted)):
            res.append((encrypted[i] ^ key[i % len_key]))
        return bytes(res)
  
def main():
    res = xor(b'w?v=MsQaPR2NjP8')
    f = open('./res.webp', 'wb')
    f.write(res)
    f.close()
  
if __name__ == '__main__':
    main()