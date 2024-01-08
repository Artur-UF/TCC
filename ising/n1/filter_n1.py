import os
import math
import fnmatch

L = 500
TI = 0.
TF = 0.
dT = 0.5


N = math.ceil((TF-TI)/dT)
T = list(TI+(n*dT) for n in range(N+1))
n = len(T)
n1 = list(0 for i in range(n))

path = f'smpl_500'
samples = fnmatch.filter(list(i.name for i in os.scandir(path)), 'n1*')
#print(samples)

i = 0

for file in samples:
    with open(os.path.join(path, file), 'r') as f:
        lines = f.readlines()
        for l in lines:
            n1[i] += float(l)
            i += 1
    i = 0
n1 = list(n1[k]/len(samples) for k in range(n))

with open(f'n1_L_{L}.dat', 'w') as f:
    for i in range(len(n1)):
        f.write(f'{n1[i]}\n') 

