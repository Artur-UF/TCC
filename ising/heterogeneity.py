#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 12})


L = [160, 320, 640]
TI = 1.
TF = 10.
dT = 0.5
T = np.arange(TI, TF+dT, dT)

H = list()
for l in range(len(L)):
    H.append(np.loadtxt(f'Hg_L_{L[l]}.dat'))

fig, ax = plt.subplots(1, 1, layout='constrained')
for i in range(len(L)):
    plt.plot(T, H[i], linewidth=.8, marker='>', label=f'L = {L[i]}')
plt.vlines(2.269, 0, max(H[-1])+10, colors='k', linewidth=.7)
plt.legend()
plt.xscale('log')
plt.xlabel(r'$T$')
plt.ylabel(r'$H_{g}$')
plt.ylim(0, max(H[-1])+10)
plt.xticks([1, 2, 2.269, 3,  4, 5, 6, 7, 8, 9, 10], [1, 2, r'$T_{c}$', 3, 4, 5, 6, 7, 8, 9, 10])
plt.savefig('hetero.png', dpi=400)

