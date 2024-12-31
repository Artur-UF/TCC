import matplotlib.pyplot as plt
import numpy as np
from glob import glob
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 30})

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


plt.figure(2, layout='constrained', figsize=(10, 10))

tau = 187/91

for i in range(len(lin_files)):
    sizes, freq = np.loadtxt(lin_files[i], unpack=True)
    params = lin_files[i].split('_')
    T = float(params[3])
    cut = -1
    sizes = sizes[:cut]
    freq = freq[:cut]
    plt.scatter(np.log10(sizes/(freq**tau)), np.log10(freq*(sizes**tau)), marker='<', label=f'T = {T:.2f}')

x = np.linspace(1, 500, 200)
y = x**(-187/91)*7000
y2 = x**(-1.66)*20000
#plt.plot(x, y, label=r'$A^{-187/91}$')
#plt.plot(x, y2, label=r'$A^{-1.66}$')
ylim = (3.4, 8.6)
xlim = (-10, 13)

plt.hlines(4.5, xlim[0], xlim[1], 'k', linestyles='dashed', zorder=0)

plt.yticks([4, 5, 6, 7, 8], [4, 5, 6, 7, 8])
plt.xticks([-10, -5, 0, 5, 10], [-10, -5, 0, 5, 10])
plt.ylim(ylim[0], ylim[1])
plt.xlim(xlim[0], xlim[1])


plt.title(rf'$L = {L} \> |\>  \tau = {tau:.3f}$')
#plt.yscale('log')
#plt.xscale('log')
plt.ylabel(r'$\log (n_{A}A^{\tau})$', fontsize=35, labelpad=12)
plt.xlabel(r'$\log (A/n_A^\tau)$', fontsize=35)
plt.legend()
plt.savefig(f'linear_dist_L_{L}.png', dpi=400)

