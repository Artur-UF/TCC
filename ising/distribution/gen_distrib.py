import os
import fnmatch
import numpy as np

L = 500
n = 200

path = 'teste-distri'
samples = fnmatch.filter(list(i.name for i in os.scandir(path)), 'DIST*')

Tcount = []
T = []
D = []
linbins = np.arange(0, L**2)
logbins = np.logspace(np.log10(1), np.log10(L**2), n)

newD = []

for file in samples:
    with open(os.path.join(path, file), 'r') as f:
        line = f.readline()
        while line != '':
            if line.split(' ')[0] == '#':
                ttemp = float(line.split(' ')[1])
                if ttemp not in T:
                    Tcount.append(1)
                    T.append(ttemp)
                    D.append(np.zeros(L**2))
                    newD.append(np.zeros(n))
                else:
                    Tcount[T.index(ttemp)] += 1
            else:
                tam = int(line.split(' ')[0])
                freq = float(line.split(' ')[1].split(r'\n')[0])
                for i in range(1, n):
                    if logbins[i-1] < tam <= logbins[i]:
                        newD[T.index(ttemp)][i] += freq
                D[T.index(ttemp)][tam] += freq
            line = f.readline()

for j in range(len(T)):
    D[j] = D[j]/Tcount[j]

for j in range(len(T)):
    newD[j] = newD[j]/Tcount[j]

for i in range(len(T)):
    with open(f'linear-distribution-L_{L}_T_{T[i]}_.dat', 'w') as f:
        for j in np.where(D[i] > 0)[0]:
            if D[i][j] > 0:
                f.write(f'{linbins[j]} {D[i][j]}\n')

    with open(f'log-distribution-L_{L}_T_{T[i]}_.dat', 'w') as f:
        for j in np.where(newD[i] > 0)[0]:
            f.write(f'{logbins[j]} {newD[i][j]}\n')

