import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 12})

L = [320, 800]
TI = 2.1
TF = 2.8
dT = 0.02

cls = [np.loadtxt(f'clsize_{L[0]}.dat'), np.loadtxt(f'clsize_{L[1]}.dat')]
T = np.arange(TI, TF+dT, dT)

markers = ['v', '^']


fig, ax = plt.subplots(1, 1, layout='constrained')
for l in range(len(L)):
    plt.plot(T, cls[l], linewidth=.8, marker=markers[l], label=f'L = {L[l]}')
plt.vlines(2.269, min(cls[0])*.9, max(cls[1])*1.1, colors='k', linestyle='dashed', linewidth=.5)
plt.legend()
#plt.xscale('log')
#plt.yscale('log')
plt.xlabel(r'$T$')
plt.ylabel(r'$\left \langle A \right \rangle$')
plt.ylim(min(cls[0])*0.95, max(cls[1])*1.05) #6max()*1.5)
plt.xlim(TI, TF)
#plt.xticks([2, 2.269]+list(range(3, 21)), [2, r'$T_{c}$']+list(range(3, 21)))
#plt.grid()
plt.savefig('meansize.png', dpi=400)
