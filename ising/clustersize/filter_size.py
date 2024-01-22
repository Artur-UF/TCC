import os
import math
import fnmatch

L = 160
TI = 2.1
TF = 2.8
dT = 0.01


L2 = L**2
N = math.ceil((TF-TI)/dT)
T = list(TI+(n*dT) for n in range(N+1))
n = len(T)
CLS = list(0 for i in range(N+1))

print(T)
print(len(T))
print(CLS)
print(len(CLS))

path = f'hksize_teste' #{L}'
samples = fnmatch.filter(list(i.name for i in os.scandir(path)), 'CLS*')
#print(samples)

t = 0

for file in samples:
    l = list()
    s = 0
    t = 0
    with open(os.path.join(path, file), 'r') as f:
        lines = f.readlines()
        for li in range(len(lines)):
            l.append(int(lines[li].split(' ')[0]))
            s += int(lines[li].split(' ')[1])
            if s == L2:
                CLS[t] += L2/len(l)
                l.clear()
                s = 0
                t += 1

CLS = list(CLS[i]/len(samples) for i in range(n))

with open(path+'.dat', 'w') as f:
    for j in range(n):
        f.write(f'{CLS[j]}\n')

