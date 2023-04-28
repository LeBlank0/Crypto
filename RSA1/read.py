from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

def RSA_read():
    file = open('rsa1Cipher.txt', 'rb')
    cipherText = file.read()
    file.close
    #Get all the component for the key
    file = open('rsa1.pem', 'r')
    key = RSA.import_key(file.read())
    file.close

    p = 11901234461494228310064076121482038286429650089208969229876184007349956782094248940290427800597817633601014470221576037327691902428151823981665392121868907
    q = key.n // p #To get q we just need to divid N by p since N = p*q
    phi = (p - 1) * (q - 1)
    d = pow(key.e, -1, phi)
    private_key = RSA.construct((key.n, key.e, d, p, q))
    cipher = PKCS1_OAEP.new(private_key)
    plain = cipher.decrypt(cipherText)
    print(plain.decode())

def main():
    RSA_read()
  
if __name__ == '__main__':
    main()