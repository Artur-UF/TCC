import matplotlib.pyplot as plt
import numpy as np
from glob import glob
plt.rcParams.update({"text.usetex" : True, "font.family" : "serif", "font.serif" : ["Computer Modern Serif"], "font.size" : 20})


tc_files = sorted(glob('tc-hh*'))
files = sorted(glob('hh*'))


marker = ['>', '^', 's', '+']
color = ['r', 'b', 'g', 'purple']

fig, ax = plt.subplots(1, 2, figsize=(12, 5), layout='constrained')


plt.subplot(121)
for i in range(len(tc_files)):
    t, hh = np.loadtxt(tc_files[i], unpack=True)
    plt.plot(t, hh, marker=marker[i], color=color[i], label=rf'$L = {int(tc_files[i].split('_')[1])}$')
plt.xlabel(r'$T$', fontsize=30)
plt.ylabel(r'$H_{hull}$', fontsize=30)
plt.legend(loc='lower right')

plt.subplot(122)
for i in range(len(files)):
    t, hh = np.loadtxt(files[i], unpack=True)
    plt.plot(t, hh, marker=marker[i], color=color[i], label=rf'$L = {int(files[i].split('_')[1])}$')
plt.xlabel(r'$T$', fontsize=30)
plt.ylabel(r'$H_{hull}$', fontsize=30)
plt.legend()


plt.savefig('fig-hh.png', dpi=400)


