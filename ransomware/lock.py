#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

#find all files

files = []
for file in os.listdir():
    if file =="lock.py":
        continue
    if os.path.isfile(file):
        files.append(file)
    
print(files)


key = Fernet.generate_key()

with open("secret.key","wb") as secret:
    secret.write(key)