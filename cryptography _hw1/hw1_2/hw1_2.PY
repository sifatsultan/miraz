
# Import modules as required
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Set up cryptographic backend
backend = default_backend()

# Initializing block size
BLOCK_SIZE=32


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

    #save the ct, iv and key in file
    saveDetails(iv,key,cipherText)
    
    #print (key)
    #print (iv)


# save the IV ,ct and  key in textfile
def saveDetails(iv, key, ct):
    # open file objec with filename 
    f1 = open('iv.txt', 'w')
    f2 = open('key.txt','w')
    f3 = open('ct.txt','w')

    # write the ct to file
    f3.write(str(ct))

    # write the key in the file
    f2.write(str(key))

    # write the iv in the file
    f1.write(str(iv))

    # close the file objects
    f1.close()
    f2.close()
    f3.close()
    
    print("CipherText saved succesfully")


def saveCipherText(ct):
    f = open('data.txt', 'w')
    f.write(str(ct))
    f.close()
    print("CipherText saved succesfully")

def readCipherText():
    f = open('data.txt','r')
    ct = f.read()
    f.close()
    return str.encode('utf-8')
    print("CiptherText saved unsuccesfully")
    


def readFromFile(fileName):
    # read the content of file
    f = open(fileName, 'r')

    # read the text from file and put in variable {content}
    content = f.read()

    # close the {f}ile
    f.close()

    # convert the context to bytes and return it
    return content.encode('utf-8')
    



def decryptMsg():
    ct= readFromFile('ct.txt')
    key= readFromFile('key.txt')
    iv= readFromFile('iv.txt')

    print(key)

    # Create cipher object
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=backend)
    
     # Create decryptor object
    decryptor = cipher.decryptor()

    # Decrypt message
    output = decryptor.update(ct) + decryptor.finalize()

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

