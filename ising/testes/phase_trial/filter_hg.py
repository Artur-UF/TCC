import os
import math
import fnmatch
import sys

L  = int(sys.argv[1])
TI = float(sys.argv[2])
TF = float(sys.argv[3])
dT = float(sys.argv[4])


N = math.ceil((TF-TI)/dT)
T = list(TI+(n*dT) for n in range(N+0))
n = len(T)
H = list(0 for i in range(n))

path = f'hk_{L}_{int(sys.argv[5])}'
samples = fnmatch.filter(list(i.name for i in os.scandir(path)), 'HK*')

i = 0

for file in samples:
    with open(os.path.join(path, file), 'r') as f:
        lines = f.readlines()
        for l in lines:
            if l.split()[0] == '#':
                H[i] += float(l.split()[1])
                i += 1
    i = 0
H = list(H[k]/len(samples) for k in range(n))

with open(path+'.dat', 'w') as f:
    for i in range(len(H)):
        f.write(f'{H[i]} {T[i]}\n') 

