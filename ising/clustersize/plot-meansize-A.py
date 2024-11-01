import matplotlib.pyplot as plt
import numpy as np
from glob import glob
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 20})

files = ['mean_A_L_1500.dat', 'mean_A_L_1000.dat', 'mean_A_L_320.dat']


fig, ax = plt.subplots(1, 2, figsize=(12, 6), layout='constrained')


markers = ['s', '^', '*']
colors = ['r', 'g', 'purple']

for i in range(len(files)):
    L = int(files[i].split('_')[-1].split('.')[0])

plt.subplot(121)
T, A = np.loadtxt(files[2], unpack=True)
plt.plot(T, A, c=colors[2], marker=markers[2], markersize=2, label=f'L = 320')

T, A = np.loadtxt(files[1], unpack=True)
plt.plot(T, A, c=colors[1], marker=markers[1], markersize=2, label=f'1000')

T, A = np.loadtxt(files[0], unpack=True)
plt.plot(T, A, c=colors[0], marker=markers[0], markersize=2, label=f'1500')

plt.ylabel(r'$\left \langle A \right \rangle $')
plt.xlabel(r'$T$')
plt.legend()
plt.vlines([2.2691, 2.567], 60, 100, linestyles='dashed', colors=['k', 'gray'], linewidth=.7, zorder=1)
plt.yticks([60, 70, 80, 90, 100], [60, 70, 80, 90, 100])
plt.ylim(60, 100)
plt.xlim(2.1, 2.8)

plt.subplot(122)
T, A = np.loadtxt(files[2], unpack=True)
plt.plot(T, np.gradient(np.gradient(A)), c=colors[2], marker=markers[2], markersize=2, label=f'L = 320')

T, A = np.loadtxt(files[1], unpack=True)
plt.plot(T, np.gradient(np.gradient(A)), c=colors[1], marker=markers[1], markersize=2, label=f'1000')

T, A = np.loadtxt(files[0], unpack=True)
plt.plot(T, np.gradient(np.gradient(A)), c=colors[0], marker=markers[0], markersize=2, label=f'1500')

plt.ylabel(r'$d^2\left \langle A \right \rangle/dT^2$')
plt.xlabel(r'$T$')
plt.legend()
plt.hlines(0, 2.1, 2.8, colors='k', linewidth=.9, zorder=0)
plt.vlines([2.2691, 2.567], -0.3, 0.6, linestyles='dashed', colors=['k', 'gray'], linewidth=.7, zorder=1)
plt.yticks([-0.3, -0.1, 0, 0.2, 0.5], [-0.3, -0.1, 0, 0.2, 0.5])
plt.ylim(-0.3, 0.6)
plt.xlim(2.1, 2.8)

left, bottom, width, height = [0.736, 0.5, 0.2, 0.2]
ax2 = fig.add_axes([left, bottom, width, height])

t, a = np.loadtxt('zoom-A-320.dat', unpack=True)
cut = 2
ax2.plot(t[cut:-cut], np.gradient(np.gradient(a))[cut:-cut], c=colors[2])
ax2.vlines(2.567, -0.1, 0.05, linestyles='dashed', colors='gray', linewidth=.7, zorder=1)
ax2.set(ylim=(-0.1, 0.05), xlim=(2.4, 2.7))
ax2.hlines(0, 2.4, 2.7, colors='k', linewidth=.9, zorder=0)

plt.savefig('new-A.png', dpi=400)




