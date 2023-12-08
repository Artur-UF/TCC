#!/usr/bin/python3
import os

os.system('gcc ising2D.c lib.c -O3 -lm\n')
for i in range(10):
    print(f'Sample: {i+1}')
    os.system('./a.out\n')
print()

