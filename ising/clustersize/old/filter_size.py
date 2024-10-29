import os
import math
import fnmatch

L = 800
TI = 2.1
TF = 2.8
dT = 0.02


L2 = L**2
N = math.ceil((TF-TI)/dT)
T = list(TI+(n*dT) for n in range(N+1))
n = len(T)
CLS = list(0 for i in range(N+1))

path = f'clsize_{L}'
samples = fnmatch.filter(list(i.name for i in os.scandir(path)), 'CLS*')

for fi in samples:
    ltotal = 0
    laux = 0
    l1 = 0
    s1 = 0
    stotal = 0
    t = 0
    with open(os.path.join(path, fi), 'r') as f:
        lines = f.readlines()
        for li in range(len(lines)):
            l1, s1 = list(map(lambda x: int(x), lines[li].split(' ')))
            if l1 >= laux and s1 > 1:
                laux = l1
                ltotal += 1
                stotal += s1
            if l1 < laux:
                CLS[t] += stotal/ltotal
                laux, ltotal, stotal = 0, 0, 0
                t += 1

CLS = list(CLS[i]/len(samples) for i in range(n))

with open(path+'.dat', 'w') as f:
    for j in range(n):
        f.write(f'{CLS[j]} {T[j]:.4f}\n')

