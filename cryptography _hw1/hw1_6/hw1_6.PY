# Import modules as required
import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Set up cryptographic backend
backend = default_backend()

def encryptMsg():
    key = os.urandom(16)
    iv = os.urandom(16)
    
    message=input("Enter message to encrypt: ")
    message=message.encode()
    
    # create cipher object with Algorithm AES and mode CTR
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=backend)

    # Create encryptor object
    encryptor = cipher.encryptor()

    # Encrypt message
    cipherText = encryptor.update(message) + encryptor.finalize()

    #print the encrypted msg, key and iv in hex format
    print ("The ciphertext is: ", cipherText.hex())
    print ("The key is: ", key.hex())
    print ("The IV is: ",iv.hex())



def decryptMsg():

    cipherText= input("Enter the ciphertext: ")
    key=input("Enter the key: " )
    iv=input("Enter the iv: " )

    #converting to bytes  
    key=bytes.fromhex(key)
    cipherText=bytes.fromhex(cipherText)
    iv=bytes.fromhex(iv)

    # create cipher object with Algorithm AES and mode CTR
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=backend)

     # Create decryptor object
    decryptor = cipher.decryptor()

    # Decrypt message
    output = decryptor.update(cipherText) + decryptor.finalize()

    #Print decrypted message
    print(output)

def main():
    while True:
        userInput = input("would you like to encryp or decrypt? ")
        if userInput == "e":
            print("encryption begins")
            encryptMsg()
        elif userInput == "d":
            print ("decryption begins")
            decryptMsg()
        else:
            print("choose between d and e")
main()

