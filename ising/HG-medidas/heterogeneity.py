#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 12})


L = [160, 320, 640, 960, 1280, 1600]
TI = 1.
TF = 10.
dT = 0.5
T = np.arange(TI, TF+dT, dT)

H = list()
for l in range(len(L)):
    H.append(np.loadtxt(f'Hg_L_{L[l]}.dat'))

peaks = [[], []]


colors = ['b', 'g', 'r', 'purple', 'orange', 'magenta']
markers = ['s', '^', 'v', '*', 'd', '>']

fig, ax = plt.subplots(1, 1, layout='constrained')
for i in range(len(L)):
    if i == 2:
        Td = np.arange(4, 5.1, .1)
        hgd = np.loadtxt('dense_hg_640.dat')
        plt.plot(Td, hgd, c=colors[i], linewidth=.8, marker=markers[i])
        peaks[0].append(Td[np.where(hgd == max(hgd))])
        peaks[1].append(max(hgd))
        plt.vlines(peaks[0][0], peaks[1][0]-10, peaks[1][0]+10, colors='k', zorder=4)
    if i == 3:
        Td = np.arange(3.7, 4.8, .1)
        hgd = np.loadtxt('dense_hg_960.dat')
        plt.plot(Td, hgd, c=colors[i], linewidth=.8, marker=markers[i])
        peaks[0].append(Td[np.where(hgd == max(hgd))])
        peaks[1].append(max(hgd))
        plt.vlines(peaks[0][1], peaks[1][1]-10, peaks[1][1]+10, colors='k', zorder=4)
    if i == 4:
        Td = np.arange(3.5, 4.55, .05)
        hgd = np.loadtxt('dense_hg_1280.dat')
        plt.plot(Td, hgd, c=colors[i], linewidth=.8, marker=markers[i])
        peaks[0].append(Td[np.where(hgd == max(hgd))])
        peaks[1].append(max(hgd))
        plt.vlines(peaks[0][2], peaks[1][2]-10, peaks[1][2]+10, colors='k', zorder=4)
    if i == 5:
        Td = np.arange(3.3, 4.35, .1)
        hgd = np.loadtxt('dense_hg_1600.dat')
        plt.plot(Td, hgd, c=colors[i], linewidth=.8, marker=markers[i])
        peaks[0].append(Td[np.where(hgd == max(hgd))])
        peaks[1].append(max(hgd))
        plt.vlines(peaks[0][3], peaks[1][3]-10, peaks[1][3]+10, colors='k', zorder=4)
    plt.plot(T, H[i], linewidth=.8, color=colors[i], marker=markers[i], label=f'L = {L[i]}')
plt.vlines(2.269, 0, max(H[-1])+25, colors='k', linestyle='dashed', linewidth=.7)
plt.plot(peaks[0], peaks[1], 'k')
plt.legend()
plt.xscale('log')
plt.xlabel(r'$T$')
plt.ylabel(r'$H_{g}$')
plt.ylim(0, max(H[-1])+30)
plt.xticks([1, 2, 2.269, 3,  4, 5, 6, 7, 8, 9, 10], [1, 2, r'$T_{c}$', 3, 4, 5, 6, 7, 8, 9, 10])
plt.grid()
plt.savefig('hetero.png', dpi=400)

