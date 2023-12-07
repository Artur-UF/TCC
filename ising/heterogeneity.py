import numpy as np
import matplotlib.pyplot as plt
import glob
import os
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 12})


L = [100, 150]
TI = 1.
TF = 10.
dT = 0.5

T = np.arange(TI, TF+dT, dT)
n = len(T)
H = list(np.zeros(n) for i in range(2))

for j in range(len(L)):
    path = f'samples_L_{L[j]}'
    samples = glob.glob('HK*', root_dir=path)
    
    i = 0
    
    for file in samples:
        with open(os.path.join(path, file), 'r') as f:
            lines = f.readlines()
            for l in lines:
                if l.split()[0] == '#':
                    H[j][i] += float(l.split()[1])
                    i += 1
        i = 0
    H[j] /= len(samples)

plt.figure(layout='constrained')
plt.plot(T, H[0], 'k--', label='L = 100')
plt.plot(T, H[1], 'r--', label='L = 150')
plt.vlines(2.269, 0, 120, linewidth=.7)
plt.legend()
plt.xlabel(r'$T$')
plt.ylabel(r'$H_{g}$')
plt.grid()
plt.savefig('hetero.png', dpi=400)

