#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 8})

colors = ['b', 'g', 'r', 'purple', 'orange', 'magenta']
markers = ['s', '^', 'v', '*', 'd', '>']

fig, ax = plt.subplots(2, 1, figsize=(6, 9), layout='constrained')

plt.subplot(211)

L = [320, 800, 1500]
TI = 2.1
TF = 2.8
dT = 0.02

Hntc = list()
T = list()
for l in range(len(L)):
    hg, t = np.loadtxt(f'hg-nearTc-{L[l]}.dat', unpack=True)
    Hntc.append(hg)
    T.append(t)

for i in range(len(L)):
    plt.plot(T[i], Hntc[i], linewidth=.5, color=colors[i], marker=markers[i], markersize=2, label=f'L = {L[i]}')
plt.vlines(2.269, 0, max(Hntc[-1])+25, colors='k', linestyle='dashed', linewidth=.7)
plt.legend()
#plt.xscale('log')
plt.xlabel(r'\Large{$T$}')
plt.ylabel(r'\Large{$H_{g}$}')
plt.ylim(0, 500) #max(Hntc[-1])+30)
plt.xlim(2.1, 2.4)
plt.xticks([2.1, 2.15, 2.20, 2.25, 2.269, 2.30, 2.35, 2.40], [2.10, 2.15, 2.20, 2.25, r'$T_c$', 2.30, 2.35, 2.40])
#plt.grid()

plt.subplot(212)

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

for i in range(len(L)):
    plt.plot(T[i], H[i], linewidth=.5, color=colors[i], marker=markers[i], markersize=2, label=f'L = {L[i]}')
plt.vlines(2.269, 0, max(H[-1])+25, colors='k', linestyle='dashed', linewidth=.7)
plt.legend()
#plt.xscale('log')
plt.xlabel(r'\Large{$T$}')
plt.ylabel(r'\Large{$H_{g}$}')
plt.ylim(0, max(H[-1])+30)
plt.xticks([1, 2.269, 3,  4, 5, 6, 7, 8, 9, 10], [1, r'$T_{c}$', 3, 4, 5, 6, 7, 8, 9, 10])
#plt.grid()

plt.savefig('hg-full-vert.png', dpi=400)

