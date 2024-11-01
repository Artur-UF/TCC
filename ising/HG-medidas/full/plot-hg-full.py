#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 30})


colors = ['b', 'g', 'r', 'purple', 'orange', 'magenta']
markers = ['s', '^', 'v', '*', 'd', '>']

def labelL(i, L):
    if i == 0:
        return f'L = {L}'
    else:
        return f'\t{L}'

fig, ax = plt.subplots(1, 2, figsize=(19, 7), layout='constrained')

plt.rc('axes', titlesize=30, labelsize=27)
plt.subplot(121)

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

colors1 = ['g', 'brown', 'olive']
for i in range(len(L)):
    plt.plot(T[i], Hntc[i], linewidth=.5, color=colors1[i], marker=markers[i], markersize=8, label=labelL(i, L[i]))
plt.vlines(2.269, 0, max(Hntc[-1])+25, colors='k', linestyle='dashed', linewidth=.7)
plt.legend()
#plt.xscale('log')
plt.xlabel(r'$T$')
plt.ylabel(r'$H$')
plt.ylim(0, 500) #max(Hntc[-1])+30)
plt.xlim(2.1, 2.4)
plt.yticks([0, 100, 300, 500], [0, 100, 300, 500])
plt.xticks([2.1, 2.20, 2.269, 2.30, 2.40], [2.10, 2.20, r'$T_c$', 2.30, 2.40])
#plt.grid()

plt.subplot(122)

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
    plt.plot(T[i], H[i], linewidth=.5, color=colors[i], marker=markers[i], markersize=8, label=labelL(i, L[i]))
plt.vlines(2.269, 0, max(H[-1])+25, colors='k', linestyle='dashed', linewidth=.7)
plt.legend()
ax[1].add_patch(Rectangle((2.1, 0), 0.3, 500, ec='k', fc='none'))
plt.xlabel(r'$T$')
plt.ylabel(r'$H$')
plt.ylim(0, max(H[-1])+30)
plt.yticks([0, 400, 800, 1200], [0, 400, 800, 1200])
plt.xticks([1, 2.269, 3,  5, 7, 9], [1, r'$T_{c}$', 3, 5, 7, 9])
#plt.grid()

plt.savefig('hg-full.png', dpi=500)

