import matplotlib.pyplot as plt
import numpy as np
from glob import glob
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 15})

tc_hh_files = sorted(glob('tc-hh*'))
hh_files = sorted(glob('hh*'))

tc_hg_files = sorted(glob('tc-Hg*'))
hg_files = sorted(glob('Hg*'))


marker = ['^', 's', 'o']
color = ['r', 'b', 'g']

fig, ax = plt.subplots(1, 2, figsize=(12, 5), layout='constrained')

linewidth = 0.7
markersize = 5
tc = 2.269


def legenda(l, i, h):
    if i == 0 and h == 'hg':
        return rf'$L = {l}$'
    if i == 0 and h == 'hh':
        return rf'$L = {l}$'
    if i > 0:
        return rf'${l}$'


plt.subplot(121)
for i in range(len(tc_hg_files)):
    h, h2, t = np.loadtxt(tc_hg_files[i], unpack=True)
    plt.plot(t, h2, linewidth=linewidth, markersize=markersize, marker=marker[i], color=color[i], linestyle='solid', label=legenda(int(tc_hg_files[i].split('_')[1]), i, 'hg'))

ylim = (3000, 290000)


plt.vlines(tc, ylim[0], ylim[1], 'k', linestyles='dashed', linewidth=0.5)
plt.ylim(ylim[0], ylim[1])
plt.xlim(2.1, 2.405)
plt.xlabel(r'$T$', fontsize=25)
plt.ylabel(r'$\left\langle H^2 \right\rangle - \left\langle H \right\rangle ^2$', fontsize=25, labelpad=12)
plt.xticks([2.1, 2.2, tc, 2.3, 2.4], [2.1, 2.2, r'$T_c$', 2.3, 2.4])

plt.legend(loc='upper left', ncols=1, fontsize=12)


plt.subplot(122)
for i in range(len(hg_files)):
    h, h2, t = np.loadtxt(hg_files[i], unpack=True)
    plt.plot(t, h2, linewidth=linewidth, markersize=markersize, marker=marker[i], color=color[i], linestyle='solid', label=legenda(int(hg_files[i].split('_')[1]), i, 'hg'))


ylim = (0, 1500000)


plt.vlines(tc, ylim[0], ylim[1], 'k', linestyles='dashed', linewidth=0.5)
plt.ylim(ylim[0], ylim[1])
plt.xlim(1, 10.1)
plt.xlabel(r'$T$', fontsize=25)
plt.ylabel(r'$\left\langle H^2 \right\rangle - \left\langle H \right\rangle ^2$', fontsize=25, labelpad=12)
plt.xticks([1, tc, 3, 5, 7, 9], [1, r'$T_c$', 3, 5, 7, 9])
plt.legend(loc='upper right', ncols=1, fontsize=12)


plt.savefig('fig-h2.png', dpi=400)



