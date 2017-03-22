
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
    
    message = input("Enter message to encrypt: ")
    message_padded = pad(message)
    # Create cipher object
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=backend)

    # Create encryptor object
    encryptor = cipher.encryptor()

    # Encrypt message
    cipherText = encryptor.update(message_padded) + encryptor.finalize()

    #print the encrypted msg
    print ("The ciphertext is: ", cipherText)
 
    #save the ct, iv and key in file
    #saveDetails(iv,key,cipherText)


    # dict = {'iv':iv, 'key':key, 'cipherText':cipherText}
    # save_changes(dict)
    
    #print (key)
    #print (iv)


# save the IV ,ct and  key in textfile
def saveDetails(iv, key, ct):
    # open file objec with filename 
    f1 = open('iv.txt', 'wb')
    f2 = open('key.txt','wb')
    f3 = open('ct.txt','wb')

    # print('IV Type: ',type(iv))

    # print('Key type: ', type(key))

    # print('CT Type: ', type(ct))
    # print('CT Convrted to String Type: ', type(str(ct)))

    # write the ct to file
    f3.write(ct)

    # write the key in the file
    f2.write(key)

    # write the iv in the file
    f1.write(iv)

    # close the file objects
    f1.close()
    f2.close()
    f3.close()
    
    print("CipherText saved succesfully")


def readFromFile(fileName):
    # read the content of file
    f = open(fileName, 'rb')

    # read the text from file and put in variable {content}
    content = f.read()

    # close the {f}ile
    f.close()

    # convert the context to bytes and return it
    return str.encode(content)



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
    key = os.urandom(16)
    iv = os.urandom(16)

    while True:
        userInput = input("would you like to encryp or decrypt? ")
        if userInput == "e":
            print("encryption begins")
            # secret_message = input("Enter the secret message")
            cipertext = encryptMsg()
            print(ciphertext)
        elif userInput == "d":
            print ("decryption begins")
            decryptMsg()
        else:
            print("choose between d and e")
main()

