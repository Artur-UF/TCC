import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 12})

L = [200, 500, 800]
TI = 2.
TF = 3.
dT = 0.03

n1 = [np.loadtxt(f'n1_{L[0]}.dat'), np.loadtxt(f'n1_{L[1]}.dat'), np.loadtxt(f'n1_{L[2]}.dat')]
T = np.arange(TI, TF+dT, dT)

markers = ['v', '^', 's']


fig, ax = plt.subplots(1, 1, layout='constrained')
for l in range(len(L)):
    plt.plot(T, n1[l], linewidth=.8, marker=markers[l], label=f'L = {L[l]}')
plt.vlines(2.269, min(n1[0])*.9, max(n1[0])*1.1, colors='k', linestyle='dashed', linewidth=.5)
plt.legend()
#plt.xscale('log')
#plt.yscale('log')
plt.xlabel(r'$T$')
plt.ylabel(r'$\left \langle n_{1}\right \rangle/L^{2}$')
plt.ylim(min(n1[0])*0.9, max(n1[0])*1.1)
plt.xlim(TI-dT, TF+dT)
#plt.xticks([2, 2.269]+list(range(3, 21)), [2, r'$T_{c}$']+list(range(3, 21)))
#plt.grid()
plt.savefig('n1_nearTc.png', dpi=400)

