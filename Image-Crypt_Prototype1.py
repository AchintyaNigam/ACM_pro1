import os
from time import sleep

"""May 1 
   9:41 AM
   First I am creating a prototype. I haven't figured the method for encryption yet.
   10:35 AM
   Prototype 1 is Complete! the encryption is very weak and consists of only an XOR operation.
   I will research and think of better encryption.
"""


def get_key():
    keyf = int(input("Enter the key for encryption: "))
    return keyf


def get_path():
    p = input("Enter the path: ")
    return p


def get_image(pathf):  # to open file and get a bytearray
    fileR = open(pathf, 'rb') #In 'FileR', 'R' stands for read and 'f' in 'pathf' is for function
    image_file = fileR.read()
    barr = bytearray(image_file)
    fileR.close()
    return barr


def encrypt_or_decrypt(image_lstf, keyf2, pathf2):
    for index, values in enumerate(image_lstf):
        image_lstf[index] = values ^ keyf2
    fileW = open(pathf2, 'wb')
    fileW.write(image_lstf)
    fileW.close()
    return



def encryption_mode():
    path = get_path()
    if not os.path.exists(path):  # Edge case 1
        print("File not found!")
    else:
        key = get_key()
        image_lst = get_image(path)
        print("Encrypting...")
        sleep(1)
        encrypt_or_decrypt(image_lst, key, path)
        print("Encryption complete.")

def decryption_mode():
    path = get_path()
    if not os.path.exists(path):  # Edge case 1
        print("File not found!")
    else:
        key = get_key()
        image_lst = get_image(path)
        print("decrypting...")
        sleep(1)
        encrypt_or_decrypt(image_lst, key, path)
        print("decryption complete.")

def driver_func():
    ch = 'y'
    while ch.lower() != 'n':
        e_or_d = input("Type 1 for encryption and 2 for decryption: ")
        if e_or_d == '1':
            encryption_mode()
            ch = input("Do you want to continue?(y/n): ")
        elif e_or_d == '2':
            decryption_mode()
            ch = input("Do you want to continue?(y/n): ")
        else:
            print("Invalid choice! please try again!")

driver_func()
