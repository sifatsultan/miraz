
# Import modules as required
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Set up cryptographic backend
backend = default_backend()


# Initialise keys & IV from random data


def encryptMsg():
    key = os.urandom(16)
    iv = os.urandom(16)
    
    message=input("Enter message to encrypt: ")
    # Create cipher object
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=backend)

    # Create encryptor object
    encryptor = cipher.encryptor()

    # Encrypt message
    cipherText = encryptor.update(b"message") + encryptor.finalize()

    #print the encrypted msg
    print ("The ciphertext is: ", cipherText)
    print (key)
    print (iv)

    


def decryptMsg():

    cipherText= input("Enter the ciphertext: ")
    key=input("Enter the key: " )
    iv=input("Enter the iv: " )

     # Create decryptor object
    decryptor = cipherText.decryptor()

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

