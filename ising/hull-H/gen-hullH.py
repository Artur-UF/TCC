import fnmatch
import os

L = 640

path = f'hullH-{L}/'
samples = fnmatch.filter(list(i.name for i in os.scandir(path)), 'HULLH*')


T = []
Tcount = []
HH = []

for i in range(len(samples)):
    with open(path+samples[i], 'r') as f:
        line = f.readline()
        while line != '':
            t = float(line.split(' ')[0])
            hh = int(line.split(' ')[1])
            if t not in T:
                T.append(t)
                Tcount.append(1)
                HH.append(hh)
            else:
                Tcount[T.index(t)] += 1
                HH[T.index(t)] += hh
            line = f.readline()


HH = list(HH[i]/Tcount[i] for i in range(len(Tcount)))

T = T[::-1]
HH = HH[::-1]

with open(f'hh_{L}_.dat', 'w') as f:
    for i in range(len(HH)):
        f.write(f'{T[i]} {HH[i]}\n')

