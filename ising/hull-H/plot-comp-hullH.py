import matplotlib.pyplot as plt
import numpy as np
from glob import glob
from matplotlib.patches import Rectangle
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 15})

tc_hh_files = sorted(glob('tc-hh*'))
hh_files = sorted(glob('hh*'))

tc_hg_files = sorted(glob('tc-Hg*'))
hg_files = sorted(glob('Hg*'))


marker = ['>', '^', 's', '+', 'v', 'o']
color = ['r', 'b', 'g', 'purple', 'brown', 'olive']

fig, ax = plt.subplots(1, 2, figsize=(12, 5), layout='constrained')

linewidth = 0.7
markersize = 3
tc = 2.269


def legenda(l, i, h):
    if i == 0 and h == 'hg':
        return rf'$L = {l}$'
    if i == 0 and h == 'hh':
        return rf'$L = {l}$'
    if i > 0:
        return rf'${l}$'


plt.subplot(121)
for i in range(len(tc_hh_files)):
    t, hh = np.loadtxt(tc_hh_files[i], unpack=True)
    plt.plot(t, hh, linewidth=linewidth, markersize=markersize, marker=marker[i], color=color[i], label=legenda(int(tc_hh_files[i].split('_')[1]), i, 'hh'))

for i in range(len(tc_hg_files)):
    h, h2, t = np.loadtxt(tc_hg_files[i], unpack=True)
    plt.plot(t, h, linewidth=linewidth, markersize=markersize, marker=marker[-(i+1)], color=color[-(i+1)], linestyle='dashed', label=legenda(int(tc_hg_files[i].split('_')[1]), i, 'hg'))

ylim = (50, 550)
xlim = (2.1, 2.405)

plt.vlines(tc, ylim[0], ylim[1], 'k', linestyles='dashed', linewidth=0.5)
plt.ylim(ylim[0], ylim[1])
plt.xlim(xlim[0], xlim[1])
plt.xlabel(r'$T$', fontsize=30)
plt.ylabel(r'$H$', fontsize=30)
plt.xticks([2.1, 2.2, tc, 2.3, 2.4], [2.1, 2.2, r'$T_c$', 2.3, 2.4])
plt.text(2.11, 190, '(a)')

plt.legend(loc='upper left', ncols=2, title=r'H-Perímetro $\>\>$ H-Tamanho', fontsize=12)


plt.subplot(122)
for i in range(len(hh_files)):
    t, hh = np.loadtxt(hh_files[i], unpack=True)
    plt.plot(t, hh, linewidth=linewidth, markersize=markersize, marker=marker[i], color=color[i], label=legenda(int(hh_files[i].split('_')[1]), i, 'hh'))

for i in range(len(hg_files)):
    h, h2, t = np.loadtxt(hg_files[i], unpack=True)
    plt.plot(t, h, linewidth=linewidth, markersize=markersize, marker=marker[-(i+1)], color=color[-(i+1)], linestyle='dashed', label=legenda(int(hg_files[i].split('_')[1]), i, 'hg'))

ylim = (0, 1250)
xlim = (1, 10.1)

plt.vlines(tc, ylim[0], ylim[1], 'k', linestyles='dashed', linewidth=0.5)
plt.ylim(ylim[0], ylim[1])
plt.xlim(xlim[0], xlim[1])
plt.xlabel(r'$T$', fontsize=30)
plt.ylabel(r'$H$', fontsize=30)
plt.xticks([1, tc, 3, 5, 7, 9], [1, r'$T_c$', 3, 5, 7, 9])
plt.legend(loc='lower right', ncols=2, title=r'H-Perímetro $\>\>$ H-Tamanho', fontsize=12)
plt.text(1.4, 390, '(b)')

ax[1].add_patch(Rectangle((2.1, 0), 0.3, 300, ec='k', fc='none'))

plt.savefig('fig-hh.png', dpi=400)











