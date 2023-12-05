import os

os.system('gcc ising2D.c lib.c -O3 -lm\n')
for i in range(10):
    os.system('./a.out\n')


