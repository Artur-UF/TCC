import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 12})

L = 200
TI = 2
TF = 10
dT = 0.5

n1 = np.loadtxt(f'n1_L_{L}.dat')
T = np.arange(TI, TF+dT, dT)

fig, ax = plt.subplots(1, 1, layout='constrained')
plt.plot(T, n1, linewidth=.8, marker='^', label=f'L = {L}')
plt.vlines(2.269, 0, max(n1)*1.1, colors='k', linewidth=.7)
plt.legend()
#plt.xscale('log')
plt.xlabel(r'$T$')
plt.ylabel(r'$\left \langle n_{1}\right \rangle/L^{2}$')
plt.ylim(0, max(n1)*1.1)
#plt.xticks([1, 2, 2.269, 3,  4, 5, 6, 7, 8, 9, 10], [1, 2, r'$T_{c}$', 3, 4, 5, 6, 7, 8, 9, 10])
plt.savefig('n1.png', dpi=400)





