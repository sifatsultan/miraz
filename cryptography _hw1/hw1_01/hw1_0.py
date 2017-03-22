
# Import modules as required
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Set up cryptographic backend
backend = default_backend()

def saveContent(filename,content):
    filename = filename + '.txt'
    f = open(filename, 'wb')
    f.write(content)
    f.close()

def readContent(filename):
    filename = filename + '.txt'
    f = open(filename,'rb')
    content = f.read()
    f.close()
    return content

# Function
# Encrypt the message
def encryptMsg(iv):
          
    # Prompt user to choose between new or existing key
    userKeyChoice = input("Go for (e)xisting key or (n)ew key?")

    # User opts for Exiting Key
    if userKeyChoice == 'e':
        # open textfile to read existing key
        try:
            key = readContent('key')

            # Create cipher object
            cipher = Cipher(algorithms.AES(key), modes.CRT(iv), backend=backend)

            # Create Encryptor Object
            encryptor = cipher.encryptor()

            # Encrypt Message
            cipherText = encryptor.update(b"a secret message") + encryptor.finalize()

            saveContent('cipherText',cipherText)

            # Print the Encrypted Msg
            print ("The ciphertext is:", cipherText)

            decryptMsg(cipherText)
            
        except:
            print("There is no existing key")
        
    # User Opts for New Key
    elif userKeyChoice == 'n':
        # initialize key from random data
        key = os.urandom(16)

        saveContent('key',key)

        # Create cipher object
        cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=backend)

        # Create encryptor object
        encryptor = cipher.encryptor()

        # Encrypt message
        cipherText = encryptor.update(b"a secret message") + encryptor.finalize()

        saveContent('cipherText',cipherText)

        #print the encrypted msg
        print ("The ciphertext is: ", cipherText)
        
        return cipherText
        


# Function
# Decrypt the message
def decryptMsg(iv):

    cipherTextFileName = input('Enter file name for [cipherText] ')
    keyFileName = input('Enter file name for [keyFileName] ')

    key = readContent(keyFileName)
    cipherText = readContent(cipherTextFileName)

    # Create cipher object
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=backend)

    # Create decryptor object
    decryptor = cipher.decryptor()
    
    # Decrypt message
    output = decryptor.update(cipherText) + decryptor.finalize()

    # Print decrypted message
    print("The decrypted msg: ",output)



def main():
    # Intialize IV from random data
    iv = os.urandom(8)
    
    while True:
        userInput = input("would you like to encryp or decrypt")
        if userInput == "e":
            print("encryption begins")
            encryptMsg(iv)
        elif userInput == "d":
            print ("decryption begins")
            decryptMsg(iv)
        else:
            print("choose between d and e")
main()
