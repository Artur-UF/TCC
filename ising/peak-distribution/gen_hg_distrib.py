import fnmatch
import os
import numpy as np

L = 3500

path = f'dense-hg-{L}/'
samples = fnmatch.filter(list(i.name for i in os.scandir(path)), 'HK*')

Tp = 3.3

bins = np.zeros(L)
c = 0

for i in range(len(samples)):
    with open(path+samples[i], 'r') as f:
        line = f.readline()
        while line != '':
            if line.split(' ')[0] == '#':
                if float(line.split(' ')[2]) == Tp:
                    bins[int(line.split(' ')[1])] += 1
            line = f.readline()

with open(f'hg-distri_{L}_{Tp}_.dat', 'w') as f:
    for i in np.where(bins > 0)[0]:
        f.write(f'{i} {bins[i]}\n')

