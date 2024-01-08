#!/usr/bin/python3
import os

os.system('make out')

for i in range(100):
    print(f'Sample: {i+1}')
    os.system('./out')
print()
os.system('make clean')

