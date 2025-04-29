import matplotlib.pyplot as plt
import numpy as np
from glob import glob
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 25})

L = 1000

path = f'distri-{L}'

lin_files = sorted(glob(path+'/lin-*'))
log_files = sorted(glob(path+'/log-*'))


#----------------------- LOG ---------------------------


plt.figure(1, layout='constrained', figsize=(10, 10))
for i in range(len(log_files)):
    sizes, freq = np.loadtxt(log_files[i], unpack=True)
    params = log_files[i].split('_')
    T = float(params[3])
    plt.plot(sizes, freq, marker='>', label=f'T = {T:.2f}')

plt.title(f'L = {L}')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('A')
plt.legend()
plt.savefig(f'log_dist_L_{L}.png', dpi=400)


#---------------------------- LINEAR ----------------------------

color = ['r', 'b', 'g', 'purple', 'orange', 'brown']

marker = ['^', 'v', 'o', '*', 's', 'h']

fig, ax = plt.subplots(1, 2, layout='constrained', figsize=(16, 9))

tau = 379/187

for i in range(len(lin_files)):
    sizes, freq = np.loadtxt(lin_files[i], unpack=True)
    params = lin_files[i].split('_')
    T = float(params[3])
    cut = -1
    sizes = sizes[:cut]
    freq = freq[:cut]
    plt.subplot(121)
    plt.scatter(sizes, freq, marker=marker[i], color=color[i], label=f'T = {T:.2f}')
    plt.subplot(122)
    plt.scatter(np.log10(sizes), np.log10(freq*(sizes**tau)), marker=marker[i], color=color[i], label=f'T = {T:.2f}')
#    plt.scatter(np.log10(sizes/(freq**tau)), np.log10(freq*(sizes**tau)), marker=marker[i], color=color[i], label=f'T = {T:.2f}')

plt.subplot(121)
x = np.linspace(1, 500, 200)
y = x**(-379/187)*10000
#y2 = x**(-1.66)*50000
plt.plot(x, y, 'k--', label=r'$A^{-379/187}$')
#plt.plot(x, y2, 'k--', label=r'$A^{-1.66}$')
plt.xscale('log')
plt.yscale('log')

plt.ylabel(r'$\log (n_{A})$', fontsize=35, labelpad=12)
plt.xlabel(r'$\log (A)$', fontsize=35)
plt.legend()
plt.text(10**(-0.2), 10**(-3.5), '(a)')

plt.subplot(122)
ylim = (3.4, 7)
xlim = (-0.5, 5)

plt.hlines(4.5, xlim[0], xlim[1], 'k', linestyles='dashed', zorder=0)

plt.yticks([4, 5, 6, 7, 8], [4, 5, 6, 7, 8])
plt.xticks([0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6])
plt.ylim(ylim[0], ylim[1])
plt.xlim(xlim[0], xlim[1])


#plt.title(rf'$\tau = {tau:.3f}$')
plt.ylabel(r'$\log (n_{A}A^{\tau})$', fontsize=35, labelpad=12)
plt.xlabel(r'$\log (A)$', fontsize=35)
#plt.xlabel(r'$\log (A/n_A^\tau)$', fontsize=35)
plt.legend(loc='upper left')
plt.text(-0.4, 3.5, '(b)')

#plt.suptitle(rf'$L = {L}$')
plt.savefig(f'linear-fuller_dist_L_{L}.png', dpi=400)

