import numpy as np


L = 960

hg, h2, t = np.loadtxt(f'Hg_{L}_.dat', unpack=True)
densehg, denseh2, denset = np.loadtxt(f'dense-Hg_{L}_.dat', unpack=True)

c = 0
ver = True

with open(f'Hg_{L}_.dat', 'w') as f:
    for i in range(len(t)):
        if ver and denset[c] < t[i]:
            f.write(f'{densehg[c]} {denseh2[c]} {denset[c]}\n')
            c += 1
            if c == len(denset)-1:
                ver = False

        f.write(f'{hg[i]} {h2[i]} {t[i]}\n')

        if ver and denset[c] < t[i+1]:
            f.write(f'{densehg[c]} {denseh2[c]} {denset[c]}\n')
            c += 1
            if c == len(denset)-1:
                ver = False

