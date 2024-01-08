import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 12})

L = [500, 800]
TI = 2
TF = 40
dT = 1

n1 = [np.loadtxt(f'n1_high_{L[0]}.dat'), np.loadtxt(f'n1_high_{L[1]}.dat')]
T = np.arange(TI, TF+dT, dT)

markers = ['v', '^']


fig, ax = plt.subplots(1, 1, layout='constrained')
for l in range(len(L)):
    plt.plot(T, n1[l], linewidth=.8, marker=markers[l], label=f'L = {L[l]}')
plt.hlines(0.06254976, 37, 40, colors='r', linewidth=.5, label=r'$T \to \infty$')
plt.vlines(2.269, min(n1[0])*.9, 0.06254976*1.1, colors='k', linestyle='dashed', linewidth=.5)
plt.legend(loc='lower right')
#plt.xscale('log')
#plt.yscale('log')
plt.xlabel(r'$T$')
plt.ylabel(r'$\left \langle n_{1}\right \rangle/L^{2}$')
plt.ylim(min(n1[0])*0.95, 0.0625497*1.05) #6max(n1)*1.5)
plt.xlim(1, 40)
#plt.xticks([2, 2.269]+list(range(3, 21)), [2, r'$T_{c}$']+list(range(3, 21)))
#plt.grid()
plt.savefig('n1_highT.png', dpi=400)

