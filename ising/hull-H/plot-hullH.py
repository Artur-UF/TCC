import matplotlib.pyplot as plt
import numpy as np
from glob import glob
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 20})


hg_files = sorted(glob('Hg-full*'))
hh_files = sorted(glob('hh-full*'))


marker2 = ['o', '^', 'v']
marker1 = [r'$\bigcirc$', r'$\bigtriangleup$', r'$\bigtriangledown$']

color = ['r', 'b', 'g']

plt.figure(1, figsize=(12, 8), layout='constrained')


for i in range(len(hh_files)):
    hg, h2, t = np.loadtxt(hg_files[i], unpack=True)
    plt.plot(t, hg, marker=marker2[i], color=color[i], label=rf'$L = {int(hg_files[i].split('_')[1])}$')
    t, hh = np.loadtxt(hh_files[i], unpack=True)
    plt.plot(t, hh, marker=marker1[i], color=color[i], label=rf'$L = {int(hh_files[i].split('_')[1])}$')


plt.xlabel(r'$T$', fontsize=30)
plt.ylabel(r'$H_{hull}$', fontsize=30)
plt.yscale('log')
plt.xscale('log')
plt.legend(loc='lower right')


plt.savefig('fig-full-hh.png', dpi=400)


