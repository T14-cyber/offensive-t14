#!/usr/bin/env python3
import os


#find all files

files = []
for file in os.listdir():
    if file =="lock.py":
        continue
    files.append(file)
    
print(files)