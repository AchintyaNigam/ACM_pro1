import os
import random
from time import sleep

"""May 1 
   9:41 AM
   First I am creating a prototype. I haven't figured the method for encryption yet.
   10:35 AM
   Prototype 1 is Complete! the encryption is very weak and consists of only an XOR operation.
   I will research and think of better encryption.
   (After this the first commit was made)
   11:16 AM
   I have done some research and have realised that it will be better if we generate a key ourselves 
   and then encrypt the file. The only problem is storing the key safely so that we can decrypt it later.
   This will also include maintaining a list of encrypted files.
   2:36 PM
   better encryption has been added. it is still using a symmetric key, But the key can no longer be brute forced.
   I need to find a way to hide the file that stores the names and keys for files 
   
"""


def generate_key():
    chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ]
    key_A = ''
    for i in range(25):
        key_A += random.choice(chars)
    return key_A


def get_key():
    keyf = int(input("Enter the key for encryption: "))
    return keyf


def get_path():
    p = input("Enter the path: ")
    return p


def get_image(pathf):  # to open file and get a bytearray
    fileR = open(pathf, 'rb')  # In 'FileR', 'R' stands for read and 'f' in 'pathf' is for function
    image_file = fileR.read()
    barr = bytearray(image_file)
    fileR.close()
    return barr


def remove_next_line(data):
    for i in data:
        data[data.index(i)] = i.replace('\n', '')


def operation(data, key):
    j = 0
    i = 0
    for index, values in enumerate(data):
            data[index] = values ^ int(key[j])
            if(j == 24 and i != (len(data)-1)):
                j = 0
                j += 1
            else:
                j += 1
                i += 1


def encrypt(image_lstf, keyf2, pathf2):
    file_name = os.path.basename(pathf2)
    encrypt_save_file = open('.encrypt_save_file.txt', 'r')
    file_names = encrypt_save_file.readlines()
    remove_next_line(file_names)

    for i in file_names:
        if file_name == i:
            print("file has already been encrypted!")
            encrypt_save_file.close()
            return
    encrypt_save_file.close()
    encrypt_save_file = open('.encrypt_save_file.txt', 'a')
    encrypt_save_file.write(file_name + '\n')
    encrypt_save_file.write(keyf2 + '\n')
    encrypt_save_file.close()

    operation(image_lstf, keyf2)

    fileW = open(pathf2, 'wb')
    fileW.write(image_lstf)
    fileW.close()
    return


def decrypt(image_lstf2, pathf3):
    file_name2 = os.path.basename(pathf3)
    encrypt_save_file2 = open('.encrypt_save_file.txt', 'r')
    file_names2 = encrypt_save_file2.readlines()
    remove_next_line(file_names2)
    fcount = 1

    for i in file_names2:
        if file_name2 == i:
            keyf3 = file_names2[file_names2.index(i) + 1]
            delete_index = file_names2.index(i)
            s_delete_index = delete_index + 1
            fcount = 0
    encrypt_save_file2.close()

    if fcount == 0:
        encrypt_save_file2 = open('.encrypt_save_file.txt', 'r')
        lines = encrypt_save_file2.readlines()
        encrypt_save_file2.close()
        encrypt_save_file2 = open('.encrypt_save_file.txt', 'w')

        del lines[delete_index-1]
        del lines[delete_index-1]
        encrypt_save_file2.writelines(lines)

        encrypt_save_file2.close()


        operation(image_lstf2, keyf3)

        fileW = open(pathf3, 'wb')
        fileW.write(image_lstf2)
        fileW.close()
        print("decryption complete.")
    else:
        print("File has not been encrypted!")
    return


def encryption_mode():
    path = get_path()
    if not os.path.exists(path):
        print("File not found!")
    else:
        key = generate_key()
        image_lst = get_image(path)
        print("Encrypting...")
        sleep(1)
        encrypt(image_lst, key, path)
        print("Encryption complete.")


def decryption_mode():
    path = get_path()
    if not os.path.exists(path):
        print("File not found!")
    else:
        image_lst = get_image(path)
        print("decrypting...")
        sleep(1)
        decrypt(image_lst, path)


def driver_func():
    ch = 'y'
    if not os.path.exists('.encrypt_save_file.txt'):
        save_file = open('.encrypt_save_file.txt', 'w')
        save_file.close()
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
