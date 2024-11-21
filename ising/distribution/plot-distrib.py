import matplotlib.pyplot as plt
import numpy as np
from glob import glob
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 15})

L = 640

path = f'distri-{L}'

lin_files = sorted(glob(path+'/lin-*'))
log_files = sorted(glob(path+'/log-*'))

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

plt.figure(2, layout='constrained', figsize=(10, 10))
for i in range(len(lin_files)):
    sizes, freq = np.loadtxt(lin_files[i], unpack=True)
    params = lin_files[i].split('_')
    T = float(params[3])
    cut = -1
    plt.plot(sizes[:cut], freq[:cut], marker='<', label=f'T = {T:.2f}')

x = np.linspace(1, 500, 200)
y = x**(-187/91)*12000
y2 = x**(-1.66)*40000
plt.plot(x, y, label=r'$A^{-187/91}$')
plt.plot(x, y2, label=r'$A^{-1.66}$')

plt.title(f'L = {L}')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('A')
plt.legend()
plt.savefig(f'linear_dist_L_{L}.png', dpi=400)

