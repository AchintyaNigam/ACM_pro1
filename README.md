# Image-Crypt

## An image encryption and decryption project
This is a menu-driven program that encrypts your image with a very secure key (cannot be brute forced in an optimal amount of time)
and decrypts it as well!
It also keeps track of the files you encrypt.
Currently, due to a lack of time, it does not have a GUI.
I hope you like it!

---

## How to use it?
- It will ask you what is it that you want to do: 1 for encryption and 2 for decryption
- If you clicked 1 then it will ask you to enter the path of the image file you want to encrypt.
  - if the file is found it will start encrypting and if the file is **not** found, then it will display that file was not found
  - then will ask you if you want to continue. entering y/Y will take you back to the menu and n/N will end the program
  - if the file was already encrypted it will display the same and ask you if you want to continue.
  - after encryption has been completed, the program will ask if you want to continue.
- If you clicked 2 then it will ask you to enter the path of the image file you want to decrypt.
  - if the file is found it will start decrypting and if the file is **not** found, then it will display that file was not found
  - then it will ask you if you want to continue. entering y/Y will take you back to the menu and n/N will end the program
  - if the file was not encrypted it will display the same and ask you if you want to continue.
  - after decryption has been completed, the program will ask if you want to continue.
 
---

## How does it work
The encryption and decryption algorithm is the same and uses an automatically generated, 25 character key./
Each digit of the key is exclusive-ored with each element of the byte array of the image and the process is repeated until we reach the 
end of the byte array.\
for example:\
let us have a byte array (say) [1,4,72,81,9,7,89,37] (An actual byte array of an image will be much larger)\
and we have a key (say) 987 (the actual key will be 25 characters long)\
then 9 will be exclusive-ored with 1\
then 8 with 4\
then 7 with 72\
then again 9 with 81\
then 8 with 9\
then 7 with 7\
then again 9 with 89\
and finally 8 with 37.\
and each of the results will replace the element it was the ex-or result of in the byte array.\

The name of the file and the key are stored in a hidden file and can be accessed later by the program even if you close the program.

---

## Problems

The major issue is that the keys along with their associated file names are being stored in an unsecured file. Although the file is 'hidden',
it can be accessed by anyone using the machine containing the program. this can be secured by further encrypting the key file but that would mean
storing that key inside the program itself...

---

### And that's it! Thank you for reading!
