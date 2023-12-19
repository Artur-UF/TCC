import os
import math
import fnmatch

L = 160
TI = 1.
TF = 10.
dT = 0.5


N = math.ceil((TF-TI)/dT)
T = list(TI+(n*dT) for n in range(N+1))
n = len(T)
H = list(0 for i in range(n))

path = f'samples_L_{L}'
samples = fnmatch.filter(list(i.name for i in os.scandir(path)), 'HK*')
print(samples)

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

with open(f'Hg_L_{L}.dat', 'w') as f:
    for i in range(len(H)):
        f.write(f'{H[i]}\n') 

