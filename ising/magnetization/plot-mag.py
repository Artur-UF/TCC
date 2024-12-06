import matplotlib.pyplot as plt
from glob import glob
import numpy as np
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 25})


samples = sorted(glob('*results.dat'))


plt.figure(1, figsize=(10, 8), layout='constrained')

c = ['r', 'b', 'g']
marker = ['^', 's', '>']

for i in range(len(samples)):
    T, M = np.loadtxt(samples[i], unpack=True)
    L = int(samples[i].split('-')[1])
    plt.plot(T, M, c=c[i], marker=marker[i], label=fr'$L={L}$')

plt.xlabel(r'$T$')
plt.ylabel(r'$\left \langle \left | m(T) \right | \right \rangle$')
plt.vlines(2.269, 0, 1.02, 'k', linestyles='dashed')
plt.ylim(0, 1.02)
plt.xlim(1, 3)
plt.xticks([1, 1.5, 2., 2.269, 2.5, 3.], [1, 1.5, 2., r'$T_c$', 2.5, 3.])
plt.legend(loc='lower left')
plt.savefig('fig-mag.png', dpi=400)



