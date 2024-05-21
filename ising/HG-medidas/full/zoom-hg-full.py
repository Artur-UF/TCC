#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 8})

colors = ['b', 'g', 'r', 'purple', 'orange', 'magenta']
markers = ['s', '^', 'v', '*', 'd', '>']

fig, ax = plt.subplots(1, 1, figsize=(8, 8), layout='constrained')

L = [160, 320, 640, 960, 1280, 1600]
TI = 1.
TF = 10.
dT = 0.5
T = np.arange(TI, TF+dT, dT)

H = list()
T = list()
for l in range(len(L)):
    hg, t = np.loadtxt(f'full-hg/hg-full-{L[l]}.dat', unpack=True)
    H.append(hg)
    T.append(t)

plt.subplot(111)

for i in range(len(L)):
    plt.plot(T[i], H[i], linewidth=.5, color=colors[i], marker=markers[i], markersize=2, label=f'L = {L[i]}')
plt.vlines(2.269, 0, max(H[-1])+25, colors='k', linestyle='dashed', linewidth=.7)
plt.legend()
plt.xscale('log')
plt.xlabel(r'$T$')
plt.ylabel(r'$H_{g}$')
plt.ylim(0, max(H[-1])+30)
plt.xticks([1, 2, 2.269, 3,  4, 5, 6, 7, 8, 9, 10], [1, 2, r'$T_{c}$', 3, 4, 5, 6, 7, 8, 9, 10])
#plt.grid()

plt.show()
#plt.savefig('zoom-hg.png', dpi=400)

