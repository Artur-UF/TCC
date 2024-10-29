import os
import fnmatch
import numpy as np
import sys

L = 960
n = 1000


path = 'teste-cls'
samples = fnmatch.filter(list(i.name for i in os.scandir(path)), 'CLS*')

Tcount = []
T = []
D = []
bins = np.logspace(np.log10(1), np.log10(L**2), n)
print(bins)
sys.exit()

newD = []

for file in samples:
    with open(os.path.join(path, file), 'r') as f:
        line = f.readline()
        while line != '':
            if line.split(' ')[0] == '#':
                ttemp = float(line.split(' ')[2])
                if ttemp not in T:
                    Tcount.append(1)
                    T.append(ttemp)
                    D.append(np.zeros(L**2))
                    newD.append(np.zeros(n))
                else:
                    Tcount[T.index(ttemp)] += 1
            else:
                tam = np.log10(int(line.split(' ')[1]))
                for i in range(1, n):
                    if bins[i-1] < tam <= bins[i]:
                        newD[T.index(ttemp)][i] += 1
                D[T.index(ttemp)][int(line.split(' ')[1])] += 1
            line = f.readline()

for j in range(len(T)):
    D[j] = D[j]/Tcount[j]

for j in range(len(T)):
    newD[j] = newD[j]/Tcount[j]

zerocount = 0
distcut = 200
cut = 0

with open(f'Ndistribution-{L}.dat', 'w') as f:
    for i in range(len(T)):
        if i == len(T)-1:
            f.write(f'{T[i]}\n')
        else:
            f.write(f'{T[i]} ')
    for i in range(L**2):
        for j in range(len(T)):
            if j == len(T)-1:
                f.write(f'{D[j][i]}\n')
            else:
                f.write(f'{D[j][i]} ')

            # Cuts the unused bins
            if D[j][i] == 0.0:
                zerocount += 1
            if D[j][i] > 0.0:
                zerocount = 0
            if zerocount > distcut:
                break

        else:
            continue
        break


with open(f'log-distribution-{L}.dat', 'w') as f:
    for i in range(len(T)):
        if i == len(T)-1:
            f.write(f'{T[i]}\n')
        else:
            f.write(f'{T[i]} ')
    for i in range(n):
        for j in range(len(T)):
            if j == len(T)-1:
                f.write(f'{newD[j][i]}\n')
            else:
                f.write(f'{newD[j][i]} ')



