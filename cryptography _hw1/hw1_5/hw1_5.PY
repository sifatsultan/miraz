import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


# Set up cryptographic backend
backend = default_backend()
bs = 32


def encryptMsg(iv):
    # get {messageFileName} from user
    messageFileName = input("Enter filename that contains [message] ")
    # get {keyFileName} from user
    keyFileName = input("Enter the filename that contais [key] ")

    # read message from file
    # save it in {message}
    f = open(messageFileName,'rb')
    message = f.read()
    f.close()

    # read key from file
    # save it in {key}
    f = open(keyFileName, 'rb')
    key = f.read()
    f.close()
    
    # Create cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)

    # Create encryptor object
    encryptor = cipher.encryptor()

    # Encrypt message
    cipherText = encryptor.update(message) + encryptor.finalize()

    # Save the ciphertext to file
    f = open('cipherText.txt','wb')
    f.write(cipherText)
    f.close()

    # print the encrypted msg
    print ("The ciphertext is: ", cipherText)
    return cipherText


def decryptMsg(iv):
    
    # get {cipherTextFileName} from user
    cipherTextFileName = input("Enter filename that contains [cipherText] ")
    # get {keyFileName} from user
    keyFileName = input("Enter the filename that contais [key] ")

    # read cipherText from file
    # save it in {cipherText}
    f = open(cipherTextFileName,'rb')
    cipherText = f.read()
    f.close()

    # read key from file
    # save it in {key}
    f = open(keyFileName, 'rb')
    key = f.read()
    f.close()


    # Create cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)

    # Create decryptor object
    decryptor = cipher.decryptor()
    
    secretMessage = decryptor.update(cipherText) + decryptor.finalize()
    print(secretMessage)
    


# key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'


def main():
    key = os.urandom(16)
    iv = os.urandom(16)

    # write the key to file
    f = open('key.txt','wb')
    f.write(key)
    f.close()

    secret_msg = b"a secret message"
    # save message to text file to simulate received
    # msg
    f = open('msg.txt','wb')
    f.write(secret_msg)
    f.close()
    

    while True:
        userInput = input("would you like to encryp or decrypt? ")
        if userInput == "e":
            print("encryption begins")
            # secret_message = input("Enter the secret message")
            ciphertext = encryptMsg(iv)
            print(ciphertext)
        elif userInput == "d":
            print ("decryption begins")
            decryptMsg(iv)
        else:
            print("choose between d and e")
main()

