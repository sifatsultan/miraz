
# Import modules as required
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Set up cryptographic backend
backend = default_backend()


global cipherText
# promp user encrypt or decryp
global key



def saveCipherText(ct):
    f = open('data.txt', 'w')
    f.write(str(ct))
    f.close()
    print("CipherText saved succesfully")

def readCipherText():
    f = open('data.txt','r')
    ct = f.read()
    f.close()
    return ct.encode('utf-8')
    print("CiptherText saved unsuccesfully")

# Function
# Encrypt the message
def encryptMsg():
          
    # Prompt user to choose between new or existing key
    userKeyChoice = input("Go for (e)xisting key or (n)ew key?")

    # Intialize IV from random data
    iv = os.urandom(8)

    # User opts for Exiting Key
    if userKeyChoice == 'e':
        # open textfile to read existing key
        try:
            f = open('data.txt','r')
            global key
            key = f.read()
            f.close()

            # Create cipher object
            cipher = Cipher(algorithms.AES(key), modes.CRT(iv), backend=backend)

            # Create Encryptor Object
            encryptor = cipher.encryptor()

            # Encrypt Message
            cipherText = encryptor.update(b"a secret message") + encryptor.finalize()

            # Save CipherText in a Text file
            # saveCipherText(cipherText)

            # Print the Encrypted Msg
            print ("The ciphertext is:", cipherText)

            decryptMsg(cipherText)
        
            
            #return cipherText
            
        except:
            print("There is no existing key")
        
    # User Opts for New Key
    elif userKeyChoice == 'n':
        # initialize key from random data
        key = os.urandom(16)

        # Create cipher object
        cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=backend)

        # Create encryptor object
        encryptor = cipher.encryptor()

        # Encrypt message
        cipherText = encryptor.update(b"a secret message") + encryptor.finalize()

        #print the encrypted msg
        print ("The ciphertext is: ", cipherText)

        decryptMsg(cipherText, key,iv)

        return cipherText
        


# Function
# Decrypt the message
def decryptMsg(cipherText,key,iv):
    # Initialise keys & IV from random data
    #key = os.urandom(16)
    #iv = os.urandom(8)

    # Create cipher object
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=backend)

    # Create decryptor object
    decryptor = cipher.decryptor()

    # Get CipherText
    #cipherText =  readCipherText()
    
    
    # Decrypt message
    output = decryptor.update(cipherText) + decryptor.finalize()

    # Print decrypted message
    print("The decrypted msg: ",output)



def main():
    while True:
        userInput = input("would you like to encryp or decrypt")
        if userInput == "e":
            print("encryption begins")
            encryptMsg()
        elif userInput == "d":
            print ("decryption begins")
            decryptMsg()
        else:
            print("choose between d and e")
main()
