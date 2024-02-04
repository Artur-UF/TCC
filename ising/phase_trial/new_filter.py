import os
import math
import fnmatch
import sys
import numpy as np

L  = int(sys.argv[1])
TI = float(sys.argv[2])
TF = float(sys.argv[3])
dT = float(sys.argv[4])

T = np.arange(TI, TF+dT, dT)
H = np.zeros(len(T))

print(T)

path = f'hk_{L}_{int(sys.argv[5])}'
samples = fnmatch.filter(list(i.name for i in os.scandir(path)), 'HK*')


for file in samples:
    hg = np.loadtxt(os.path.join(path, file), usecols=1, comments=None, unpack=True)
    H += hg
H /= len(samples)

with open(path+'.dat', 'w') as f:
    for i in range(len(H)):
        f.write(f'{H[i]} {T[i]}\n') 

