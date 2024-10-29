import os
import fnmatch

L = 50

inverted = 1

path = 'teste-A'
samples = fnmatch.filter(list(i.name for i in os.scandir(path)), 'A_*')

Tcount = []
T = []
A = []

for s in samples:
    with open(os.path.join(path, s), 'r') as f:
        line = f.readline()
        while line != '':
            taux = float(line.split(' ')[0])
            Aaux = float(line.split(' ')[1])
            if taux not in T:
                T.append(taux)
                Tcount.append(1)
                A.append(Aaux)
            else:
                A[T.index(taux)] += Aaux
                Tcount[T.index(taux)] += 1
            line = f.readline()

A = list(A[i]/Tcount[i] for i in range(len(T)))

if inverted:
    A = A[::-1]
    T = T[::-1]

with open(f'mean_A_L_{L}.dat', 'w') as f:
    for i in range(len(T)): f.write(f'{T[i]} {A[i]}\n')

