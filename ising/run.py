#!/usr/bin/python3
import os
import sys

AMOSTRAS = int(sys.argv[1])

os.system('make out')

for i in range(AMOSTRAS):
    os.system('./out_size')
print()


os.system('make clean')

