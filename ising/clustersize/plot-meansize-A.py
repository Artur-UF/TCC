import matplotlib.pyplot as plt
import numpy as np
from glob import glob


files = sorted(glob('mean*'))


fig, ax = plt.subplots(1, 2, figsize=(12, 4), layout='constrained')


markers = ['s', '^', '*']
colors = ['r', 'g', 'purple']

for i in range(len(files)):
    T, A = np.loadtxt(files[i], unpack=True)
    L = int(files[i].split('_')[-1].split('.')[0])
    plt.subplot(121)
    plt.plot(T, A, c=colors[i], marker=markers[i], markersize=2, label=f'L = {L}')
    plt.subplot(122)
    plt.plot(T, np.gradient(A), c=colors[i], marker=markers[i], markersize=2, label=f'L = {L}')

plt.subplot(121)
plt.ylabel(r'$\left \langle A \right \rangle $')
plt.xlabel(r'$T$')
plt.legend()

plt.subplot(122)
plt.ylabel(r'$d\left \langle A \right \rangle/dT$')
plt.xlabel(r'$T$')
plt.legend()

plt.savefig('A.png', dpi=400)




